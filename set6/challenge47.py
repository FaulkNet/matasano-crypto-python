# Challenge 47: Bleichenbacher's PKCS 1.5 Padding Oracle (Simple Case)
#
# Bleichenbacher 1998 (BB'98): a chosen-ciphertext attack on PKCS#1 v1.5
# padding that was used to attack SSL/TLS for years. The oracle only answers:
# "does this ciphertext decrypt to something starting with 0x00 0x02?"
#
# PKCS#1 v1.5 padding for RSA encryption:
#   00 02 [at least 8 non-zero random bytes] 00 [message]
# A conformant plaintext (2B-conformant) satisfies: 2B <= m < 3B
# where B = 2^(8*(keylen_bytes - 2))  (for 256-bit key: B = 2^(8*30) = 2^240)
#
# The attack:
#   1. Find an s1 such that c * pow(s1, e, n) mod n is conformant (step 2a).
#   2. Given s_i, narrow the interval of possible plaintext values (step 3).
#   3. When one interval remains, find the next s by searching near n/3B (step 2c).
#   4. Repeat until the interval collapses to a single value.
#
# Simple case (Challenge 47): use a 256-bit RSA key (fast) and implement
# steps 2a and 2c only. The full Bleichenbacher includes step 2b for
# multiple intervals, which is Challenge 48.
#
# Task:
#   Generate a 256-bit RSA keypair.
#   PKCS#1.5-pad and encrypt the message "kick it, CC".
#   Implement the oracle and the simple BB'98 attack.

# TODO: implement PKCS1.5 padding, oracle, and Bleichenbacher step 2a/2c/3/4
