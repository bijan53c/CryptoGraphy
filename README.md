# CryptoGraphy
Cryptographic projects and studies stuff here 

So this repo includes all projects I create to study cryptography field.
It may go by different folders, so I explain here each one are what.

-------------

## PyCrypto v.2026.8.12

Simple AES-GCM encryption of plaintext data into ciphertext, using a salt, nonce, and Argon2id-derived key.

**So what actually does it do?**

It's a demonstration of encrypting plaintext data in a way that:

- *we can avoid identical plaintext producing identical ciphertext*
  - The same plaintext can be encrypted using the same password/key while producing different ciphertexts:
    - A random salt is used during Argon2id key derivation, producing a different derived key when a different salt is used.
    - A nonce is used during AES-GCM encryption, making each encryption operation unique even when the key and plaintext are the same.

- *We can make key derivation more resource-intensive to make brute-force attacks harder*
  - Argon2id is used to derive the encryption key from the password with intentionally high computational and memory costs, making password guessing more expensive than with fast hashing algorithms such as SHA-256.
