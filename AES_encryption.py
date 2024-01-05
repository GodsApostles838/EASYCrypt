import typing
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from os import urandom

class AESEncrypt:
    """
    Encrypts and decrypts data using the AES algorithm with CFB mode.
    """

    AES_ALGORITHM = algorithms.AES
    CFB_MODE = modes.CFB

    def __init__(self, key: bytes, plaintext: typing.Union[bytes, str]) -> None:
        """
        Initializes the AESEncrypt instance.

        Args:
            key (bytes): The key used for encryption and decryption.
            plaintext (Union[bytes, str]): The plaintext to be encrypted.
        """
        self._key = key
        self._plaintext = plaintext
        self._iv = urandom(16)

    def _hex_to_bytes(self, hex_string: str) -> bytes:
        """
        Converts a hexadecimal string to bytes.

        Args:
            hex_string (str): The hexadecimal string to be converted.

        Returns:
            bytes: The corresponding bytes representation.

        Raises:
            ValueError: If the input string is not a valid hexadecimal string.
        """
        try:
            return bytes.fromhex(hex_string)
        except ValueError:
            raise ValueError("Invalid hexadecimal string") from None

    def _bytes_to_hex(self, byte_data: bytes) -> str:
        """
        Converts bytes to a hexadecimal string.

        Args:
            byte_data (bytes): The bytes to be converted.

        Returns:
            str: The corresponding hexadecimal string.
        """
        return byte_data.hex()

    def _initialize_cipher(self) -> Cipher:
        """
        Initializes the AES cipher with CFB mode.

        Returns:
            Cipher: The initialized AES cipher.
        """
        backend = default_backend()
        return Cipher(self.AES_ALGORITHM(self._key), self.CFB_MODE(self._iv), backend=backend)

    def encrypt(self) -> typing.Tuple[str, str]:
        """
        Encrypts the plaintext using AES algorithm.

        Returns:
            Tuple[str, str]: A tuple containing the ciphertext (hex) and IV (hex).
        """
        cipher = self._initialize_cipher()
        encryptor = cipher.encryptor()

        if isinstance(self._plaintext, str):
            plaintext_bytes = self._plaintext.encode()
        elif isinstance(self._plaintext, bytes):
            plaintext_bytes = self._plaintext
        else:
            raise ValueError("Invalid plaintext type")

        ciphertext = encryptor.update(plaintext_bytes) + encryptor.finalize()
        return self._bytes_to_hex(ciphertext), self._bytes_to_hex(self._iv)

    def decrypt(self, ciphertext_hex: str, iv_hex: str) -> bytes:
        """
        Decrypts the ciphertext using AES algorithm.

        Args:
            ciphertext_hex (str): The ciphertext (hex) to be decrypted.
            iv_hex (str): The IV (hex) used in decryption.

        Returns:
            bytes: The decrypted data.

        Raises:
            ValueError: If decryption fails.
        """
        try:
            cipher = self._initialize_cipher()
            iv = self._hex_to_bytes(iv_hex)
            decryptor = cipher.decryptor()
            ciphertext = self._hex_to_bytes(ciphertext_hex)
            decrypted_data = decryptor.update(ciphertext) + decryptor.finalize()
            return decrypted_data
        except Exception as e:
            raise ValueError(f"Decryption failed: {e}") from None

    def return_key(self, key: typing.Tuple[str, str]) -> bytes:
        """
        Decrypts the ciphertext using AES algorithm and returns the decrypted data.
        (This method seems redundant as it's functionally equivalent to decrypt())

        Args:
            key (Tuple[str, str]): A tuple containing the ciphertext (hex) and IV (hex).

        Returns:
            bytes: The decrypted data.

        Raises:
            ValueError: If decryption fails.
        """
        try:
            ciphertext_hex, iv_hex = key
            decrypted_data = self.decrypt(ciphertext_hex, iv_hex)
            return decrypted_data
        except ValueError as e:
            raise
