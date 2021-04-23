# Helloworld

```python
def apply(receiver, first_receiver, action):
    print('hello,world')
```

# Name Object

```python
import chain
def apply(receiver, first_receiver, action):
    print(type(receiver), type(first_receiver), type(action))

    print(receiver, first_receiver, action)
    print(int(receiver), int(first_receiver), int(action))
    print(str(receiver), str(first_receiver), str(action))

    print(name('hello'), name('sayhello'))
    
    print(chain.s2n('hello'), chain.n2s(7684013976526520320), type(chain.n2s(7684013976526520320)))
```

# Float128

```python
def apply(a, b, c):
    a = float128('3.14') * 5.1
    print(type(a), a)

    a = 5.1 * float128('3.14')
    print(type(a), a)

    a = float128(3.14) * float128(5.1)
    print(type(a), a)

    raw_bytes = bytes(float128(3.14))
    print(raw_bytes)
    print(float128(raw_bytes))
```

# BytesIO

```python
def apply(a, b, c):
    a = float128('3.14') * 5.1
    print(type(a), a)

    a = 5.1 * float128('3.14')
    print(type(a), a)

    a = float128(3.14) * float128(5.1)
    print(type(a), a)

    raw_bytes = bytes(float128(3.14))
    print(raw_bytes)
    print(float128(raw_bytes))
```

# Math Module

```python
# https://docs.micropython.org/en/latest/library/math.html
def apply(receiver, first_receiver, action):
    import math
    print(math.pow(5, 2) == 25.0)
    print(math.ceil(1.1) == 2)
    print(math.log2(8) == 3.0)
    print(math.sqrt(4) == 2.0)
    print(math.pi)
    print(dir(math))
```

# Import Custom Module
```python
from helloworld11 import hello
from helloworld11.hello import say_hello

def apply(receiver, first_receiver, action):
    hello.say_hello()
    say_hello()

# contract deploy to helloworld11
def say_hello():
    print('hello world from sub module')

```

# Assestion APIs
```python
import chain
def apply(receiver, first_receiver, action):
    if action == name('test1'):
        chain.uuos_assert(receiver == first_receiver, 'oops, not work in notify')
        chain.uuos_assert_code(receiver == first_receiver, 123)
    elif action == name('test2'):
        assert False, 'exception raised'
    else:
        chain.uuos_assert(False, 'bad action')
```

# Authorization APIs
```python
import chain
def apply(receiver, first_receiver, action):
    print(receiver, first_receiver)
    if action == name('test1'):
        print(chain.has_auth('hello'))
        print(chain.has_auth(receiver))
        chain.require_auth(receiver)
        chain.require_auth2(receiver, 'active')
    elif action == name('test2'):
        print('hello')
        # not good, transaction does not have owner authorization,
        # will throw an exception, should be caught by test code
        chain.require_auth2(receiver, 'owner')
```

# Inline Action
```python
import chain
def apply(receiver, first_receiver, action):
    if action == name('testinline'):
        account = receiver
        action = name('sayhello')
        actor = receiver
        permission = name('active')
        data = b'hello,world'
        chain.send_inline(account, action, actor, permission, data)
        print('inline action sent')
    elif action == name('sayhello'):
        data = chain.read_action_data()
        print(data)
```

# Notification
```python
#send notify
import chain
def apply(receiver, first_receiver, action):
    data = chain.read_action_data()
    notify_to = data[8:16]
    notify_to = name(notify_to)
    print('send notify:', notify_to)
    assert chain.is_account(notify_to), 'notify to account does not exists!'
    chain.require_recipient(notify_to)
```

# Block Info APIs
```python
import chain
import time
def apply(receiver, first_receiver, action):
    print(time.time())
    print(chain.current_time())
    print(chain.is_account(receiver), chain.is_account('none'))
    print(chain.tapos_block_num())
    print(chain.tapos_block_prefix())
    print(chain.expiration())
    
    print(chain.read_transaction())

#    _type - 0 for context free action, 1 for action
#    index - the index of the requested action
#    get_action(_type, index)

    print(chain.get_action(1, 0))
    print(chain.get_action(0, 0))
```

# Hash APIs

```python
import chain
def apply(receiver, first_receiver, action):
    data = 'hello,world'
    h = chain.sha256(data)
    print('hash256:', h)
    chain.assert_sha256(data, h)

    h = chain.sha1(data)
    print('sha1:', h)
    chain.assert_sha1(data, h)

    h = chain.sha512(data)
    print('sha512', h)
    chain.assert_sha512(data, h)

    h = chain.ripemd160(data)
    print('ripemd160:', h)
    chain.assert_ripemd160(data, h)
    print('all tests passed!')
```

# Recover Public Key from Signature
```python
import chain
def apply(receiver, first_receiver, action):
    signature = chain.read_action_data()[8:]
    digest = chain.sha256('hello,world')
    pub_key = chain.recover_key(digest, signature)
    print(pub_key)
    # raw public key, no checksum, 34 bytes
    assert pub_key == b'\x00\x02\xa8\x91\xe0\xddW\x13.\xd6\x83\xbc\x87]\xac\xc9a\xc6\xfd]\xfa\xe6\x80\x0b\xc6\x18\x1a\xb6\x8b\xb8H%\x1eR'
    chain.assert_recover_key(digest, signature, pub_key)
```

# Storage
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






