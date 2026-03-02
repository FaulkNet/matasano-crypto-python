# Challenge 16: CBC bitflipping attacks
#
# CBC mode has a useful (and dangerous) property: flipping a bit in ciphertext
# block N causes a completely garbled block N in the plaintext, but it also
# produces the exact same bit flip in block N+1. An attacker who can control
# part of the ciphertext and observe the result can exploit this to modify
# the decrypted plaintext in a precise, predictable way — without knowing
# the key.
#
# Setup:
#   Function 1 — encrypt_userdata(userdata: str) -> bytes
#     Prepends:  "comment1=cooking%20MCs;userdata="   (32 bytes = 2 blocks)
#     Appends:   ";comment2=%20like%20a%20pound%20of%20bacon"
#     Sanitises: replaces ';' and '=' in userdata with '?' (or similar)
#     Pads to block size and encrypts with AES-CBC using a random key and IV.
#
#   Function 2 — is_admin(ciphertext: bytes) -> bool
#     Decrypts and checks whether the plaintext contains ";admin=true;"
#
# The attack:
#   You cannot inject ";admin=true;" directly because the oracle sanitises
#   your input. Instead, submit a crafted userdata that, after a ciphertext
#   bit-flip, produces ";admin=true;" in the decrypted output.
#
#   Hint: your userdata lands in block 3 (0-indexed: block 2). The bit-flip
#   you apply to block 2 of the ciphertext will corrupt block 2 of the
#   plaintext but flip the corresponding bits in block 3 exactly as intended.
#   Use XOR to compute which bits to flip.
#
# Task:
#   Implement both functions and the attack. Call is_admin() with your forged
#   ciphertext and assert that it returns True.
#
# This attack motivates authenticated encryption (AES-GCM, AES-CCM, etc.).
# CBC without a MAC provides no integrity guarantee whatsoever.

import os

# TODO: implement
