# Challenge 36: Implement Secure Remote Password (SRP)
#
# SRP combines DH with password-based authentication. The server never
# stores the password — only a verifier v = g^x mod N where x = H(salt|password).
# Even if the database is stolen, an attacker can't log in without the password.
#
# Parameters: N (same NIST prime as Challenge 33), g = 2, k = 3
#
# Registration (server):
#   salt = random bytes
#   x    = SHA256(salt || password) as integer
#   v    = pow(g, x, N)
#   store: (identity, salt, v)
#
# Login:
#   Client->Server: I (identity), A = pow(g, a, N)  [a = random]
#   Server->Client: salt, B = (k*v + pow(g, b, N)) % N  [b = random]
#
#   Both compute:
#     uH = SHA256(str(A) + str(B));  u = int(uH, 16)
#
#   Client computes:
#     x = int(SHA256(salt || password), 16)
#     S = pow(B - k*pow(g, x, N), a + u*x, N)
#     K = SHA256(str(S))
#
#   Server computes:
#     S = pow(A * pow(v, u, N), b, N)
#     K = SHA256(str(S))
#
#   Client->Server: HMAC-SHA256(K, salt)
#   Server verifies HMAC matches its own computation.
#
# Task: implement the full SRP protocol between a client and server.

# NIST prime (same as Challenge 33)
N = 0xffffffffffffffffc90fdaa22168c234c4c6628b80dc1cd129024e088a67cc74020bbea63b139b22514a08798e3404ddef9519b3cd3a431b302b0a6df25f14374fe1356d6d51c245e485b576625e7ec6f44c42e9a637ed6b0bff5cb6f406b7edee386bfb5a899fa5ae9f24117c4b1fe649286651ece45b3dc2007cb8a163bf0598da48361c55d39a69163fa8fd24cf5f83655d23dca3ad961c62f356208552bb9ed529077096966d670c354e4abc9804f1746c08ca237327ffffffffffffffff
g = 2
k = 3

# TODO: implement SRP client and server
