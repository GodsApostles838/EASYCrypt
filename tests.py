from modules.aes_module.aes import *

key="donuts"
encrypted_message = AES.encrypt(encryption_key="donuts", message="Hello, world!")
print(f"Encrypted message: {encrypted_message}")

decrypted_message = AES(key).decrypt(encrypted_message)
print(f"Decrypted message: {decrypted_message}")
