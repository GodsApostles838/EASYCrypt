
def c_blocksize(blocksize):
    return ("Block size is missing" 
            if blocksize is None else f"Error: Block size must be greater than 16 (provided: {blocksize})" if blocksize <= 16 else None)

def c_key_size(key_size):
    return ("Key size is missing" 
            if key_size is None else f"Error: Key size must be greater than 16 (provided: {key_size})" if key_size <= 16 else None)

def c_plaintext(plaintext):
    return ("Error: Plaintext cannot be empty"
            if plaintext is None or plaintext == "" else None)

