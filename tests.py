from AES import *
from base64 import b64encode

# Example usage:
iv, ciphertext = AESEncrypt(key=b'hello world', key_size=256, cipher_mode='CBC', plaintext='This is secret').encrypt()

print('---------------------------------------')
print('IV:', b64encode(iv).decode('utf-8'))
print('Ciphertext:', b64encode(ciphertext).decode('utf-8'))


print('---------------------------------------')
print('IV:', b64encode(iv).decode('utf-8'))
print('Ciphertext:', b64encode(ciphertext).decode('utf-8'))