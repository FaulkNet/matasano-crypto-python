# Challenge 46: RSA parity oracle
#
# An RSA parity oracle answers one question: is the decrypted plaintext even
# or odd? That single bit, queried repeatedly, allows full plaintext recovery.
#
# Why: multiplying a ciphertext by pow(2, e, n) is equivalent to doubling
# the plaintext (mod n). If the doubled plaintext overflows n, a modulo
# reduction occurs, changing parity. Tracking whether overflow occurred
# reveals which half of [0, n) the plaintext fell in — a binary search.
#
# Algorithm (~log2(n) iterations, i.e. ~1024 for a 1024-bit key):
#   lower, upper = 0, n
#   f = ciphertext
#   for _ in range(1024):
#       f = f * pow(2, e, n) mod n    (double the plaintext)
#       if oracle(f) == even:         (no overflow: plaintext < n/2 relative to current range)
#           upper = (lower + upper) // 2
#       else:                         (overflow: plaintext >= n/2)
#           lower = (lower + upper) // 2
#   return upper  (converges to plaintext)
#
# Task:
#   Generate a 1024-bit RSA keypair.
#   Encrypt the base64-decoded message below.
#   Implement the oracle and the binary search attack.
#   Print the recovered plaintext. (It decrypts to something recognisable.)

from base64 import b64decode

CIPHERTEXT_B64: str = 'VGhhdCdzIHdoeSBJIGZvdW5kIHlvdSBkb24ndCBwbGF5IGFyb3VuZCB3aXRoIHRoZSBGdW5reSBDb2xkIE1lZGluYQ=='

# TODO: implement oracle and binary search attack
