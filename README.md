# Python Smart Contract Development Kit

# [Documentation](https://uuosio.github.io/uuosio.pscdk)

# Python Smart Contracts Example

```python
import json
import struct
import chain
import db

class MyDataI64(object):
    def __init__(self, a: int, b: int, c: int, d: float):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.payer = 0

    def pack(self):
        return struct.pack('lllf', self.a, self.b, self.c, self.d)

    @classmethod
    def unpack(cls, data):
        data = struct.unpack('lllf', data)
        return cls(data[0], data[1], data[2], data[3])

    def get_primary_key(self):
        return self.a

    def __str__(self):
        data = (self.a, self.b, self.c, self.d)
        return json.dumps(data)

def apply(receiver, first_receiver, action):
    code = receiver
    scope = name('scope')
    table = name('table3')
    payer = receiver

    storage = db.ChainDBKey64(code, scope, table, MyDataI64)
    d = MyDataI64(1, 2, 3, 5.0)
    d.payer = payer
    storage.store(d)
    
    primary_key = 1
    data = storage.load(primary_key)
    print(data)

    primary_key = 2
    data = storage.load(primary_key)
    print(data)
```