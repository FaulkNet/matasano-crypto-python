# Challenge 37: Break SRP with a zero key
#
# The SRP server computes the shared secret as:
#   S = pow(A * pow(v, u, N), b, N)
#
# If the client sends A = 0 (or any multiple of N):
#   S = pow(0 * pow(v, u, N), b, N) = pow(0, b, N) = 0
#
# The client also derives S = 0 (for A=0, regardless of the password):
#   S = pow(0 - k*pow(g, x, N), a + u*x, N)
#   = pow(-k*g^x, ..., N)  ... actually for A=0 or A=N the math collapses.
#
# For A = 0:    both sides get S = 0
# For A = N:    A mod N = 0, same result
# For A = 2N:   same
#
# Since S = 0, K = SHA256("0") is known to the attacker. They can compute
# the correct HMAC and authenticate without knowing the password at all.
#
# Task:
#   Using your SRP implementation from Challenge 36, log in to the server
#   by sending A=0 (and then A=N, A=2N) without knowing the password.
#   Verify that is_admin or the equivalent returns True.
#
# Fix: servers must validate that A mod N != 0 before proceeding.

# TODO: attack SRP from Challenge 36 with A=0, A=N, A=2N
