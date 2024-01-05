EASYCrypt: Simple Python Cryptography
EASYCrypt is a Python library designed to make cryptography accessible and straightforward. Whether you need basic encryption or decryption, EASYCrypt simplifies the process with clear and concise functions.

Why EASYCrypt?
Simple and Intuitive: No expertise in cryptography required. EASYCrypt offers functions that are clear and easy to understand.

Focus on Common Tasks: Covering frequently used encryption and decryption scenarios, EASYCrypt minimizes configuration and technical details.

Lightweight and Efficient: Keep your code bloat-free and performant with EASYCrypt.

Ideal for Quick Jobs: Secure secrets, cookies, or files effortlessly with just a few lines of code.

What Can You Do with EASYCrypt?
Encrypt and decrypt data using popular algorithms like AES and DES.

Generate secure keys and initialization vectors.

Encode and decode data in base64, hexadecimal, or other formats.

Sign and verify data to ensure authenticity and integrity.

Getting Started
Install EASYCrypt:

bash
Copy code
pip install easycrypt
Import the Library:

python
Copy code
from easycrypt import EasyCrypt
Create an EasyCrypt Object with Your Key:

python
Copy code
encryptor = EasyCrypt(b"your_secret_key")
Encrypt Your Data:

python
Copy code
ciphertext = encryptor.encrypt(b"your_data")
Decrypt Your Data:

python
Copy code
plaintext = encryptor.decrypt(ciphertext)
That's it! EASYCrypt handles the rest.

Advanced Features
For advanced users, EASYCrypt offers additional features such as custom algorithms and modes. Explore the documentation for complete details.

Remember to use cryptography responsibly and ethically.

Happy coding!
