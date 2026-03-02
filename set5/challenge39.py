# Challenge 39: Implement RSA
#
# RSA key generation:
#   1. Generate two large primes p and q.
#   2. n = p * q  (the modulus)
#   3. et = (p-1) * (q-1)  (Euler's totient)
#   4. e = 3  (common small public exponent — fast but dangerous, see Challenge 40)
#   5. d = modinv(e, et)  (private exponent: e*d ≡ 1 mod et)
#   Public key:  (e, n)
#   Private key: (d, n)
#
# Encryption: c = pow(m, e, n)
# Decryption: m = pow(c, d, n)
#
# The hard part: implementing the extended Euclidean algorithm for modinv.
# EGCD finds integers x, y such that a*x + b*y = gcd(a, b).
# If gcd(e, et) = 1, then e*x ≡ 1 mod et, so x = modinv(e, et).
#
# Python note: Python 3.8+ has pow(e, -1, et) as a built-in modinv.
# Implement it yourself first to understand it, then you can use the
# built-in for convenience in later challenges.
#
# Start with small primes (e.g. p=61, q=53) to verify correctness,
# then scale up to 1024-bit primes.
#
# Task:
#   Implement egcd, modinv, generate_rsa_keypair, rsa_encrypt, rsa_decrypt.
#   Encrypt and decrypt a short string to verify round-trip correctness.

# TODO: implement RSA from scratch
