# Challenge 44: DSA nonce recovery from repeated nonce
#
# If the same nonce k is used to sign two different messages m1 and m2:
#   s1 = modinv(k, q) * (H(m1) + x*r) mod q
#   s2 = modinv(k, q) * (H(m2) + x*r) mod q
#
# Since r = pow(g, k, p) mod q, r1 == r2 when k is reused.
# Subtracting the two s equations:
#   s1 - s2 = modinv(k, q) * (H(m1) - H(m2)) mod q
#   k = (H(m1) - H(m2)) * modinv(s1 - s2, q) mod q
#
# Once k is known, recover x from either signature (see Challenge 43).
#
# Data file: challenge44.txt
#   Each signature record contains four lines:
#     msg: <message text>
#     s: <s as decimal integer>
#     r: <r as decimal integer>
#     m: <SHA-1 hash of message as hex string>
#
# Find the pair of records with the same r value (same k), recover k,
# then recover x. Verify by checking SHA-1(hex(x)) equals:
EXPECTED_FINGERPRINT: str = 'ca8f6f7c66fa362d40760d135b763eb8527d3d52'

# DSA parameters (same as Challenge 43):
p = 0x800000000000000089e1855218a0e7dac38136ffafa72eda7859f2171e25e65eac698c1702578b07dc2a1076da241c76c62d374d8389ea5aeffd3226a0530cc565f3bf6b50929139eberaa10afe4c8aa23a1e0aea1de4a8a3f1b9e3b8add3a44af7e4cc0cd8df77cbef22d61a9a327a5879c9e9a68a549b5d1d8f76cc8dc6dea49e2ec7ac0ae2c08d9c5d6ba27d21b4e9b5ec62a1b4ab35cf10c18e2c68b3dc9e56de1dbe02c5f49be4caf41ed4c9b32a9c0ebaa36df28c4289c82a6f9cdd6d5a22b22db9bd6e3c01e5e7c0a6b6f0ead5d0a0e2d8a7c0a9b8a7a07de55e3c05e2a8d20b0b3a7b8e6c6f0d5d0a0e2d8a7c0a9b8a7a0
q = 0xf4f47f05794b256174bba6e9b396a7707e563c5b
g = 0x5958c9d3898b224b12672c0b98e06c60df923cb8bc999d119458fef538b8fa4046c8db53039db620c094c9fa077ef389b5322a559946a71903f990f1f7e0e025e2d7f7cf494aff1a0470f5b64c36b625a097f1651fe775323556fe00b3608c887892878480e99041be601a62166ca6894bdd41a7054ec89f756ba9fc95302291

# TODO: parse challenge44.txt, find repeated r, recover k and then x, verify fingerprint
