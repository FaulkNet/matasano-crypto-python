# Challenge 9: Implement PKCS#7 padding
#
# A block cipher transforms a fixed-sized block (usually 16 bytes) of
# plaintext into ciphertext. Real messages are rarely an exact multiple of
# the block size, so we need a padding scheme to make them fit.
#
# PKCS#7 padding works by appending N bytes, each with the value N, where N
# is the number of bytes needed to reach the next block boundary. If the
# message is already block-aligned, a full block of padding is appended so
# that the receiver can always unambiguously strip it.
#
# Example:
#   "YELLOW SUBMARINE" is 16 bytes. Padded to 20 bytes:
#   "YELLOW SUBMARINE\x04\x04\x04\x04"
#
# Task:
#   Implement pkcs7_pad(message: bytes, block_size: int) -> bytes
#
# This is a prerequisite for CBC mode (Challenge 10) and padding validation
# (Challenge 15). Almost every block cipher implementation in the wild uses
# PKCS#7 padding, which is why understanding and correctly validating it
# matters — padding oracle attacks (a major class of real-world crypto
# vulnerabilities) arise from mishandling exactly this.

# TODO: implement


input_block: bytes = b'YELLOW SUBMARINE'
block_size: int = 20
expected: bytes = b'YELLOW SUBMARINE\x04\x04\x04\x04'

assert pkcs7_pad(input_block, block_size) == expected
