# Db

> Auto-generated documentation for [pysrc.db](https://github.com/uuosio/python-contracts-dev-kit/blob/master/pysrc/db.py) module.

- [Python-contract-dev-kit](../README.md#python-contracts-dev-kit) / [Modules](../MODULES.md#python-contract-dev-kit-modules) / [Pysrc](index.md#pysrc) / Db
    - [ChainDB](#chaindb)
        - [ChainDB().find](#chaindbfind)
        - [ChainDB().get](#chaindbget)
        - [ChainDB().load](#chaindbload)
        - [ChainDB().lower_bound](#chaindblower_bound)
        - [ChainDB().remove](#chaindbremove)
        - [ChainDB().remove_by_itr](#chaindbremove_by_itr)
        - [ChainDB().store](#chaindbstore)
        - [ChainDB().upper_bound](#chaindbupper_bound)
    - [ChainDBKey256](#chaindbkey256)
    - [ChainDBKey64](#chaindbkey64)
    - [MultiIndex](#multiindex)
        - [MultiIndex().find](#multiindexfind)
        - [MultiIndex().get](#multiindexget)
        - [MultiIndex().get_secondary_index](#multiindexget_secondary_index)
        - [MultiIndex().get_secondary_values](#multiindexget_secondary_values)
        - [MultiIndex().idx_find](#multiindexidx_find)
        - [MultiIndex().idx_lower_bound](#multiindexidx_lower_bound)
        - [MultiIndex().idx_upper_bound](#multiindexidx_upper_bound)
        - [MultiIndex().load](#multiindexload)
        - [MultiIndex().lower_bound](#multiindexlower_bound)
        - [MultiIndex().remove](#multiindexremove)
        - [MultiIndex().store](#multiindexstore)
        - [MultiIndex().upper_bound](#multiindexupper_bound)

#### Attributes

- `Name` - Name represent as str or int: `str`

## ChainDB

[[find in source code]](https://github.com/uuosio/python-contracts-dev-kit/blob/master/pysrc/db.py#L17)

```python
class ChainDB(object):
    def __init__(
        primary_type: int,
        code: Name,
        scope: Name,
        table: Name,
        data_type,
    ):
```

#### See also

- [Name](#name)

### ChainDB().find

[[find in source code]](https://github.com/uuosio/python-contracts-dev-kit/blob/master/pysrc/db.py#L42)

```python
def find(primary_key: int):
```

### ChainDB().get

[[find in source code]](https://github.com/uuosio/python-contracts-dev-kit/blob/master/pysrc/db.py#L45)

```python
def get(itr: int):
```

### ChainDB().load

[[find in source code]](https://github.com/uuosio/python-contracts-dev-kit/blob/master/pysrc/db.py#L63)

```python
def load(primary_key: int):
```

### ChainDB().lower_bound

[[find in source code]](https://github.com/uuosio/python-contracts-dev-kit/blob/master/pysrc/db.py#L60)

```python
def lower_bound(primary: int):
```

### ChainDB().remove

[[find in source code]](https://github.com/uuosio/python-contracts-dev-kit/blob/master/pysrc/db.py#L77)

```python
def remove(primary_key: int):
```

### ChainDB().remove_by_itr

[[find in source code]](https://github.com/uuosio/python-contracts-dev-kit/blob/master/pysrc/db.py#L86)

```python
def remove_by_itr(itr: int):
```

### ChainDB().store

[[find in source code]](https://github.com/uuosio/python-contracts-dev-kit/blob/master/pysrc/db.py#L69)

```python
def store(obj):
```

### ChainDB().upper_bound

[[find in source code]](https://github.com/uuosio/python-contracts-dev-kit/blob/master/pysrc/db.py#L54)

```python
def upper_bound(primary: int):
```

## ChainDBKey256

[[find in source code]](https://github.com/uuosio/python-contracts-dev-kit/blob/master/pysrc/db.py#L93)

```python
class ChainDBKey256(ChainDB):
    def __init__(code, scope, table, data_type):
```

#### See also

- [ChainDB](#chaindb)

## ChainDBKey64

[[find in source code]](https://github.com/uuosio/python-contracts-dev-kit/blob/master/pysrc/db.py#L89)

```python
class ChainDBKey64(ChainDB):
    def __init__(code, scope, table, data_type):
```

#### See also

- [ChainDB](#chaindb)

## MultiIndex

[[find in source code]](https://github.com/uuosio/python-contracts-dev-kit/blob/master/pysrc/db.py#L97)

```python
class MultiIndex():
    def __init__(code, scope, table, data_type):
```

### MultiIndex().find

[[find in source code]](https://github.com/uuosio/python-contracts-dev-kit/blob/master/pysrc/db.py#L110)

```python
def find(primary_key):
```

### MultiIndex().get

[[find in source code]](https://github.com/uuosio/python-contracts-dev-kit/blob/master/pysrc/db.py#L113)

```python
def get(itr):
```

### MultiIndex().get_secondary_index

[[find in source code]](https://github.com/uuosio/python-contracts-dev-kit/blob/master/pysrc/db.py#L205)

```python
def get_secondary_index(idx):
```

### MultiIndex().get_secondary_values

[[find in source code]](https://github.com/uuosio/python-contracts-dev-kit/blob/master/pysrc/db.py#L119)

```python
def get_secondary_values(primary_key):
```

### MultiIndex().idx_find

[[find in source code]](https://github.com/uuosio/python-contracts-dev-kit/blob/master/pysrc/db.py#L214)

```python
def idx_find(index, secondary_key):
```

### MultiIndex().idx_lower_bound

[[find in source code]](https://github.com/uuosio/python-contracts-dev-kit/blob/master/pysrc/db.py#L223)

```python
def idx_lower_bound(index, secondary_key):
```

### MultiIndex().idx_upper_bound

[[find in source code]](https://github.com/uuosio/python-contracts-dev-kit/blob/master/pysrc/db.py#L218)

```python
def idx_upper_bound(index, secondary_key):
```

### MultiIndex().load

[[find in source code]](https://github.com/uuosio/python-contracts-dev-kit/blob/master/pysrc/db.py#L141)

```python
def load(primary_key):
```

### MultiIndex().lower_bound

[[find in source code]](https://github.com/uuosio/python-contracts-dev-kit/blob/master/pysrc/db.py#L211)

```python
def lower_bound(primary):
```

### MultiIndex().remove

[[find in source code]](https://github.com/uuosio/python-contracts-dev-kit/blob/master/pysrc/db.py#L168)

```python
def remove(primary_key):
```

### MultiIndex().store

[[find in source code]](https://github.com/uuosio/python-contracts-dev-kit/blob/master/pysrc/db.py#L147)

```python
def store(obj):
```

### MultiIndex().upper_bound

[[find in source code]](https://github.com/uuosio/python-contracts-dev-kit/blob/master/pysrc/db.py#L208)

```python
def upper_bound(primary):
```
