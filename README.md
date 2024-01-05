# EASYCrypt

## **KEY FEATURES**

- Effortless Encryption and Decryption: Handle common cryptographic tasks with just a few lines of code.

- User-Friendly Design: No need to be a cryptography expert, thanks to EASYCrypt's intuitive libary makes it accessible to all.

- Focus on Essentials: Covers the most frequently used encryption techniques, streamlining your workflow.

- Lightweight and Efficient: Keeps your code clean and performant, avoiding unnecessary bloat.

- Ideal for Quick Tasks: Secure sensitive information, cookies, files, and more with ease.

## **Available Features**

- Encryption and decryption using popular algorithms (AES, DES, etc.)
- Secure key and initialization vector generation
- Data encoding and decoding (base64, hexadecimal, etc.)
- Data signing and verification for authenticity and integrity
- Customizable for advanced users (explore documentation for details)

![Static Badge](https://img.shields.io/badge/version-v1.0.0-blue?style=flat&logoColor=grey&labelColor=grey&color=blue) ![Static Badge](https://img.shields.io/badge/Python-v3.12.0-blue?labelColor=yellow)



----
**How to get started**


**1.** You're going to need to import easycrypt using PIP. Make sure you have PIP up-to date.
```cs
C:\Users\User> pip install easycrypt
```

**2.** You need to make sure you're in the project, you can do this by opening the terminal and typing the following command, or you can navigate to the project folder, left click and open terminal in there.
```cs
C:\Users\User> cd Yourproject
C:\Users\User\Yourprojecr>
```

**3.** All done! Now just import easycrypt and happy coding, find some examples down below.


**Example 1** Message encyption
```python
from AES_encryption import *

message = input("Enter your message: ")
ciphertext, iv = AESEncrypt(urandom(16), message.encode()).encrypt()
print("Encrypted message:", ciphertext)  # Remove .hex() here

```

**Example 2** Easy encyption (simple & most easiest)
```python
from AES_encryption import *

a =  "hello world"

# Encryption:
print((lambda ai: ai.encrypt())(AESEncrypt(urandom(16), a)))

# Decryption:
print((lambda ai: ai.return_key(ai.encrypt()))(AESEncrypt(urandom(16), a)))

```
