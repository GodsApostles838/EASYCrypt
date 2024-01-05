from os import urandom
class EncryptionError(Exception):
    pass  # Custom exception for encryption errors

class IVGenerator:
    def __call__(self):
        self._iv = urandom(16)  # Generate and store IV
        return self._iv