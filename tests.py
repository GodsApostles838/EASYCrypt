from AES_encryption import AES_EASYcrypt

key = b'Donuts'

easy_crypt = AES_EASYcrypt(key)

message_to_encrypt = "Hello, this is a secret message!"
encrypted_message = easy_crypt.encrypt_m(message_to_encrypt)

print("-" * 100)
print(f"Original Message: {message_to_encrypt}")
print("-" * 100)
print(f"Encrypted Message: {encrypted_message}")
print("-" * 100)
print(f"X merged to end: {easy_crypt.m_x_to_e(encrypted_message)}")
print("-" * 100)
