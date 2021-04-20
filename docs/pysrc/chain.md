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
    - [db_end_i256](#db_end_i256)
    - [db_end_i64](#db_end_i64)
    - [db_find_i256](#db_find_i256)
    - [db_find_i64](#db_find_i64)
    - [db_get_i256](#db_get_i256)
    - [db_get_i64](#db_get_i64)
    - [db_get_table_row_count](#db_get_table_row_count)
    - [db_idx_end](#db_idx_end)
    - [db_idx_find_primary](#db_idx_find_primary)
    - [db_idx_find_secondary](#db_idx_find_secondary)
    - [db_idx_lowerbound](#db_idx_lowerbound)
    - [db_idx_next](#db_idx_next)
    - [db_idx_previous](#db_idx_previous)
    - [db_idx_remove](#db_idx_remove)
    - [db_idx_store](#db_idx_store)
    - [db_idx_update](#db_idx_update)
    - [db_idx_upperbound](#db_idx_upperbound)
    - [db_lowerbound_i256](#db_lowerbound_i256)
    - [db_lowerbound_i64](#db_lowerbound_i64)
    - [db_next_i256](#db_next_i256)
    - [db_next_i64](#db_next_i64)
    - [db_previous_i256](#db_previous_i256)
    - [db_previous_i64](#db_previous_i64)
    - [db_remove_i256](#db_remove_i256)
    - [db_remove_i64](#db_remove_i64)
    - [db_store_i256](#db_store_i256)
    - [db_store_i64](#db_store_i64)
    - [db_update_i256](#db_update_i256)
    - [db_update_i64](#db_update_i64)
    - [db_upperbound_i256](#db_upperbound_i256)
    - [db_upperbound_i64](#db_upperbound_i64)
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

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L28)

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

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L37)

```python
def action_free():
```

## action_new

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L10)

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

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L22)

```python
def action_send(ptr, actor, permission):
```

Send a action

## assert_recover_key

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L40)

```python
def assert_recover_key():
```

## assert_ripemd160

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L43)

```python
def assert_ripemd160():
```

## assert_sha1

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L46)

```python
def assert_sha1():
```

## assert_sha256

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L49)

```python
def assert_sha256():
```

## assert_sha512

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L52)

```python
def assert_sha512():
```

## call_contract

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L55)

```python
def call_contract():
```

## current_receiver

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L58)

```python
def current_receiver():
```

## current_time

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L61)

```python
def current_time():
```

## db_end_i256

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L64)

```python
def db_end_i256():
```

## db_end_i64

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L67)

```python
def db_end_i64():
```

## db_find_i256

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L70)

```python
def db_find_i256():
```

## db_find_i64

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L73)

```python
def db_find_i64():
```

## db_get_i256

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L76)

```python
def db_get_i256():
```

## db_get_i64

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L79)

```python
def db_get_i64():
```

## db_get_table_row_count

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L82)

```python
def db_get_table_row_count():
```

## db_idx_end

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L85)

```python
def db_idx_end():
```

## db_idx_find_primary

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L88)

```python
def db_idx_find_primary():
```

## db_idx_find_secondary

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L91)

```python
def db_idx_find_secondary():
```

## db_idx_lowerbound

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L94)

```python
def db_idx_lowerbound():
```

## db_idx_next

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L97)

```python
def db_idx_next():
```

## db_idx_previous

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L100)

```python
def db_idx_previous():
```

## db_idx_remove

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L103)

```python
def db_idx_remove():
```

## db_idx_store

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L106)

```python
def db_idx_store():
```

## db_idx_update

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L109)

```python
def db_idx_update():
```

## db_idx_upperbound

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L112)

```python
def db_idx_upperbound():
```

## db_lowerbound_i256

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L115)

```python
def db_lowerbound_i256():
```

## db_lowerbound_i64

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L118)

```python
def db_lowerbound_i64():
```

## db_next_i256

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L121)

```python
def db_next_i256():
```

## db_next_i64

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L124)

```python
def db_next_i64():
```

## db_previous_i256

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L127)

```python
def db_previous_i256():
```

## db_previous_i64

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L130)

```python
def db_previous_i64():
```

## db_remove_i256

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L133)

```python
def db_remove_i256():
```

## db_remove_i64

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L136)

```python
def db_remove_i64():
```

## db_store_i256

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L139)

```python
def db_store_i256():
```

## db_store_i64

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L142)

```python
def db_store_i64():
```

## db_update_i256

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L145)

```python
def db_update_i256():
```

## db_update_i64

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L148)

```python
def db_update_i64():
```

## db_upperbound_i256

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L151)

```python
def db_upperbound_i256():
```

## db_upperbound_i64

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L154)

