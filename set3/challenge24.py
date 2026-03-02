# Challenge 24: Create the MT19937 stream cipher and break it
#
# Part 1: MT19937 stream cipher
#   Build a stream cipher using MT19937 as the keystream generator.
#   Use a 16-bit seed (i.e. the key is a number 0-65535).
#   To generate keystream bytes: call extract_number() repeatedly and
#   use each 32-bit output as 4 keystream bytes.
#
#   Given a ciphertext that ends with 14 known 'A' bytes (preceded by
#   random unknown bytes), recover the 16-bit seed by brute force.
#   There are only 65,536 possible seeds — try them all.
#
# Part 2: Password reset token detection
#   Generate a "password reset token" by seeding MT19937 with the current
#   Unix timestamp and producing some output (e.g. 16 bytes).
#
#   Write a function that takes a token and determines whether it was likely
#   generated this way (i.e. the seed is a timestamp close to now).
#
#   Strategy: try all recent timestamps as seeds and check if any produce
#   a matching token. The window only needs to be a few thousand seconds wide.
#
# Key takeaway: PRNGs seeded with timestamps or short keys are trivially
# broken. Never use MT19937 (or any non-CSPRNG) for security-sensitive
# random values like tokens, IVs, or keys.

import time

# TODO: implement MT19937 stream cipher, brute-force cracker, and token detector
