# Challenge 40: Implement an E=3 RSA Broadcast attack
#
# If the same plaintext m is encrypted under three different RSA public keys
# all with exponent e=3, an attacker can recover m without breaking RSA.
#
# Why: by the Chinese Remainder Theorem (CRT), given:
#   c0 = pow(m, 3, n0)
#   c1 = pow(m, 3, n1)
#   c2 = pow(m, 3, n2)
#
# You can reconstruct x ≡ m^3 (mod n0*n1*n2).
# If m < min(n0, n1, n2) (likely for short plaintexts), then
# m^3 < n0*n1*n2, so m^3 was never reduced by the modulus.
# Therefore m = integer_cube_root(x) exactly.
#
# CRT reconstruction:
#   ms0 = n1 * n2;  ms1 = n0 * n2;  ms2 = n0 * n1
#   r = (c0 * ms0 * modinv(ms0, n0)
#      + c1 * ms1 * modinv(ms1, n1)
#      + c2 * ms2 * modinv(ms2, n2)) % (n0 * n1 * n2)
#
# Then m = integer cube root of r (use binary search or Newton's method).
#
# Task:
#   Generate three RSA keypairs with e=3.
#   Encrypt the same message under all three.
#   Recover the message using CRT + cube root.
#
# Lesson: small exponents are dangerous when the same message reaches
# multiple recipients. OAEP padding prevents this by randomising the
# plaintext before encryption.

# TODO: implement CRT reconstruction and integer cube root, then run the attack
