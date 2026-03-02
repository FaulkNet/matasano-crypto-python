# Challenge 41: Implement unpadded message recovery oracle
#
# Unpadded RSA is homomorphic under multiplication: if c = pow(m, e, n),
# then pow(s, e, n) * c mod n decrypts to s*m mod n. This lets an attacker
# recover any previously-seen ciphertext using a fresh query.
#
# The server caches ciphertexts it has already decrypted and refuses to
# decrypt duplicates. This sounds like a defence, but it isn't.
#
# Attack:
#   Given target ciphertext C (for unknown plaintext P):
#   1. Pick random s > 1 (and s < N).
#   2. Compute C' = pow(s, e, n) * C mod n  (a fresh, never-seen ciphertext)
#   3. Submit C' to the server; receive P' = s*P mod n.
#   4. Recover P = P' * modinv(s, n) mod n.
#
# The duplicate-detection defence fails because C' is a completely different
# ciphertext from C. The multiplicative homomorphism of RSA is the root cause.
# OAEP padding breaks this by making the message space non-multiplicative.
#
# Task:
#   Implement a server that decrypts RSA ciphertexts, caches them, and
#   refuses repeats. Implement the attack and recover P without a direct
#   decryption of C.

# TODO: implement the server and unpadded message recovery attack
