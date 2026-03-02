# Challenge 18: Implement CTR, the stream cipher mode
#
# CTR (Counter) mode turns AES into a stream cipher. Instead of encrypting
# the plaintext directly, you encrypt a counter value to produce a keystream,
# then XOR the keystream with the plaintext.
#
# Counter block format (little-endian):
#   [8 bytes nonce (LE)] [8 bytes block count (LE)]
#
# For each 16-byte block:
#   keystream_block = AES_ECB_encrypt(nonce_counter_block, key)
#   output_block    = plaintext_block XOR keystream_block
#
# Decryption is identical to encryption (XOR is its own inverse).
# CTR mode does not require padding — just stop XOR-ing when you run out
# of plaintext.
#
# CTR mode is attractive because it allows random access (seek to any
# position by computing the right counter block) and is parallelisable.
# Its weakness: reusing a nonce with the same key is catastrophic, since
# you get the same keystream and XOR-ing two ciphertexts cancels the key,
# leaving plaintext XOR plaintext (see Challenges 19 and 20).
#
# Task:
#   Implement aes_ctr(data: bytes, key: bytes, nonce: int) -> bytes
#   and use it to decrypt the ciphertext below.

from base64 import b64decode

CIPHERTEXT: bytes = b64decode(
    'L77na/nrFsKvynd6HzOoG7GHTLXsTVu9qvY/2syLXzhPweyyMTJULu/6/kXX0KSvoOLSFQ=='
)
KEY: bytes = b'YELLOW SUBMARINE'
NONCE: int = 0

# TODO: implement aes_ctr and decrypt CIPHERTEXT
