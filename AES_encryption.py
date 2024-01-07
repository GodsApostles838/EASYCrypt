from Crypto import Random
from Crypto.Cipher import AES
import os

class AES_EASYcrypt:
    def __init__(self, key: bytes) -> None:
        self.key = self.pad(key)

    def pad(self, s: bytes) -> bytes:
        return s + b"\0" * (AES.block_size - len(s) % AES.block_size)

    def encrypt(self, message: bytes) -> bytes:
        message = self.pad(message)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return iv + cipher.encrypt(message)

    def encrypt_file(self, file_name: str) -> None:
        with open(file_name, "rb") as fo:
            plaintext = fo.read()
        enc = self.encrypt(plaintext)
        with open(file_name + ".enc", "wb") as fo:
            fo.write(enc)
        os.remove(file_name)

    def decrypt(self, cipherText: bytes) -> bytes:
        iv = cipherText[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        decrypted = cipher.decrypt(cipherText[AES.block_size:])
        return decrypted.rstrip(b"\0")

    def decrypt_file(self, file_name: str) -> None:
        with open(file_name + ".enc", 'rb') as fo:
            cipherText = fo.read()
        d = self.decrypt(cipherText)
        with open(file_name, 'wb') as fo:
            fo.write(d)
        os.remove(file_name + ".enc")

    def G_A_F(self) -> list:
        dir_path = os.path.dirname(os.path.realpath(__file__))
        dirs = []

        for dirName, _, fileList in os.walk(dir_path):
            for fname in fileList:
                if fname not in ['script.py', 'data.txt.enc']:
                    dirs.append(os.path.join(dirName, fname))

        return dirs

    def encrypt_m(self, message: str) -> bytes:
        encrypted_message = self.encrypt(message.encode('utf-8'))
        return encrypted_message
    
    def decrypt_m(self, encrypted_message: bytes) -> str:
        decrypted_message = self.decrypt(encrypted_message).decode('utf-8')
        return decrypted_message

    def m_x_to_e(self, key: bytes) -> bytes:
        result = bytearray()
        i = 0

        while i < len(key):
            if key[i:i + 1] == b'x':
                if i > 0 and key[i - 1:i] != b'\\' and key[i - 1:i] != b'\n':
                    result.extend([key[i - 1], key[i]])  # Merge 'x' with the previous byte
                elif i < len(key) - 1:
                    result.extend([key[i], key[i + 1]])  # Merge 'x' with the next byte
                    i += 1  # Skip the next character
                else:
                    result.append(key[i])  # Append standalone 'x' at the end
            else:
                result.append(key[i])
            i += 1

        return bytes(result)