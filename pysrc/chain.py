#dummy module for buildin chain module
from typing import Union

# buildin name object
class name:
    pass

Name = Union[str, int, name]
Uint32 = int
Uint128 = int
Uint64 = int

def s2b(s: Union[str, bytes]) -> bytes:
    '''
    Convert a name in string to raw bytes
    '''
    pass

def s2n(s: Union[str, bytes]):
    '''
    Convert a name in string to a 64 bits integer
    '''
    pass

def action_new(account: Name, act_name: Name, actor: Name, permission: name):
    ''' Create a new action
    Args:
        account: Name
        act_name: Name
        actor: Name
        permission: name
    Returns:
        pointer to a action struct 
    '''
    pass

def action_send(ptr):
    '''Send a action
    '''
    pass

def action_add_permission(ptr: int, actor: Name, permission: Name):
    '''Add a permission to action
    Args:
        ptr: int
        actor: Name
        permission: Name
    '''
    pass

def action_free(ptr: int):
    pass

def transaction_new(expiration: Uint32,
                    ref_block_num: Uint32,
                    ref_block_prefix: Uint32,
                    max_net_usage_words: Uint32,
                    max_cpu_usage_ms: Uint32,
                    delay_sec: Uint32) -> int:
    '''
    Create a new transaction

    Args:
        expiration: Uint32,
        ref_block_num: Uint32,
        ref_block_prefix: Uint32,
        max_net_usage_words: Uint32,
        max_cpu_usage_ms: Uint32,
        delay_sec: Uint32

    Returns:
        int: pointer to a C transaction struct 
    '''

def transaction_add_action(ptr: int, act_ptr: int):
    '''
    Add an action to transaction
    '''
    pass

def transaction_add_context_free_action(ptr: int, act_ptr: int):
    '''
    Add an context free action to transaction
    '''
    pass

def transaction_send(trx_ptr: Uint64, sender_id: Uint128, payer: Name, replace_existing: bool):
    '''
    Send a transaction
    '''
    pass

def transaction_cancel(sender_id: Uint128) -> bool:
    '''
    Cancel a transaction
    '''
    pass

def transaction_free(ptr: int):
    '''
    Release the memory of transaction
    '''
    pass

def assert_recover_key(digest: bytes, sig: bytes, pub_key: bytes):
    '''
    Assertion for recover key
    '''
    pass

def assert_ripemd160(data: bytes, hash: bytes):
    '''
    Assertion for ripemd160
    
    Args:
        data: data to hash
        hash: 20 bytes hash of ripemd160 
    '''
    pass

def assert_sha1(data: bytes, hash: bytes):
    '''
    Assertion for sha1
    
    Args:
        data: data to hash
        hash: 20 bytes hash of sha1 
    '''
    pass

def assert_sha256(data: bytes, hash: bytes):
    '''
    Assertion for sha256
    
    Args:
        data: data to hash
        hash: 32 bytes hash of sha256
    '''
    pass

def assert_sha512(data: bytes, hash: bytes):
    '''
    Assertion for sha512
    
    Args:
        data: data to hash
        hash: 64 bytes hash of sha512
    '''
    pass

def ripemd160(data: Union[str, bytes]) -> bytes:
    '''
    ripemd160 hash of data

    Returns:
        20 bytes hash
    '''
    pass

def sha1(data: Union[str, bytes]) -> bytes:
    '''
    hash of sha1

    Returns:
        20 bytes of sha1 hash
    '''
    pass

def sha256(data: Union[str, bytes]) -> bytes:
    '''
    hash of sha256

    Returns:
        32 bytes of sha256 hash
    '''
    pass

def sha512(data: Union[str, bytes]):
    '''
    hash of sha512

    Returns:
        64 bytes of sha512 hash
    '''
    pass

def call_contract():
    pass

def current_receiver():
    pass

def current_time():
    pass

def db_end_i256():
    pass

def db_end_i64():
    pass

def db_find_i256():
    pass

def db_find_i64():
    pass

def db_get_i256():
    pass

def db_get_i64():
    pass

def db_get_table_row_count():
    pass

def db_idx_end():
    pass

def db_idx_find_primary():
    pass

def db_idx_find_secondary():
    pass

def db_idx_lowerbound():
    pass

def db_idx_next():
    pass

def db_idx_previous():
    pass

def db_idx_remove():
    pass

def db_idx_store():
    pass

def db_idx_update():
    pass

def db_idx_upperbound():
    pass

def db_lowerbound_i256():
    pass

def db_lowerbound_i64():
    pass

def db_next_i256():
    pass

def db_next_i64():
    pass

def db_previous_i256():
    pass

def db_previous_i64():
    pass

def db_remove_i256():
    pass

def db_remove_i64():
    pass

def db_store_i256():
    pass

def db_store_i64():
    pass

def db_update_i256():
    pass

def db_update_i64():
    pass

def db_upperbound_i256():
    pass

def db_upperbound_i64():
    pass

def enable_log():
    pass

def expiration():
    pass

def get_action():
    pass

def get_active_producers():
    pass

def get_blockchain_parameters():
    pass

def get_code_hash():
    pass

def get_code_version():
    pass

def get_context_free_data():
    pass

def get_log():
    pass

def get_resource_limits():
    pass

def has_auth():
    pass

def is_account():
    pass

def is_privileged():
    pass

def kv_erase():
    pass

def kv_get():
    pass

def kv_get_data():
    pass

def kv_it_compare():
    pass

def kv_it_create():
    pass

def kv_it_destroy():
    pass

def kv_it_key():
    pass

def kv_it_key_compare():
    pass

def kv_it_lower_bound():
    pass

def kv_it_move_to_end():
    pass

def kv_it_next():
    pass

def kv_it_prev():
    pass

def kv_it_status():
    pass

def kv_it_value():
    pass

def kv_set():
    pass

def n2s():
    pass

def publication_time():
    pass

def read_action_data():
    pass

def read_transaction():
    pass

def recover_key():
    pass

def require_auth():
    pass

def require_auth2():
    pass

def require_recipient():
    pass

def send_context_free_inline():
    pass

def send_context_free_inline_raw():
    pass

def send_inline():
    pass

def send_inline_raw():
    pass

def set_action_return_value():
    pass

def set_blockchain_parameters():
    pass

def set_kv_parameters_packed():
    pass

def set_privileged():
    pass

def set_proposed_producers():
    pass

def set_resource_limits():
    pass

def tapos_block_num():
    pass

def tapos_block_prefix():
    pass

def token_close():
    pass

def token_create():
    pass

def token_issue():
    pass

def token_open():
    pass

def token_retire():
    pass

def token_transfer():
    pass

def uuos_assert():
    pass

def uuos_assert_code():
    pass
