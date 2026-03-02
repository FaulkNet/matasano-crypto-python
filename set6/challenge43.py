# Challenge 43: DSA key recovery from nonce
#
# DSA signing for message m:
#   1. Generate random nonce k (1 < k < q)
#   2. r = pow(g, k, p) mod q
#   3. s = modinv(k, q) * (H(m) + x*r) mod q
#   (x is the private key)
#
# Key recovery given k:
#   From s = modinv(k, q) * (H(m) + x*r) mod q, solve for x:
#   x = (s*k - H(m)) * modinv(r, q) mod q
#
# If k is weak (e.g. 16-bit: 0 < k < 2^16), brute force all 65536 values,
# compute the candidate x for each, and check whether pow(g, x, p) mod q == y
# (the public key).
#
# Given data:
#   Public key y:
y = 0x84ad4719d044495496a3201c8ff484feb45b962e7302e56a392aee4abab3e4bdebf2955b4736012f21a08084056b19bcd7fee56048e004e44984e2f411788efdc837a0d2e5abb7b555039fd243ac01f0fb2ed1dec568280ce678e931868d23eb095fde9d3779191b8c0299d6e07bbb283e6633451e535c45513b2d33c99ea17

#   Parameters (DSA standard):
p = 0x800000000000000089e1855218a0e7dac38136ffafa72eda7859f2171e25e65eac698c1702578b07dc2a1076da241c76c62d374d8389ea5aeffd3226a0530cc565f3bf6b50929139eberaa10afe4c8aa23a1e0aea1de4a8a3f1b9e3b8add3a44af7e4cc0cd8df77cbef22d61a9a327a5879c9e9a68a549b5d1d8f76cc8dc6dea49e2ec7ac0ae2c08d9c5d6ba27d21b4e9b5ec62a1b4ab35cf10c18e2c68b3dc9e56de1dbe02c5f49be4caf41ed4c9b32a9c0ebaa36df28c4289c82a6f9cdd6d5a22b22db9bd6e3c01e5e7c0a6b6f0ead5d0a0e2d8a7c0a9b8a7a07de55e3c05e2a8d20b0b3a7b8e6c6f0d5d0a0e2d8a7c0a9b8a7a0
q = 0xf4f47f05794b256174bba6e9b396a7707e563c5b
g = 0x5958c9d3898b224b12672c0b98e06c60df923cb8bc999d119458fef538b8fa4046c8db53039db620c094c9fa077ef389b5322a559946a71903f990f1f7e0e025e2d7f7cf494aff1a0470f5b64c36b625a097f1651fe775323556fe00b3608c887892878480e99041be601a62166ca6894bdd41a7054ec89f756ba9fc95302291

#   Message and signature:
message: str = "For those that envy a MC it can be hazardous to your health\nSo be friendly, a matter of life and death, just like a etch-a-sketch\n"
r = 548099063082341131477253921760299949438196259240
s = 857042759984254168557880549501802188789837994940

# Expected SHA-1 fingerprint of the recovered private key (as hex string):
EXPECTED_FINGERPRINT: str = '0954edd5e0afe5542a4adf012611a91912a3ec16'

# TODO: brute force k in range(0, 2**16), recover x, verify fingerprint
