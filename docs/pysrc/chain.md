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

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L45)

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

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L55)

```python
def action_free(ptr: int):
```

## action_new

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L28)

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

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L40)

```python
def action_send(ptr):
```

Send a action

## assert_recover_key

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L124)

```python
def assert_recover_key(digest: bytes, sig: bytes, pub_key: bytes):
```

Assertion for recover key

## assert_ripemd160

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L129)

```python
def assert_ripemd160(data: bytes, hash: bytes):
```

Assertion for ripemd160

#### Arguments

- `data` - data to hash
- `hash` - 20 bytes hash of ripemd160

## assert_sha1

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L138)

```python
def assert_sha1(data: bytes, hash: bytes):
```

Assertion for sha1

#### Arguments

- `data` - data to hash
- `hash` - 20 bytes hash of sha1

## assert_sha256

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L147)

```python
def assert_sha256(data: bytes, hash: bytes):
```

Assertion for sha256

#### Arguments

- `data` - data to hash
- `hash` - 32 bytes hash of sha256

## assert_sha512

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L156)

```python
def assert_sha512(data: bytes, hash: bytes):
```

Assertion for sha512

#### Arguments

- `data` - data to hash
- `hash` - 64 bytes hash of sha512

## call_contract

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L197)

```python
def call_contract(contract: Name, args: bytes):
```

Call a function in contract

#### Arguments

- `contract` - Name,
- `args` - bytes

#### See also

- [Name](#name)

## current_receiver

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L206)

```python
def current_receiver() -> name:
```

Get current receiver of action

#### See also

- [name](#name)

## current_time

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L211)

```python
def current_time() -> int:
```

Get current block time in microseconds

## enable_log

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L216)

```python
def enable_log():
```

Enable logging via print

## expiration

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L103)

```python
def expiration():
```

Gets the expiration of the currently executing transaction in seconds.

## get_action

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L108)

```python
def get_action(_type: int, index: int) -> bytes:
```

Retrieves the indicated action from the active transaction.

#### Arguments

- `type` - int - 0 for context free action, 1 for action
- `index` - int - the index of the requested action

## get_active_producers

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L224)

```python
def get_active_producers() -> Tuple[str]:
```

Gets the set of active producers.

## get_blockchain_parameters

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L229)

```python
def get_blockchain_parameters():
```

Retrieve the blolckchain parameters

## get_code_hash

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L234)

```python
def get_code_hash(contract: Name):
```

Get code hash of a contract

#### See also

- [Name](#name)

## get_code_version

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L239)

```python
def get_code_version(contract: Name):
```

Get code version of a contract

#### See also

- [Name](#name)

## get_context_free_data

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L117)

```python
def get_context_free_data(index: int):
```

Retrieve the signed_transaction.context_free_data[index].

#### Arguments

- `index` - int - the index of the context_free_data entry to retrieve

## get_log

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L221)

```python
def get_log():
```

## get_resource_limits

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L244)

```python
def get_resource_limits(account: Name):
```

Get the resource limits of an account

#### Returns

(ram_bytes, net_weight, cpu_weight)

#### See also

- [Name](#name)

## has_auth

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L252)

```python
def has_auth(account: Name):
```

Verifies that account name has auth.

#### See also

- [Name](#name)

## is_account

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L257)

```python
def is_account(account: Name):
```

Check if an account is exists.

#### Returns

True for account exists, False for account not exists.

#### See also

- [Name](#name)

## is_privileged

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L264)

```python
def is_privileged(account: Name):
```

Check if an account is privileged

#### See also

- [Name](#name)

## n2s

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L13)

```python
def n2s(n: int) -> str:
```

Convert a integer to string

## publication_time

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L269)

```python
def publication_time():
```

Retrive the publication time

## read_action_data

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L274)

```python
def read_action_data() -> bytes:
```

Retrive data in an action

#### Returns

- `bytes` - raw data in an action

## read_transaction

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L282)

```python
def read_transaction():
```

Read raw transaction

## recover_key

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L287)

```python
def recover_key(digest: bytes, sig: bytes):
```

Calculates the public key used for a given signature and hash used to create a message.

#### Arguments

digest (bytes) : 32 bytes hash of sha256
- `sig` *bytes* - raw signature

## require_auth

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L295)

```python
def require_auth(account: Name):
```

Verifies that account exists in the set of provided auths on a action. Throws if not found.

#### See also

- [Name](#name)

## require_auth2

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L300)

```python
def require_auth2(account: Name, permission: Name):
```

Verifies that account name exists in the set of provided auths on a action. Throws if not found.

#### See also

- [Name](#name)

## require_recipient

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L305)

```python
def require_recipient(contract: Name):
```

Send notify to contract

#### See also

- [Name](#name)

## ripemd160

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L165)

```python
def ripemd160(data: Union[str, bytes]) -> bytes:
```

ripemd160 hash of data

#### Returns

20 bytes hash

## s2b

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L18)

