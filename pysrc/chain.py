#dummy module for buildin chain module
from typing import Union, List, Tuple

# buildin name object
class name:
    pass

Name = Union[str, int, name]
Uint32 = int
Uint128 = int
Uint64 = int

def n2s(n: int) -> str:
    '''Convert a integer to string
    '''
    pass

def s2b(s: Union[str, bytes]) -> bytes:
    '''Convert a name in string to raw bytes
    '''
    pass

def s2n(s: Union[str, bytes]):
    '''Convert a name in string to a 64 bits integer
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
    '''Create a new transaction

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
    '''Add an action to transaction
    '''
    pass

def transaction_add_context_free_action(ptr: int, act_ptr: int):
    '''Add an context free action to transaction
    '''
    pass

def transaction_send(trx_ptr: Uint64, sender_id: Uint128, payer: Name, replace_existing: bool):
    '''Send a transaction
    '''
    pass

def transaction_cancel(sender_id: Uint128) -> bool:
    '''Cancel a transaction
    '''
    pass

def transaction_free(ptr: int):
    '''Release the memory of transaction
    '''
    pass

def expiration():
    '''Gets the expiration of the currently executing transaction in seconds.
    '''
    pass

def get_action(_type: int, index: int) -> bytes:
    '''Retrieves the indicated action from the active transaction.

    Args:
        type: int - 0 for context free action, 1 for action
        index: int - the index of the requested action
    '''
    pass

def get_context_free_data(index: int):
    '''Retrieve the signed_transaction.context_free_data[index].
    Args:
        index: int - the index of the context_free_data entry to retrieve
    '''
    pass

def assert_recover_key(digest: bytes, sig: bytes, pub_key: bytes):
    '''Assertion for recover key
    '''
    pass

def assert_ripemd160(data: bytes, hash: bytes):
    '''Assertion for ripemd160
    
    Args:
        data: data to hash
        hash: 20 bytes hash of ripemd160 
    '''
    pass

def assert_sha1(data: bytes, hash: bytes):
    '''Assertion for sha1
    
    Args:
        data: data to hash
        hash: 20 bytes hash of sha1 
    '''
    pass

def assert_sha256(data: bytes, hash: bytes):
    '''Assertion for sha256
    
    Args:
        data: data to hash
        hash: 32 bytes hash of sha256
    '''
    pass

def assert_sha512(data: bytes, hash: bytes):
    '''Assertion for sha512
    
    Args:
        data: data to hash
        hash: 64 bytes hash of sha512
    '''
    pass

def ripemd160(data: Union[str, bytes]) -> bytes:
    '''ripemd160 hash of data

    Returns:
        20 bytes hash
    '''
    pass

def sha1(data: Union[str, bytes]) -> bytes:
    '''Hash of sha1

    Returns:
        20 bytes of sha1 hash
    '''
    pass

def sha256(data: Union[str, bytes]) -> bytes:
    '''Hash of sha256

    Returns:
        32 bytes of sha256 hash
    '''
    pass

def sha512(data: Union[str, bytes]):
    '''Hash of sha512

    Returns:
        64 bytes of sha512 hash
    '''
    pass

def call_contract(contract: Name, args: bytes):
    '''Call a function in contract

    Args:
        contract: Name,
        args: bytes
    '''
    pass

def current_receiver() -> name:
    '''Get current receiver of action
    '''
    pass

def current_time() -> int:
    '''Get current block time in microseconds
    '''
    pass

def enable_log():
    '''Enable logging via print
    '''
    pass

def get_log():
    '''get all log of print
    '''
    pass

def get_active_producers() -> Tuple[str]:
    '''Gets the set of active producers.
    '''
    pass

def get_blockchain_parameters():
    '''Retrieve the blolckchain parameters
    '''
    pass

def get_code_hash(contract: Name):
    '''Get code hash of a contract
    '''
    pass

def get_code_version(contract: Name):
    '''Get code version of a contract
    '''
    pass

def get_resource_limits(account: Name):
    '''Get the resource limits of an account

    Returns:
       (ram_bytes, net_weight, cpu_weight)
    '''
    pass

def has_auth(account: Name):
    '''Verifies that account name has auth.
    '''
    pass

def is_account(account: Name):
    '''Check if an account is exists.
    Returns:
        True for account exists, False for account not exists.
    '''
    pass

def is_privileged(account: Name):
    '''Check if an account is privileged
    '''
    pass

def publication_time():
    '''Retrive the publication time
    '''
    pass

def read_action_data() -> bytes:
    '''Retrive data in an action

    Returns:
        bytes: raw data in an action
    '''
    pass

def read_transaction():
    '''Read raw transaction
    '''
    pass

def recover_key(digest: bytes, sig: bytes):
    '''Calculates the public key used for a given signature and hash used to create a message.
    Args:
        digest (bytes) : 32 bytes hash of sha256
        sig (bytes): raw signature
    '''
    pass

def require_auth(account: Name):
    '''Verifies that account exists in the set of provided auths on a action. Throws if not found. 
    '''
    pass

def require_auth2(account: Name, permission: Name):
    '''Verifies that account name exists in the set of provided auths on a action. Throws if not found.
    '''
    pass

def require_recipient(contract: Name):
    '''Send notify to contract
    '''
    pass

def send_context_free_inline(account: Name, action: Name, data: bytes):
    '''send inline context free action
    '''
    pass

def send_context_free_inline_raw(data):
    '''Send raw context free inline action
    '''
    pass

def send_inline(account: Name, action: Name, actor: Name, permission: Name, data: bytes):
    '''Send inline action
    '''
    pass

def send_inline_raw(data):
    '''send raw inline action
    '''
    pass

def set_action_return_value(data):
    '''set return value of action
    '''
    pass

def set_blockchain_parameters(parameters: Tuple[int]):
    '''
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
    '''
    pass

def set_kv_parameters_packed():
    pass

def set_privileged(account: Name, is_priv: bool):
    '''Set the privileged status of an account
    '''
    pass

def set_proposed_producers(producers: List[Name]):
    '''Proposes a schedule change, once the block that contains the proposal becomes irreversible, the schedule is promoted to "pending" automatically. Once the block that promotes the schedule is irreversible, the schedule will become "active"
    '''
    pass

def set_resource_limits(account: Name, ram_bytes: int, net_weight: int, cpu_weight: int):
    '''Set the resource limits of an account
    '''
    pass

def tapos_block_num() -> int:
    '''Gets the block number used for TAPOS on the currently executing transaction.
    '''
    pass

def tapos_block_prefix() -> int:
    '''Gets the block prefix used for TAPOS on the currently executing transaction.
    '''
    pass

def uuos_assert(test: bool, msg: str):
    '''raise exception if test is false
    '''
    pass

def uuos_assert_code(test: bool, code: int):
    '''raise exception with code if test is false
    '''
    pass

def token_create(issuer: Name, maximum_supply: int, sym: int):
    '''Create a token
    '''
    pass

def token_issue(to: Name, quantity: int, sym: int, memo: str):
    '''Issue aa token
    '''
    pass

def token_transfer(_from: Name, to: Name, quantity: int, sym: int, memo: str):
    '''Transfer a token
    '''
    pass

def token_open(owner: Name, symbol: int, ram_payer: Name):
    '''Open a token
    '''
    pass

def token_retire(amount: int, symbol: int, memo: str):
    '''
    Retire a token
    '''
    pass

def token_close(owner: Name, symbol: int):
    '''Close a token
    '''
    pass
