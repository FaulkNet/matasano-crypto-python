# Challenge 26: CTR bitflipping
#
# The same bitflipping attack from Challenge 16 (CBC), now applied to CTR.
# In CTR mode the relationship is even simpler: flipping bit N in the
# ciphertext flips bit N in the plaintext with no effect on any other byte.
# There is no block corruption to worry about.
#
# Setup (same as Challenge 16):
#   encrypt_userdata(userdata: str) -> bytes
#     Prepends "comment1=cooking%20MCs;userdata="
#     Appends  ";comment2=%20like%20a%20pound%20of%20bacon"
#     Sanitises ';' and '=' from userdata
#     Encrypts under AES-CTR with a random key
#
#   is_admin(ciphertext: bytes) -> bool
#     Decrypts and checks for ";admin=true;"
#
# The attack:
#   Submit a known userdata payload. Identify which byte positions in the
#   ciphertext correspond to the characters you want to flip in the plaintext.
#   XOR those ciphertext bytes with (current_char XOR target_char) to flip
#   the plaintext bits exactly. No two-block sacrifice needed — CTR gives
#   you direct one-to-one bit control.
#
# This drives home the message: encryption ≠ authentication.
# Without a MAC, any cipher mode can be manipulated by an active attacker.

import os

# TODO: implement encrypt_userdata, is_admin, and the attack
