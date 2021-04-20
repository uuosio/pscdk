# Chain

> Auto-generated documentation for [pysrc.chain](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py) module.

- [Python-contract-dev-kit](../README.md#python-contract-dev-kit) / [Modules](../MODULES.md#python-contract-dev-kit-modules) / [Pysrc](index.md#pysrc) / Chain
    - [name](#name)
    - [action_add_permission](#action_add_permission)
    - [action_free](#action_free)
    - [action_new](#action_new)
    - [action_send](#action_send)
    - [assert_recover_key](#assert_recover_key)
    - [assert_ripemd160](#assert_ripemd160)
    - [assert_sha1](#assert_sha1)
    - [assert_sha256](#assert_sha256)
    - [assert_sha512](#assert_sha512)
    - [call_contract](#call_contract)
    - [current_receiver](#current_receiver)
    - [current_time](#current_time)
    - [enable_log](#enable_log)
    - [expiration](#expiration)
    - [get_action](#get_action)
    - [get_active_producers](#get_active_producers)
    - [get_blockchain_parameters](#get_blockchain_parameters)
    - [get_code_hash](#get_code_hash)
    - [get_code_version](#get_code_version)
    - [get_context_free_data](#get_context_free_data)
    - [get_log](#get_log)
    - [get_resource_limits](#get_resource_limits)
    - [has_auth](#has_auth)
    - [is_account](#is_account)
    - [is_privileged](#is_privileged)
    - [kv_erase](#kv_erase)
    - [kv_get](#kv_get)
    - [kv_get_data](#kv_get_data)
    - [kv_it_compare](#kv_it_compare)
    - [kv_it_create](#kv_it_create)
    - [kv_it_destroy](#kv_it_destroy)
    - [kv_it_key](#kv_it_key)
    - [kv_it_key_compare](#kv_it_key_compare)
    - [kv_it_lower_bound](#kv_it_lower_bound)
    - [kv_it_move_to_end](#kv_it_move_to_end)
    - [kv_it_next](#kv_it_next)
    - [kv_it_prev](#kv_it_prev)
    - [kv_it_status](#kv_it_status)
    - [kv_it_value](#kv_it_value)
    - [kv_set](#kv_set)
    - [n2s](#n2s)
    - [publication_time](#publication_time)
    - [read_action_data](#read_action_data)
    - [read_transaction](#read_transaction)
    - [recover_key](#recover_key)
    - [require_auth](#require_auth)
    - [require_auth2](#require_auth2)
    - [require_recipient](#require_recipient)
    - [ripemd160](#ripemd160)
    - [s2b](#s2b)
    - [s2n](#s2n)
    - [send_context_free_inline](#send_context_free_inline)
    - [send_context_free_inline_raw](#send_context_free_inline_raw)
    - [send_inline](#send_inline)
    - [send_inline_raw](#send_inline_raw)
    - [set_action_return_value](#set_action_return_value)
    - [set_blockchain_parameters](#set_blockchain_parameters)
    - [set_kv_parameters_packed](#set_kv_parameters_packed)
    - [set_privileged](#set_privileged)
    - [set_proposed_producers](#set_proposed_producers)
    - [set_resource_limits](#set_resource_limits)
    - [sha1](#sha1)
    - [sha256](#sha256)
    - [sha512](#sha512)
    - [tapos_block_num](#tapos_block_num)
    - [tapos_block_prefix](#tapos_block_prefix)
    - [token_close](#token_close)
    - [token_create](#token_create)
    - [token_issue](#token_issue)
    - [token_open](#token_open)
    - [token_retire](#token_retire)
    - [token_transfer](#token_transfer)
    - [transaction_add_action](#transaction_add_action)
    - [transaction_add_context_free_action](#transaction_add_context_free_action)
    - [transaction_cancel](#transaction_cancel)
    - [transaction_free](#transaction_free)
    - [transaction_new](#transaction_new)
    - [transaction_send](#transaction_send)
    - [uuos_assert](#uuos_assert)
    - [uuos_assert_code](#uuos_assert_code)

## name

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L5)

```python
class name():
```

## action_add_permission

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L42)

```python
def action_add_permission(ptr: int, actor: Name, permission: Name):
```

Add a permission to action

#### Arguments

- `ptr` - int
- `actor` - Name
- `permission` - Name

#### See also

- [Name](#name)

## action_free

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L51)

```python
def action_free(ptr: int):
```

## action_new

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L25)

```python
def action_new(account: Name, act_name: Name, actor: Name, permission: name):
```

Create a new action

#### Arguments

- `account` - Name
- `act_name` - Name
- `actor` - Name
- `permission` - name

#### Returns

pointer to a action struct

#### See also

- [Name](#name)
- [name](#name)

## action_send

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L37)

```python
def action_send(ptr):
```

Send a action

## assert_recover_key

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L119)

```python
def assert_recover_key(digest: bytes, sig: bytes, pub_key: bytes):
```

Assertion for recover key

## assert_ripemd160

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L125)

```python
def assert_ripemd160(data: bytes, hash: bytes):
```

Assertion for ripemd160

#### Arguments

- `data` - data to hash
- `hash` - 20 bytes hash of ripemd160

## assert_sha1

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L135)

```python
def assert_sha1(data: bytes, hash: bytes):
```

Assertion for sha1

#### Arguments

- `data` - data to hash
- `hash` - 20 bytes hash of sha1

## assert_sha256

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L145)

```python
def assert_sha256(data: bytes, hash: bytes):
```

Assertion for sha256

#### Arguments

- `data` - data to hash
- `hash` - 32 bytes hash of sha256

## assert_sha512

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L155)

```python
def assert_sha512(data: bytes, hash: bytes):
```

Assertion for sha512

#### Arguments

- `data` - data to hash
- `hash` - 64 bytes hash of sha512

## call_contract

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L201)

```python
def call_contract(contract: Name, args: bytes):
```

call a function in contract

#### Arguments

- `contract` - Name,
- `args` - bytes

#### See also

- [Name](#name)

## current_receiver

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L211)

```python
def current_receiver() -> name:
```

Get current receiver of action

#### See also

- [name](#name)

## current_time

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L217)

```python
def current_time() -> int:
```

Get current block time in microseconds

## enable_log

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L223)

```python
def enable_log():
```

## expiration

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L105)

```python
def expiration():
```

Gets the expiration of the currently executing transaction in seconds.

## get_action

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L111)

```python
def get_action(_type: int, index: int) -> bytes:
```

Retrieves the indicated action from the active transaction.

#### Arguments

- `type` - int - 0 for context free action, 1 for action
- `index` - int - the index of the requested action

## get_active_producers

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L226)

```python
def get_active_producers():
```

## get_blockchain_parameters

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L229)

```python
def get_blockchain_parameters():
```

## get_code_hash

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L232)

```python
def get_code_hash():
```

## get_code_version

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L235)

```python
def get_code_version():
```

## get_context_free_data

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L238)

```python
def get_context_free_data():
```

## get_log

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L241)

```python
def get_log():
```

## get_resource_limits

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L244)

```python
def get_resource_limits():
```

## has_auth

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L247)

```python
def has_auth():
```

## is_account

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L250)

```python
def is_account():
```

## is_privileged

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L253)

```python
def is_privileged():
```

## kv_erase

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L256)

```python
def kv_erase():
```

## kv_get

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L259)

```python
def kv_get():
```

## kv_get_data

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L262)

```python
def kv_get_data():
```

## kv_it_compare

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L265)

```python
def kv_it_compare():
```

## kv_it_create

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L268)

```python
def kv_it_create():
```

## kv_it_destroy

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L271)

```python
def kv_it_destroy():
```

## kv_it_key

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L274)

```python
def kv_it_key():
```

## kv_it_key_compare

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L277)

```python
def kv_it_key_compare():
```

## kv_it_lower_bound

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L280)

```python
def kv_it_lower_bound():
```

## kv_it_move_to_end

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L283)

```python
def kv_it_move_to_end():
```

## kv_it_next

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L286)

```python
def kv_it_next():
```

## kv_it_prev

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L289)

```python
def kv_it_prev():
```

## kv_it_status

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L292)

```python
def kv_it_status():
```

## kv_it_value

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L295)

```python
def kv_it_value():
```

## kv_set

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L298)

```python
def kv_set():
```

## n2s

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L301)

```python
def n2s():
```

## publication_time

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L304)

```python
def publication_time():
```

## read_action_data

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L307)

```python
def read_action_data():
```

## read_transaction

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L310)

```python
def read_transaction():
```

## recover_key

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L313)

```python
def recover_key():
```

## require_auth

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L316)

```python
def require_auth():
```

## require_auth2

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L319)

```python
def require_auth2():
```

## require_recipient

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L322)

```python
def require_recipient():
```

## ripemd160

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L165)

```python
def ripemd160(data: Union[str, bytes]) -> bytes:
```

ripemd160 hash of data

#### Returns

20 bytes hash

## s2b

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L13)

```python
def s2b(s: Union[str, bytes]) -> bytes:
```

Convert a name in string to raw bytes

## s2n

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L19)

```python
def s2n(s: Union[str, bytes]):
```

Convert a name in string to a 64 bits integer

## send_context_free_inline

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L325)

```python
def send_context_free_inline():
```

## send_context_free_inline_raw

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L328)

```python
def send_context_free_inline_raw():
```

## send_inline

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L331)

```python
def send_inline():
```

## send_inline_raw

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L334)

```python
def send_inline_raw():
```

## set_action_return_value

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L337)

```python
def set_action_return_value():
```

## set_blockchain_parameters

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L340)

```python
def set_blockchain_parameters():
```

## set_kv_parameters_packed

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L343)

```python
def set_kv_parameters_packed():
```

## set_privileged

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L346)

```python
def set_privileged():
```

## set_proposed_producers

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L349)

```python
def set_proposed_producers():
```

## set_resource_limits

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L352)

```python
def set_resource_limits():
```

## sha1

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L174)

```python
def sha1(data: Union[str, bytes]) -> bytes:
```

hash of sha1

#### Returns

20 bytes of sha1 hash

## sha256

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L183)

```python
def sha256(data: Union[str, bytes]) -> bytes:
```

hash of sha256

#### Returns

32 bytes of sha256 hash

## sha512

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L192)

```python
def sha512(data: Union[str, bytes]):
```

hash of sha512

#### Returns

64 bytes of sha512 hash

## tapos_block_num

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L355)

```python
def tapos_block_num():
```

## tapos_block_prefix

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L358)

```python
def tapos_block_prefix():
```

## token_close

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L361)

```python
def token_close():
```

## token_create

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L364)

```python
def token_create():
```

## token_issue

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L367)

```python
def token_issue():
```

## token_open

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L370)

```python
def token_open():
```

## token_retire

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L373)

```python
def token_retire():
```

## token_transfer

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L376)

```python
def token_transfer():
```

## transaction_add_action

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L75)

```python
def transaction_add_action(ptr: int, act_ptr: int):
```

Add an action to transaction

## transaction_add_context_free_action

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L81)

```python
def transaction_add_context_free_action(ptr: int, act_ptr: int):
```

Add an context free action to transaction

## transaction_cancel

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L93)

```python
def transaction_cancel(sender_id: Uint128) -> bool:
```

Cancel a transaction

#### See also

- [Uint128](#uint128)

## transaction_free

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L99)

```python
def transaction_free(ptr: int):
```

Release the memory of transaction

## transaction_new

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L54)

```python
def transaction_new(
    expiration: Uint32,
    ref_block_num: Uint32,
    ref_block_prefix: Uint32,
    max_net_usage_words: Uint32,
    max_cpu_usage_ms: Uint32,
    delay_sec: Uint32,
) -> int:
```

Create a new transaction

#### Arguments

- `expiration` - Uint32,
- `ref_block_num` - Uint32,
- `ref_block_prefix` - Uint32,
- `max_net_usage_words` - Uint32,
- `max_cpu_usage_ms` - Uint32,
- `delay_sec` - Uint32

#### Returns

- `int` - pointer to a C transaction struct

#### See also

- [Uint32](#uint32)

## transaction_send

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L87)

```python
def transaction_send(
    trx_ptr: Uint64,
    sender_id: Uint128,
    payer: Name,
    replace_existing: bool,
):
```

Send a transaction

#### See also

- [Name](#name)
- [Uint128](#uint128)
- [Uint64](#uint64)

## uuos_assert

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L379)

```python
def uuos_assert():
```

## uuos_assert_code

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L382)

```python
def uuos_assert_code():
```
