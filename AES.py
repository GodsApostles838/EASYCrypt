from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from base64 import b64encode
from Constructors import *
# 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

class AESEncrypt:
    def __init__(self, key, key_size=128, cipher_mode='CFB', plaintext=''):
        self.key = self.derive_key(key)
        self.key_size = key_size
        self.cipher_mode = cipher_mode
        self.plaintext = plaintext
        self._iv = None

    def derive_key(self, key):
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=b'',
            iterations=100000,
            backend=default_backend()
        )
        return kdf.derive(key)

    def _set_algorithm(self):
        self._iv = IVGenerator()()
        return algorithms.AES(self.key), {
            'CBC': modes.CBC(self._iv),
            'GCM': modes.GCM(self._iv),
            'ECB': modes.ECB(),
            'OFB': None,
            'CTR': None
        }[self.cipher_mode]

    def encrypt(self):
        try:
            algorithm, mode = self._set_algorithm()
            cipher = Cipher(algorithm, mode, backend=default_backend())
            encryptor = cipher.encryptor()
            padder = padding.PKCS7(128).padder()
            iv, ciphertext = self._iv, b''

            for block in range(0, len(self.plaintext), 16):
                block_plaintext = self.plaintext[block:block + 16].encode('utf-8')  # Convert to bytes
                ciphertext += bytes(x ^ y for x, y in zip(encryptor.update(iv), block_plaintext))
                iv = (int.from_bytes(iv, 'big') + 1).to_bytes(16, 'big')

            return self._iv, ciphertext
        except Exception as e:
            raise EncryptionError(f"Encryption failed: {e}")


