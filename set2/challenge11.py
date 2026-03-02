# Challenge 11: An ECB/CBC detection oracle
#
# At this point you have ECB and CBC under your belt. Now we build the
# first real "oracle" — a black-box function that encrypts data in a way
# you can't fully see — and write code to detect which mode it used.
#
# The oracle:
#   1. Generates a random 16-byte AES key.
#   2. Prepends 5-10 random bytes to the plaintext.
#   3. Appends 5-10 random bytes to the plaintext.
#   4. Flips a coin: encrypts with ECB half the time, CBC the other half
#      (using a random IV for CBC).
#
# Your detector:
#   Feed the oracle a plaintext of your choice (hint: lots of repeated
#   bytes) and inspect the ciphertext. ECB mode produces identical
#   ciphertext blocks for identical plaintext blocks — CBC does not.
#   If you see two identical 16-byte blocks in the output, it's ECB.
#
# Task:
#   Implement encryption_oracle(plaintext: bytes) -> bytes
#   Implement detect_mode(ciphertext: bytes) -> str  # returns 'ECB' or 'CBC'
#
# This is the canonical ECB detection technique. It works because ECB is
# stateless — each block is encrypted in isolation — so any repeated
# plaintext block produces a repeated ciphertext block, leaking structure
# about the message. This is why ECB mode should never be used for anything
# longer than a single block.

import os

# TODO: implement


# Sanity check: run the oracle many times and verify the detector is correct.
# (The oracle tells you which mode it used so you can check your answer.)
