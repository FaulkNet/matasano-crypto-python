# Challenge 34: Implement a MITM key-fixing attack on Diffie-Hellman
#
# A man-in-the-middle who can intercept and modify DH messages can force
# both parties to derive a known shared secret by substituting p for their
# public keys.
#
# Why it works:
#   Normal shared secret: s = B^a mod p
#   If attacker substitutes B = p:  s = p^a mod p = 0  (p mod p = 0)
#   Same for A: if attacker sends p to B, B computes p^b mod p = 0
#   Both sides derive s = 0, so the AES key = SHA1(0)[0:16] is known to M.
#
# Protocol to implement:
#   A->M: (p, g, A)    M->B: (p, g, p)   [replaces A with p]
#   B->M: B            M->A: p            [replaces B with p]
#   A->M: AES_CBC(SHA1(s)[0:16], msg, iv)
#   M decrypts with key=SHA1(0)[0:16], re-encrypts, forwards to B.
#
# Task:
#   Simulate A, B, and M as functions or classes. Have A send a message
#   to B through M. Verify M can read (and re-encrypt) every message.
#
# This attack motivated the development of authenticated key exchange (e.g.
# certificates, SRP) — unauthenticated DH is vulnerable to this MITM.

# TODO: implement A, B, and the MITM M