```python
def db_upperbound_i64():
```

## enable_log

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L157)

```python
def enable_log():
```

## expiration

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L160)

```python
def expiration():
```

## get_action

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L163)

```python
def get_action():
```

## get_active_producers

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L166)

```python
def get_active_producers():
```

## get_blockchain_parameters

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L169)

```python
def get_blockchain_parameters():
```

## get_code_hash

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L172)

```python
def get_code_hash():
```

## get_code_version

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L175)

```python
def get_code_version():
```

## get_context_free_data

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L178)

```python
def get_context_free_data():
```

## get_log

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L181)

```python
def get_log():
```

## get_resource_limits

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L184)

```python
def get_resource_limits():
```

## has_auth

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L187)

```python
def has_auth():
```

## is_account

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L190)

```python
def is_account():
```

## is_privileged

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L193)

```python
def is_privileged():
```

## kv_erase

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L196)

```python
def kv_erase():
```

## kv_get

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L199)

```python
def kv_get():
```

## kv_get_data

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L202)

```python
def kv_get_data():
```

## kv_it_compare

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L205)

```python
def kv_it_compare():
```

## kv_it_create

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L208)

```python
def kv_it_create():
```

## kv_it_destroy

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L211)

```python
def kv_it_destroy():
```

## kv_it_key

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L214)

```python
def kv_it_key():
```

## kv_it_key_compare

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L217)

```python
def kv_it_key_compare():
```

## kv_it_lower_bound

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L220)

```python
def kv_it_lower_bound():
```

## kv_it_move_to_end

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L223)

```python
def kv_it_move_to_end():
```

## kv_it_next

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L226)

```python
def kv_it_next():
```

## kv_it_prev

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L229)

```python
def kv_it_prev():
```

## kv_it_status

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L232)

```python
def kv_it_status():
```

## kv_it_value

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L235)

```python
def kv_it_value():
```

## kv_set

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L238)

```python
def kv_set():
```

## n2s

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L241)

```python
def n2s():
```

## publication_time

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L244)

```python
def publication_time():
```

## read_action_data

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L247)

```python
def read_action_data():
```

## read_transaction

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L250)

```python
def read_transaction():
```

## recover_key

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L253)

```python
def recover_key():
```

## require_auth

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L256)

```python
def require_auth():
```

## require_auth2

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L259)

```python
def require_auth2():
```

## require_recipient

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L262)

```python
def require_recipient():
```

## ripemd160

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L265)

```python
def ripemd160():
```

## s2b

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L268)

```python
def s2b():
```

## s2n

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L271)

```python
def s2n():
```

## send_context_free_inline

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L274)

```python
def send_context_free_inline():
```

## send_context_free_inline_raw

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L277)

```python
def send_context_free_inline_raw():
```

## send_inline

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L280)

```python
def send_inline():
```

## send_inline_raw

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L283)

```python
def send_inline_raw():
```

## set_action_return_value

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L286)

```python
def set_action_return_value():
```

## set_blockchain_parameters

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L289)

```python
def set_blockchain_parameters():
```

## set_kv_parameters_packed

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L292)

```python
def set_kv_parameters_packed():
```

## set_privileged

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L295)

```python
def set_privileged():
```

## set_proposed_producers

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L298)

```python
def set_proposed_producers():
```

## set_resource_limits

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L301)

```python
def set_resource_limits():
```

## sha1

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L304)

```python
def sha1():
```

## sha256

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L307)

```python
def sha256():
```

## sha512

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L310)

```python
def sha512():
```

## tapos_block_num

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L313)

```python
def tapos_block_num():
```

## tapos_block_prefix

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L316)

```python
def tapos_block_prefix():
```

## token_close

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L319)

```python
def token_close():
```

## token_create

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L322)

```python
def token_create():
```

## token_issue

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L325)

```python
def token_issue():
```

## token_open

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L328)

```python
def token_open():
```

## token_retire

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L331)

```python
def token_retire():
```

## token_transfer

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L334)

```python
def token_transfer():
```

## transaction_add_action

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L337)

```python
def transaction_add_action():
```

## transaction_add_context_free_action

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L340)

```python
def transaction_add_context_free_action():
```

## transaction_cancel

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L343)

```python
def transaction_cancel():
```

## transaction_free

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L346)

```python
def transaction_free():
```

## transaction_new

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L349)

```python
def transaction_new():
```

## transaction_send

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L352)

```python
def transaction_send():
```

## uuos_assert

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L355)

```python
def uuos_assert():
```

## uuos_assert_code

[[find in source code]](https://github.com/uuosio/python-contract-dev-kit/blob/master/pysrc/chain.py#L358)

```python
def uuos_assert_code():
```
