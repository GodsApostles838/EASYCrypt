# EASYCrypt Library
# Author: Blake D 
# Copyright (c) 2024 GodsApostles. All rights reserved.

"""
EASYCrypt: Simple and secure cryptography for Python developers.

This library provides intuitive interfaces for common cryptographic operations,
making encryption, decryption, and other security tasks accessible to developers
of all experience levels.
"""

# Version information
__version__ = '0.1.0'
__author__ = 'Blake D (GodsApostles)'

# Import core modules
from .aes import AES

# Convenience functions
def encrypt(key, data):
    """Encrypt data using AES encryption."""
    return AES.encrypt_simple(key, data)

def decrypt(key, data):
    """Decrypt AES-encrypted data."""
    return AES.decrypt_simple(key, data)

def generate_key(length=32):
    """Generate a secure random key."""
    return AES.generate_key(length)
