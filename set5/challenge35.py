# Challenge 35: Implement DH with negotiated groups, and break with malicious g
#
# Some DH implementations allow the client to propose g. A MITM can exploit
# this by substituting a malicious generator.
#
# Three attack scenarios with different g values:
#
#   g = 1:
#     A = 1^a mod p = 1  and  B = 1^b mod p = 1
#     s = 1^b mod p = 1  and  s = 1^a mod p = 1
#     Both sides always get s = 1. AES key is known.
#
#   g = p:
#     A = p^a mod p = 0  and  B = p^b mod p = 0
#     s = 0. AES key is known.
#
#   g = p-1:
#     (p-1)^a mod p is either 1 (if a is even) or p-1 (if a is odd).
#     So s is either 1 or p-1. Try both keys to decrypt.
#
# Protocol: A proposes (p, g) to B via M, who substitutes g.
# A and B then exchange public keys (which M can leave unchanged).
# M knows s and can read all encrypted traffic.
#
# Task:
#   Implement all three g-substitution attacks and verify M can decrypt.
#   This is why protocols fix the group parameters out-of-band (e.g. in
#   the TLS spec) rather than allowing negotiation.

# TODO: implement the three MITM attacks with g=1, g=p, and g=p-1
