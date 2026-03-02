# Challenge 12: Byte-at-a-time ECB decryption (Simple)
#
# This is the first challenge described as breaking "real crypto." The
# attack recovers a secret string appended to your input by an ECB oracle,
# one byte at a time, without ever knowing the key.
#
# The oracle encrypts:
#   AES-128-ECB(your_input || secret_string, consistent_random_key)
#
# The secret string is the following Base64-encoded value (decode it in code,
# don't manually decode it):
#
#   Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkg
#   aGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBq
#   dXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3AgTm8ganVzdCBkcm92ZSBieQo=
#
# Attack steps:
#   1. Feed identical bytes to the oracle one at a time until the ciphertext
#      grows — the jump in size reveals the block size.
#   2. Confirm ECB mode using the technique from Challenge 11.
#   3. To recover byte N of the secret: craft an input that puts byte N at
#      the end of a known block (one byte short of a full block of your
#      chosen bytes). Encrypt that, save the block. Then try all 256 possible
#      values for that byte, find the one that produces a matching block.
#   4. Repeat for every byte.
#
# Task:
#   Implement the oracle and the full byte-at-a-time attack.
#   Print the recovered secret string.

from base64 import b64decode

SECRET: bytes = b64decode(
    'Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkg'
    'aGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBq'
    'dXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3AgTm8ganVzdCBkcm92ZSBieQo='
)

# TODO: implement oracle and attack
