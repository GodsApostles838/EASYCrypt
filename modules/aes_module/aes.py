# AES Encryption using Python

# Author: Blake D 
# Copyright (c) 2024 GodsApostles. All rights reserved. 

import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES as CryptoAES 

class Aes:
    """
    Securely encrypts and decrypts data using AES. 
    """

    def __init__(self, key: bytes) -> None:
        """
        Initializes the cipher with a secret key.

        Args:
            key: The encryption key as bytes (exactly 16, 24, or 32 bytes).
        """
        self.bs = CryptoAES.block_size
        self.key = hashlib.sha256(key).digest()         

    def encrypt(self, plaintext: str) -> str:
        """
        Encrypts a message and returns the base64-encoded ciphertext.

        Args:
            plaintext: The message to be encrypted.

        Returns:
            The encrypted message as a base64-encoded string.
        """
        padded_text = self._pad(plaintext)
        iv = Random.new().read(self.bs) 
        cipher = CryptoAES.new(self.key, CryptoAES.MODE_CBC, iv)
        encrypted_bytes = iv + cipher.encrypt(padded_text.encode())
        return base64.b64encode(encrypted_bytes).decode('utf-8')

    def decrypt(self, ciphertext: bytes) -> str:
        """
        Decrypts a base64-encoded ciphertext and returns the plaintext.

        Args:
            ciphertext: The ciphertext to be decrypted as bytes.

        Returns:
            The decrypted plaintext message.
        """
        ciphertext = base64.b64decode(ciphertext)
        iv = ciphertext[:self.bs]
        cipher = CryptoAES.new(self.key, CryptoAES.MODE_CBC, iv)
        decrypted_bytes = self._unpad(cipher.decrypt(ciphertext[self.bs:]))
        return decrypted_bytes.decode('utf-8')

    @staticmethod
    def _pad(text: str) -> str:
        """
        Adds PKCS7 padding to a string.

        Args:
            text: The string to be padded.

        Returns:
            The padded string.
        """
        padding_length = AES.bs - len(text) % AES.bs
        return text + chr(padding_length) * padding_length

    @staticmethod
    def _unpad(padded_bytes: bytes) -> bytes:
        """
        Removes PKCS7 padding from bytes.

        Args:
            padded_bytes: The bytes to be unpadded.

        Returns:
            The unpadded bytes.
        """
        return padded_bytes[:-padded_bytes[-1]]

    @classmethod
    def encrypt_message(cls, key: str, message: str) -> str:
        """
        Convenient class method for encrypting a message with a string key.

        Args:
            key: The encryption key as a string.
            message: The message to be encrypted.

        Returns:
            The encrypted message as a base64-encoded string.
        """
        cipher = cls(key.encode()) 
        return cipher.encrypt(message)
    
    
    def r_key(key: bytes) -> bytes:
        """
        Reversing hashed key

        Args:
            key (bytes): The encryption key as a string

        Returns:
            Reversed key for current key
        """
        return key[::-1]