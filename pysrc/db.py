import json
import struct
import chain

idx64 = 0
idx128 = 1
idx256 = 2
idx_double = 3
idx_long_double = 4

primary_type_i64 = 0
primary_type_i256 = 1

# Name represent as str or int
Name = str

class ChainDB(object):
    def __init__(self, primary_type: int, code: Name, scope: Name, table: Name, data_type):
        self.code = code
        self.scope = scope
        self.table = table
        self.data_type = data_type
        self.primary_type = primary_type

        if primary_type == primary_type_i64:
            self._db_find = chain.db_find_i64
            self._db_get = chain.db_get_i64
            self._db_store = chain.db_store_i64
            self._db_update = chain.db_update_i64
            self._db_remove = chain.db_remove_i64
            self._lowerbound = chain.db_lowerbound_i64
            self._upperbound = chain.db_upperbound_i64
        else:
            self._db_find = chain.db_find_i256
            self._db_get = chain.db_get_i256
            self._db_store = chain.db_store_i256
            self._db_update = chain.db_update_i256
            self._db_remove = chain.db_remove_i256
            self._lowerbound = chain.db_lowerbound_i256
            self._upperbound = chain.db_upperbound_i256

    def find(self, primary_key: int):
        return self._db_find(self.code, self.scope, self.table, primary_key)

    def get(self, itr: int):
        '''
        
        '''
        if itr < 0:
            raise IndexError
        data = self._db_get(itr)
        return self.data_type.unpack(data)

    def upper_bound(self, primary: int):
        '''

        '''
        return self._upperbound(self.code, self.scope, self.table, primary)

    def lower_bound(self, primary: int):
        return self._lowerbound(self.code, self.scope, self.table, primary)

    def load(self, primary_key: int):
        itr = self.find(primary_key)
        if itr < 0:
            return None
        return self.get(itr)

    def store(self, obj):
        primary_key = obj.get_primary_key()
        itr = self._db_find(self.code, self.scope, self.table, primary_key)
        if itr < 0:
            self._db_store(self.scope, self.table, obj.payer, primary_key, obj.pack())
        else:
            self._db_update(itr, obj.payer, obj.pack())

    def remove(self, primary_key: int):
        itr = self._db_find(self.code, self.scope, self.table, primary_key)
        if itr < 0:
            raise IndexError
        self._db_remove(itr)

    def __len__(self):
        return chain.db_get_table_row_count(self.code, self.scope, self.table)

    def remove_by_itr(self, itr: int):
        self._db_remove(itr)

class ChainDBKey64(ChainDB):
    def __init__(self, code, scope, table, data_type):
        ChainDB.__init__(self, primary_type_i64, code, scope, table, data_type)

class ChainDBKey256(ChainDB):
    def __init__(self, code, scope, table, data_type):
        ChainDB.__init__(self, primary_type_i256, code, scope, table, data_type)

class MultiIndex:
    def __init__(self, code, scope, table, data_type):
        self.code = code
        self.scope = scope
        self.table = table
        self.indexes = data_type.get_secondary_indexes()
        self.data_type = data_type
        self.primary_key = 0
        self.idx_tables = []
        for i in range(len(self.indexes)):
            table = (int(self.table) & 0xFFFFFFFFFFFFFFF0) | i
            self.idx_tables.append(table)

    def find(self, primary_key):
        return chain.db_find_i64(self.code, self.scope, self.table, primary_key)

    def get(self, itr):
        if itr < 0:
            raise IndexError
        data = chain.db_get_i64(itr)
        return self.data_type.unpack(data)

    def get_secondary_values(self, primary_key):
        values = []
        i = 0
        for idx in self.indexes:
            table = self.idx_tables[i]
            itr, secondary = chain.db_idx_find_primary(idx, self.code, self.scope, table, primary_key)
            if itr < 0:
                return None
            values.append(secondary)
            i += 1
        return values

    def __getitem__(self, primary_key):
        itr = self.find(primary_key)
        if itr < 0:
            raise IndexError
        return self.get(itr)

    def __setitem__(self, primary_key, obj):
        assert primary_key == obj.get_primary_key()
        self.store(obj)

    def load(self, primary_key):
        itr = self.find(primary_key)
        if itr < 0:
            return None
        return self.get(itr)

    def store(self, obj):
        primary = obj.get_primary_key()
        itr = chain.db_find_i64(self.code, self.scope, self.table, primary)        
        if itr < 0:
            chain.db_store_i64(self.scope, self.table, obj.payer, primary, obj.pack())
            i = 0
            for idx in self.indexes:
                table = self.idx_tables[i]
                chain.db_idx_store(idx, self.scope, table, obj.payer, primary, obj.get_secondary_values()[i])
                i += 1
        else:
            chain.db_update_i64(itr, obj.payer, obj.pack())
            i = 0
            for idx in self.indexes:
                table = self.idx_tables[i]
                itr, old_secondary = chain.db_idx_find_primary(idx, self.code, self.scope, table, primary)
                secondary = obj.get_secondary_values()[i]
                if not secondary == old_secondary:
                    chain.db_idx_update(idx, itr, obj.payer, secondary)
                i += 1

    def remove(self, primary_key):
        itr = chain.db_find_i64(self.code, self.scope, self.table, primary_key)
        if itr < 0:
            raise IndexError
        chain.db_remove_i64(itr)
        i = 0
        for idx in self.indexes:
            table = self.idx_tables[i]
            itr, _ = chain.db_idx_find_primary(idx, self.code, self.scope, table, primary_key)
            assert itr >= 0
            chain.db_idx_remove(idx, itr)
            i += 1

    def __delitem__(self, primary_key):
        self.remove(primary_key)

    def __contains__(self, primary_key):
        return chain.db_find_i64(self.code, self.scope, self.table, primary_key) >= 0

    def __iter__(self):
        self.itr = chain.db_end_i64(self.code, self.scope, self.table)
        return self

    def __next__(self):
        if self.itr == -1:
            raise StopIteration
        self.itr, self.primary_key = chain.db_previous_i64(self.itr)
        if self.itr < 0:
            raise StopIteration
        return self.get(self.itr)

    def __len__(self):
        row_count = chain.db_get_table_row_count(self.code, self.scope, self.table)
        if self.indexes:
            row_count /= 2
        return row_count

    def get_secondary_index(self, idx):
        return SecondaryIndex(self, self.indexes[idx], self.data_type)

    def upper_bound(self, primary):
        return chain.db_upperbound_i64(self.code, self.scope, self.table, primary)

    def lower_bound(self, primary):
        return chain.db_lowerbound_i64(self.code, self.scope, self.table, primary)

    def idx_find(self, index, secondary_key):
        idx = self.indexes[index]
        return chain.db_idx_find_secondary(idx, self.code, self.scope, self.table, secondary_key)

    def idx_upper_bound(self, index, secondary_key):
        idx = self.indexes[index]
        idx_table = self.idx_tables[index]
        return chain.db_idx_upperbound(idx, self.code, self.scope, idx_table, secondary_key)

    def idx_lower_bound(self, index, secondary_key):
        idx = self.indexes[index]
        idx_table = self.idx_tables[index]
        return chain.db_idx_lowerbound(idx, self.code, self.scope, idx_table, secondary_key)

def _say_hello(msg):
    print('++++hello,world')

