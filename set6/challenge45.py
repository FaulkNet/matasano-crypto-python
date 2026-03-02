# Challenge 45: DSA parameter tampering
#
# DSA signature verification checks: pow(g, H(m)/s, p)*pow(y, r/s, p) mod p mod q == r
# This breaks completely when g is chosen maliciously.
#
# Attack 1: g = 0 (mod p)
#   r = pow(0, k, p) mod q = 0
#   Any signature (r=0, s=anything) trivially verifies as 0==0.
#   But most implementations reject r=0 or s=0 as invalid, so this
#   is usually caught. Still worth demonstrating.
#
# Attack 2: g = p + 1  (so g ≡ 1 mod p)
#   pow(g, x, p) = pow(1, x, p) = 1 for ALL x.
#   So y = pow(g, x, p) = 1 (the public key is always 1).
#
#   Magic signature for ANY message m:
#     z = any value (e.g. 1)
#     r = pow(y, z, p) mod q  = pow(1, z, p) mod q = 1 mod q = 1
#     s = r * modinv(z, q) mod q
#
#   Verify: pow(g, H(m)/s, p) * pow(y, r/s, p) mod p mod q
#         = pow(1, ...) * pow(1, ...) mod p mod q = 1 = r ✓
#
# Task:
#   Use g=p+1 to forge signatures for "Hello, world" AND "Goodbye, world"
#   using the same (r, s) pair. Both should verify under the same public key.

# TODO: generate DSA parameters with g=p+1, generate magic signature, verify on two messages
