# Challenge 20: Break fixed-nonce CTR statistically
#
# Same vulnerability as Challenge 19 (fixed nonce CTR = many-time pad),
# but now solved statistically rather than manually.
#
# The key insight: if you truncate all ciphertexts to the length of the
# shortest one and concatenate them, you have a repeating-key XOR problem
# where the "key" is the keystream and the "key length" is the truncated
# ciphertext length. Apply the same frequency analysis from Challenge 6
# (break repeating-key XOR) column by column.
#
# Steps:
#   1. Load and decode all ciphertexts from challenge20.txt.
#   2. Truncate to the shortest ciphertext length.
#   3. Transpose: collect all bytes at position 0, all at position 1, etc.
#   4. For each column, score all 256 XOR keys by English letter frequency
#      (exactly like Challenge 3).
#   5. Assemble the keystream from the best-scoring byte per column.
#   6. XOR each ciphertext against the recovered keystream.
#
# Data file: challenge20.txt (base64-encoded ciphertexts, one per line)

from base64 import b64decode

with open('challenge20.txt', 'r') as f:
    ciphertexts: list[bytes] = [b64decode(line.strip()) for line in f if line.strip()]

# TODO: truncate, transpose, and crack column by column
