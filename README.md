# CryptoGraphy
Cryptographic projects and studies stuff here 

So this repo includes all projects I create to study cryptography field.
It may go by different folders, so I explain here each one are what.

-------------

## PyCrypto v.2026.8.12
Simple AES algorithm encryption of a clear text to cipher, using salt, nonce and argon based key.
**So what actually it does?**
It's a demonstration on how to encrypt a clear text (data), in a way that:
- *==How avoid compromising a cipher text if same data is leaked in other place?==*
  - By this solutions you can encrypt using same key, the same plain text, but get different cipher texts. How?
    - Adding salt to the key generation using argon2 hash, causing our key to be different each time even with same password
    - Adding nonce to the encryption process, so the cipher text gets random output even if the key and plain text are same
    - *"So in short we got 2 different randomization in process, each at their own spot"*
- *==How to make a key generation resource demanding and time consuming to make brute force harder==*
  - using argon2, we turn the password in hash, but not as fast as sha256, but time consuming and demanding specific resource
