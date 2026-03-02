# Challenge 38: Offline dictionary attack on simplified SRP
#
# Simplified SRP (no k multiplier):
#   Client->Server: I, A = pow(g, a, N)
#   Server->Client: salt, B = pow(g, b, N), u (random 128-bit integer)
#   Client: x = SHA256(salt || password), S = pow(B, a + u*x, N), K = SHA256(S)
#   Server: S = pow(A * pow(v, u, N), b, N), K = SHA256(S)
#   Client->Server: HMAC-SHA256(K, salt)
#
# Malicious MITM server attack:
#   The attacker intercepts the exchange and impersonates the server.
#   They choose their own b, B=pow(g,b,N), u, and salt.
#   They observe the client's A and their HMAC.
#
#   Since B and u are attacker-controlled, the client's S simplifies to:
#     S = pow(B, a + u*x, N) = pow(g, b*(a + u*x), N)
#
#   The attacker knows a (they control B=g^b), so:
#     S = pow(A, b, N) * pow(pow(g, x, N), b*u, N)
#       = pow(A * pow(g^x, u, N), b, N)
#
#   For a dictionary word P:
#     x_guess = SHA256(salt || P)
#     v_guess = pow(g, x_guess, N)
#     S_guess = pow(A * pow(v_guess, u, N), b, N)
#     K_guess = SHA256(S_guess)
#     if HMAC-SHA256(K_guess, salt) == observed_HMAC: found password
#
# Task: implement the MITM server and offline dictionary attack.

# TODO: implement simplified SRP and the MITM dictionary attack
