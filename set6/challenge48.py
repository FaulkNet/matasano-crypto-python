# Challenge 48: Bleichenbacher's PKCS 1.5 Padding Oracle (Complete Case)
#
# The complete BB'98 attack, now with a 768-bit RSA key.
# This is the version that "routinely breaks SSL/TLS."
#
# Adds step 2b to Challenge 47: when there are multiple disjoint intervals
# in the solution set (M_i), you must search for s values that reduce
# at least one of them, rather than only focusing on a single interval.
#
# Full algorithm:
#   Blinding (step 1): find s0 such that c0 = c * pow(s0, e, n) is conformant.
#     (If c is already conformant, s0 = 1.)
#
#   Step 2a: find smallest s1 >= n/(3B) such that oracle(c0 * pow(s1,e,n)) is True.
#   Step 2b: if multiple intervals, search s_i = s_{i-1} + 1 upward.
#   Step 2c: if one interval [a, b], search using:
#     r_i >= 2*(b*s_{i-1} - 2B) / n  (rounded up)
#     s_i in range(ceil((2B+r_i*n)/b), floor((3B+r_i*n)/a) + 1)
#
#   Step 3: narrow intervals with each new conformant s_i.
#   Step 4: if M_i = {[a,a]}, plaintext = a * modinv(s0, n) mod n.
#
# Task:
#   Generate a 768-bit RSA keypair.
#   Encrypt "kick it, CC" with PKCS#1.5 padding.
#   Implement and run the complete BB'98 attack.
#   This will be slow — hundreds of thousands of oracle queries for 768 bits.

# TODO: implement complete BB'98 (extends Challenge 47 with step 2b and larger key)
