#crypto.py

import os

from argon2.low_level import (
	hash_secret_raw,
	Type,
)
from cryptography.hazmat.primitives.ciphers.aead import AESGCM


SALT_SIZE = 16
NONCE_SIZE = 12
KEY_SIZE = 32


def derive_key(master_password: str, salt: bytes) -> bytes:
	return hash_secret_raw(
		secret=master_password.encode("utf-8"),
		salt=salt,
		time_cost=3,
		memory_cost=65536,
		parallelism=4,
		hash_len=KEY_SIZE,
		type=Type.ID,
	)


def encrypt(plaintext: bytes, key: bytes) -> tuple[bytes, bytes]:
	nonce = os.urandom(NONCE_SIZE)

	aes = AESGCM(key)
	ciphertext = aes.encrypt(
		nonce,
		plaintext,
		None,
	)

	return nonce, ciphertext


def decrypt(ciphertext: bytes, key:bytes, nonce: bytes) -> bytes:
	aes = AESGCM(key)

	return aes.decrypt(
		nonce,
		ciphertext,
		None,
	)
