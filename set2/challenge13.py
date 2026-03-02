# Challenge 13: ECB cut-and-paste
#
# ECB mode encrypts each block independently and deterministically. That
# means you can take ciphertext blocks from different oracle calls and
# splice them together to produce a ciphertext that, when decrypted, yields
# a plaintext you never directly encrypted. This is a forgery attack.
#
# Setup:
#   Build a profile system:
#     profile_for(email) -> "email=USER&uid=10&role=user"
#     (strip & and = from the email to prevent direct injection)
#
#   Encrypt and decrypt profiles using a consistent random AES-ECB key:
#     encrypt_profile(profile_str) -> ciphertext
#     decrypt_profile(ciphertext)  -> parsed dict
#
# The attack:
#   Using only profile_for() as your oracle (you cannot touch the key or
#   the encryption function directly), craft a ciphertext that decrypts to
#   a profile with role=admin.
#
#   Hint: choose an email address such that "admin" (with valid PKCS#7
#   padding) lands exactly at the start of a 16-byte block. Then swap that
#   block into the position where "user" sits in a normal profile.
#
# Task:
#   Implement the profile system, the encryption/decryption pair, and the
#   attack. Print the decrypted forged profile showing role=admin.
#
# This demonstrates why ECB mode is unsuitable for any protocol that must
# prevent message tampering — its block-independence is a feature that
# becomes a fatal flaw the moment an attacker can observe multiple outputs.

import os

# TODO: implement
