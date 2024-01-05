from AES_encryption import *

a =  "hello world"

# Encryption:
print((lambda ai: ai.encrypt())(AESEncrypt(urandom(16), a)))

# Decryption:
print((lambda ai: ai.return_key(ai.encrypt()))(AESEncrypt(urandom(16), a)))
