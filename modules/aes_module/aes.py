# AES Encryption using Python
# Author: Blake D 
# Copyright (c) 2024 GodsApostles. All rights reserved.

import base64
import hashlib
import os
from typing import Tuple, Union, Optional
from Crypto import Random
from Crypto.Cipher import AES as CryptoAES


class AES:
    """
    Securely encrypts and decrypts data using AES with a simple interface.
    
    This class provides an intuitive API for AES encryption operations,
    handling key derivation, padding, and encoding/decoding automatically.
    """
    
    def __init__(self, key: Union[str, bytes]) -> None:
        """
        Initialize the AES cipher with a secret key.
        
        Args:
            key: The encryption key as string or bytes. 
                 Will be hashed to produce a secure 256-bit key.
        """
        self.block_size = CryptoAES.block_size
        
        # Convert string keys to bytes if needed
        if isinstance(key, str):
            key = key.encode('utf-8')
            
        # Derive a secure key using SHA-256
        self.key = hashlib.sha256(key).digest()
    
    def encrypt(self, plaintext: Union[str, bytes]) -> str:
        """
        Encrypt data and return the base64-encoded ciphertext.
        
        Args:
            plaintext: The data to encrypt (string or bytes)
            
        Returns:
            The encrypted data as a base64-encoded string
        """
        # Convert string to bytes if needed
        if isinstance(plaintext, str):
            plaintext = plaintext.encode('utf-8')
            
        # Add padding
        padded_data = self._pad(plaintext)
        
        # Generate a random initialization vector
        iv = Random.new().read(self.block_size)
        
        # Create cipher and encrypt
        cipher = CryptoAES.new(self.key, CryptoAES.MODE_CBC, iv)
        encrypted_bytes = iv + cipher.encrypt(padded_data)
        
        # Return base64 encoded result
        return base64.b64encode(encrypted_bytes).decode('utf-8')
    
    def decrypt(self, ciphertext: Union[str, bytes]) -> str:
        """
        Decrypt a base64-encoded ciphertext and return the plaintext.
        
        Args:
            ciphertext: The encrypted data (base64 string or bytes)
            
        Returns:
            The decrypted plaintext as a string
            
        Raises:
            ValueError: If decryption fails due to invalid data or key
        """
        try:
            # Convert string to bytes if needed
            if isinstance(ciphertext, str):
                ciphertext = ciphertext.encode('utf-8')
                
            # Decode from base64
            encrypted_data = base64.b64decode(ciphertext)
            
            # Extract IV and ciphertext
            iv = encrypted_data[:self.block_size]
            actual_ciphertext = encrypted_data[self.block_size:]
            
            # Create cipher and decrypt
            cipher = CryptoAES.new(self.key, CryptoAES.MODE_CBC, iv)
            decrypted_bytes = self._unpad(cipher.decrypt(actual_ciphertext))
            
            # Return decoded result
            return decrypted_bytes.decode('utf-8')
        except Exception as e:
            raise ValueError(f"Decryption failed: {str(e)}")
    
    def _pad(self, data: bytes) -> bytes:
        """Add PKCS7 padding to data."""
        padding_length = self.block_size - len(data) % self.block_size
        padding = bytes([padding_length]) * padding_length
        return data + padding
    
    def _unpad(self, data: bytes) -> bytes:
        """Remove PKCS7 padding from data."""
        padding_length = data[-1]
        if padding_length > self.block_size:
            raise ValueError("Invalid padding")
        if data[-padding_length:] != bytes([padding_length]) * padding_length:
            raise ValueError("Invalid padding")
        return data[:-padding_length]

    @classmethod
    def generate_key(cls, length: int = 32) -> bytes:
        """
        Generate a secure random key of specified length.
        
        Args:
            length: Key length in bytes (default: 32)
            
        Returns:
            Random bytes suitable for use as an encryption key
        """
        return os.urandom(length)
    
    @classmethod
    def encrypt_simple(cls, key: Union[str, bytes], data: Union[str, bytes]) -> str:
        """
        One-line encryption method for simple use cases.
        
        Args:
            key: The encryption key (string or bytes)
            data: The data to encrypt (string or bytes)
            
        Returns:
            The encrypted data as a base64-encoded string
        """
        cipher = cls(key)
        return cipher.encrypt(data)
    
    @classmethod
    def decrypt_simple(cls, key: Union[str, bytes], ciphertext: Union[str, bytes]) -> str:
        """
        One-line decryption method for simple use cases.
        
        Args:
            key: The encryption key (string or bytes)
            ciphertext: The encrypted data (base64 string or bytes)
            
        Returns:
            The decrypted plaintext as a string
        """
        cipher = cls(key)
        return cipher.decrypt(ciphertext)
