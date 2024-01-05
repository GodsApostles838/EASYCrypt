from AES_encryption import AESEncrypt
from os import urandom

# Encryption steps (unchanged)
message = input("Enter your message: ")
aes_instance = AESEncrypt(urandom(16), message.encode())
ciphertext, iv = aes_instance.encrypt()
print("Encrypted message:", ciphertext)

# Decryption steps
try:
    # Recreate AESEncrypt instance with the same key and IV
    aes_instance = AESEncrypt(aes_instance.key, iv)  # Assuming key is accessible

    # Decrypt the ciphertext
    decrypted_message = aes_instance.decrypt(ciphertext)

    print("Decrypted message:", decrypted_message.decode())
except ValueError as e:
    print("Decryption failed:", e)