```python
def s2b(s: Union[str, bytes]) -> bytes:
```

Convert a name in string to raw bytes

## s2n

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L23)

```python
def s2n(s: Union[str, bytes]):
```

Convert a name in string to a 64 bits integer

## send_context_free_inline

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L310)

```python
def send_context_free_inline(account: Name, action: Name, data: bytes):
```

send inline context free action

#### See also

- [Name](#name)

## send_context_free_inline_raw

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L315)

```python
def send_context_free_inline_raw(data):
```

Send raw context free inline action

## send_inline

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L320)

```python
def send_inline(
    account: Name,
    action: Name,
    actor: Name,
    permission: Name,
    data: bytes,
):
```

Send inline action

#### See also

- [Name](#name)

## send_inline_raw

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L325)

```python
def send_inline_raw(data):
```

send raw inline action

## set_action_return_value

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L330)

```python
def set_action_return_value(data):
```

set return value of action

## set_blockchain_parameters

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L335)

```python
def set_blockchain_parameters(parameters: Tuple[int]):
```

struct blockchain_parameters {
    uint64_t max_block_net_usage;
    uint32_t target_block_net_usage_pct;
    uint32_t max_transaction_net_usage;
    uint32_t base_per_transaction_net_usage;
    uint32_t net_usage_leeway;
    uint32_t context_free_discount_net_usage_num;
    uint32_t context_free_discount_net_usage_den;
    uint32_t max_block_cpu_usage;
    uint32_t target_block_cpu_usage_pct;
    uint32_t max_transaction_cpu_usage;
    uint32_t min_transaction_cpu_usage;
    uint64_t context_free_discount_cpu_usage_num;
    uint64_t context_free_discount_cpu_usage_den;
    uint32_t max_transaction_lifetime;
    uint32_t deferred_trx_expiration_window;
    uint32_t max_transaction_delay;
    uint32_t max_inline_action_size;
    uint16_t max_inline_action_depth;
    uint16_t max_authority_depth;
};

## set_kv_parameters_packed

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L361)

```python
def set_kv_parameters_packed():
```

## set_privileged

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L364)

```python
def set_privileged(account: Name, is_priv: bool):
```

Set the privileged status of an account

#### See also

- [Name](#name)

## set_proposed_producers

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L369)

```python
def set_proposed_producers(producers: List[Name]):
```

Proposes a schedule change, once the block that contains the proposal becomes irreversible, the schedule is promoted to "pending" automatically. Once the block that promotes the schedule is irreversible, the schedule will become "active"

## set_resource_limits

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L374)

```python
def set_resource_limits(
    account: Name,
    ram_bytes: int,
    net_weight: int,
    cpu_weight: int,
):
```

Set the resource limits of an account

#### See also

- [Name](#name)

## sha1

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L173)

```python
def sha1(data: Union[str, bytes]) -> bytes:
```

Hash of sha1

#### Returns

20 bytes of sha1 hash

## sha256

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L181)

```python
def sha256(data: Union[str, bytes]) -> bytes:
```

Hash of sha256

#### Returns

32 bytes of sha256 hash

## sha512

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L189)

```python
def sha512(data: Union[str, bytes]):
```

Hash of sha512

#### Returns

64 bytes of sha512 hash

## tapos_block_num

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L379)

```python
def tapos_block_num() -> int:
```

Gets the block number used for TAPOS on the currently executing transaction.

## tapos_block_prefix

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L384)

```python
def tapos_block_prefix() -> int:
```

Gets the block prefix used for TAPOS on the currently executing transaction.

## token_close

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L425)

```python
def token_close(owner: Name, symbol: int):
```

Close a token

#### See also

- [Name](#name)

## token_create

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L399)

```python
def token_create(issuer: Name, maximum_supply: int, sym: int):
```

Create a token

#### See also

- [Name](#name)

## token_issue

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L404)

```python
def token_issue(to: Name, quantity: int, sym: int, memo: str):
```

Issue aa token

#### See also

- [Name](#name)

## token_open

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L414)

```python
def token_open(owner: Name, symbol: int, ram_payer: Name):
```

Open a token

#### See also

- [Name](#name)

## token_retire

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L419)

```python
def token_retire(amount: int, symbol: int, memo: str):
```

Retire a token

## token_transfer

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L409)

```python
def token_transfer(_from: Name, to: Name, quantity: int, sym: int, memo: str):
```

Transfer a token

#### See also

- [Name](#name)

## transaction_add_action

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L78)

```python
def transaction_add_action(ptr: int, act_ptr: int):
```

Add an action to transaction

## transaction_add_context_free_action

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L83)

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

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L98)

```python
def transaction_free(ptr: int):
```

Release the memory of transaction

## transaction_new

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L58)

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

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L88)

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

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L389)

```python
def uuos_assert(test: bool, msg: str):
```

raise exception if test is false

## uuos_assert_code

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L394)

```python
def uuos_assert_code(test: bool, code: int):
```

raise exception with code if test is false
