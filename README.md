# Python Smart Contracts Development Kit

### [Documentation](https://uuosio.github.io/uuosio.pscdk)

### Quick Start
```python
import os
from uuoskit import uuosapi, wallet, config
from uuoskit.exceptions import ChainException

if os.path.exists('mywallet.wallet'):
    os.remove('mywallet.wallet')
psw = wallet.create('mywallet')

wallet.import_key('mywallet', '5Jbb4wuwz8MAzTB9FJNmrVYGXo4ABb7wqPVoWGcZ6x8V2FwNeDo')

uuosapi.set_node('https://testnode.uuos.network:8443')
code = '''
import chain
def apply(a, b, c):
    data = chain.read_action_data()
    print('++++action data:', data)
'''

account = 'helloworld11'
config.python_contract = account
code = uuosapi.mp_compile(account, code)

uuosapi.deploy_python_contract(account, code, b'')

r = uuosapi.push_action(account, 'sayhello', b'hellooo,world', {account:'active'})
console = r['processed']['action_traces'][0]['console']
print(console)

r = uuosapi.push_action(account, 'sayhello', b'goodbye,world', {account:'active'})
console = r['processed']['action_traces'][0]['console']
print(console)
```

### Python Smart Contracts Example

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
        return struct.pack('llld', self.a, self.b, self.c, self.d)

    @classmethod
    def unpack(cls, data):
        data = struct.unpack('llld', data)
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

### License
[MIT](./LICENSE)
