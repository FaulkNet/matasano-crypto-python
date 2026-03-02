# Challenge 33: Implement Diffie-Hellman
#
# Diffie-Hellman (DH) is the foundational public-key key-exchange protocol.
# Two parties agree on public parameters (p, g), each generates a private
# key, exchanges public keys, and independently arrives at the same shared
# secret — without ever transmitting that secret.
#
# Math:
#   Private keys: a, b  (random integers < p)
#   Public keys:  A = g^a mod p,  B = g^b mod p
#   Shared secret: s = B^a mod p = A^b mod p  (because (g^b)^a = (g^a)^b mod p)
#
# Phase 1 — toy parameters:
#   p = 37, g = 5
#   Verify that both parties compute the same s.
#
# Phase 2 — real parameters (NIST 1536-bit group):
#   p = 0xffffffffffffffffc90fdaa22168c234c4c6628b80dc1cd129024e088a67cc74
#       020bbea63b139b22514a08798e3404ddef9519b3cd3a431b302b0a6df25f1437
#       4fe1356d6d51c245e485b576625e7ec6f44c42e9a637ed6b0bff5cb6f406b7ed
#       ee386bfb5a899fa5ae9f24117c4b1fe649286651ece45b3dc2007cb8a163bf05
#       98da48361c55d39a69163fa8fd24cf5f83655d23dca3ad961c62f356208552bb
#       9ed529077096966d670c354e4abc9804f1746c08ca237327ffffffffffffffff
#   g = 2
#   You MUST use modular exponentiation (pow(base, exp, mod) in Python).
#   Standard ** will overflow — these numbers are huge.
#   Hash s with SHA-256 and use the first 16 bytes as an AES key.

# NIST parameters
p = 0xffffffffffffffffc90fdaa22168c234c4c6628b80dc1cd129024e088a67cc74020bbea63b139b22514a08798e3404ddef9519b3cd3a431b302b0a6df25f14374fe1356d6d51c245e485b576625e7ec6f44c42e9a637ed6b0bff5cb6f406b7edee386bfb5a899fa5ae9f24117c4b1fe649286651ece45b3dc2007cb8a163bf0598da48361c55d39a69163fa8fd24cf5f83655d23dca3ad961c62f356208552bb9ed529077096966d670c354e4abc9804f1746c08ca237327ffffffffffffffff
g = 2

# TODO: implement DH key exchange and verify both parties get the same shared secret
