# Challenge 19: Break fixed-nonce CTR mode using substitutions
#
# The file challenge19.txt contains 60 base64-encoded ciphertexts. All were
# encrypted with AES-CTR using the same key and nonce=0. This means every
# ciphertext was XOR'd against an identical keystream — identical to the
# classic many-time-pad problem.
#
# Since: ciphertext[i] = plaintext[i] XOR keystream[i]
# XOR-ing two ciphertexts gives: plaintext_a[i] XOR plaintext_b[i]
# which can be attacked with frequency analysis or linguistic intuition.
#
# Approach (manual/semi-manual, as the challenge intends):
#   - For each keystream byte position, collect all ciphertext bytes at
#     that position across all 60 messages.
#   - Guess the keystream byte by finding which value, when XOR'd with the
#     column, produces the most plausible English characters.
#   - Use trigram analysis and context to resolve ambiguous positions.
#   - Human intuition about the plaintext content (these are W.B. Yeats
#     poems) helps converge faster than pure statistics.
#
# This is intentionally a bit manual — Challenge 20 automates it fully.
#
# Data file: challenge19.txt (base64-encoded ciphertexts, one per line)

from base64 import b64decode

with open('challenge19.txt', 'r') as f:
    ciphertexts: list[bytes] = [b64decode(line.strip()) for line in f if line.strip()]

# TODO: recover the keystream and decrypt the messages
