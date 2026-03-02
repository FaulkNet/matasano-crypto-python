# Challenge 42: Bleichenbacher's e=3 RSA Attack (signature forgery)
#
# PKCS#1 v1.5 signature format (for a 1024-bit key):
#   00 01 [FF padding...] 00 [ASN.1 digest info] [hash]
#
# A lazy verifier might only check that the signature starts with "00 01 FF"
# and that the hash at the end matches, without verifying that the FF
# padding extends all the way to the ASN.1 block. This lets us forge.
#
# The forge:
#   We want to find an integer x such that x^3 (mod n) looks like a valid
#   PKCS#1 block when interpreted as bytes. If the verifier doesn't check
#   the padding length, we just need the block to start with:
#     00 01 FF 00 [ASN.1] [SHA1(message)]
#   followed by garbage.
#
#   Construct the target block with the above prefix, zero-pad the rest,
#   then take the cube root (rounding up). Cube that result and check that
#   the top bytes match. The cube won't wrap n if the valid prefix is in
#   the top bits and the rest is small.
#
# Task:
#   Implement a 1024-bit RSA signature verifier with the above bug.
#   Forge a valid signature for the string "hi mom" without the private key.

from hashlib import sha1

TARGET_MESSAGE: bytes = b'hi mom'

# TODO: implement the vulnerable verifier and the cube-root forgery attack
