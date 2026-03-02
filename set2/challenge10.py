# Challenge 10: Implement CBC mode
#
# CBC (Cipher Block Chaining) mode is one of the most widely used block
# cipher modes. Unlike ECB mode (which encrypts each block independently and
# is therefore trivially broken by pattern analysis), CBC XORs each plaintext
# block with the previous ciphertext block before encrypting it. The first
# block is XORed with an initialization vector (IV).
#
# Decryption reverses this: decrypt each ciphertext block, then XOR the
# result with the previous ciphertext block (or the IV for the first block).
#
# The challenge prohibits using a library's CBC implementation — the point is
# to build it yourself on top of a raw ECB block cipher.
#
# Setup:
#   - Data file: challenge10.txt (Base64-encoded ciphertext)
#   - Key: b'YELLOW SUBMARINE'
#   - IV: 16 zero bytes (b'\x00' * 16)
#
# Task:
#   Implement aes_cbc_decrypt(ciphertext: bytes, key: bytes, iv: bytes) -> bytes
#   and use it to decrypt challenge10.txt. The plaintext should be
#   recognisable English text.
#
# This is the foundation for the CBC bitflipping attack in Challenge 16 and
# the padding oracle attack (Challenge 17 in Set 3). Understanding exactly
# how CBC chaining works — and what happens when you flip bits in a
# ciphertext block — is essential for both.

from base64 import b64decode

# TODO: implement

key: bytes = b'YELLOW SUBMARINE'
iv: bytes = b'\x00' * 16

with open('challenge10.txt', 'r') as f:
    ciphertext: bytes = b64decode(f.read())

plaintext: bytes = aes_cbc_decrypt(ciphertext, key, iv)
print(plaintext.decode('utf-8'))
