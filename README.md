Matasano Crypto Python
======================

A project to bring a set of [Cryptopals](https://cryptopals.com) challenge solutions up to Python 3.

## About the Cryptopals Challenges

The Cryptopals Crypto Challenges (originally published by Matasano Security) are a series of hands-on
programming exercises designed to teach real-world cryptography by breaking it. Rather than presenting
crypto as a black box of safe primitives, Cryptopals walks you through constructing and then dismantling
classic and modern schemes — XOR ciphers, block cipher modes, stream ciphers, MACs, and more.

The philosophy is simple: you don't truly understand why a cryptographic primitive is secure until you've
exploited a broken version of it. Each challenge builds on the last, and by the end of a set you've
implemented attacks that have appeared in real vulnerabilities against real protocols.

## About This Repository

The original solutions were written in Python 2. This project translates them to idiomatic Python 3,
fixing any incompatibilities along the way (byte string handling being the main offender — Python 3 draws
a hard line between `str` and `bytes` that catches a lot of sloppy crypto code). Where the originals had
bugs, those are fixed too. Each challenge is also documented with an explanation of the underlying concept
it demonstrates.

---

## Set 1 — The Basics ✓

Encoding, XOR, and frequency analysis. These feel basic but underpin every attack in the later sets.

[Cryptopals Set 1](https://cryptopals.com/sets/1)

| Challenge | File | Concept |
|-----------|------|---------|
| 1 | [set1/challenge1.py](set1/challenge1.py) | Encoding and byte representation (hex → Base64) |
| 2 | [set1/challenge2.py](set1/challenge2.py) | Bitwise XOR on equal-length buffers |
| 3 | [set1/challenge3.py](set1/challenge3.py) | Breaking single-byte XOR with frequency analysis |
| 4 | [set1/challenge4.py](set1/challenge4.py) | Detecting single-byte XOR across many ciphertexts |
| 5 | [set1/challenge5.py](set1/challenge5.py) | Repeating-key XOR (the Vigenère cipher at the byte level) |

Run from the `set1/` directory: `python challenge1.py`

---

## Set 2 — Block Crypto *(coming soon)*

Block cipher fundamentals and the first real attacks — ECB pattern detection, byte-at-a-time decryption, padding oracles, and CBC bitflipping.

[Cryptopals Set 2](https://cryptopals.com/sets/2)

| Challenge | File | Concept |
|-----------|------|---------|
| 9  | [set2/challenge9.py](set2/challenge9.py)   | PKCS#7 padding |
| 10 | [set2/challenge10.py](set2/challenge10.py) | Implement CBC mode from scratch |
| 11 | [set2/challenge11.py](set2/challenge11.py) | ECB/CBC detection oracle |
| 12 | [set2/challenge12.py](set2/challenge12.py) | Byte-at-a-time ECB decryption (simple) |
| 13 | [set2/challenge13.py](set2/challenge13.py) | ECB cut-and-paste forgery |
| 14 | [set2/challenge14.py](set2/challenge14.py) | Byte-at-a-time ECB decryption (harder) |
| 15 | [set2/challenge15.py](set2/challenge15.py) | PKCS#7 padding validation |
| 16 | [set2/challenge16.py](set2/challenge16.py) | CBC bitflipping attack |

---

## Set 3 — Block & Stream Crypto *(coming soon)*

The CBC padding oracle (one of the most powerful real-world attacks), CTR mode, and breaking the Mersenne Twister RNG.

[Cryptopals Set 3](https://cryptopals.com/sets/3)

| Challenge | File | Concept |
|-----------|------|---------|
| 17 | [set3/challenge17.py](set3/challenge17.py) | CBC padding oracle attack |
| 18 | [set3/challenge18.py](set3/challenge18.py) | AES-CTR stream cipher mode |
| 19 | [set3/challenge19.py](set3/challenge19.py) | Break fixed-nonce CTR (substitutions) |
| 20 | [set3/challenge20.py](set3/challenge20.py) | Break fixed-nonce CTR (statistical) |
| 21 | [set3/challenge21.py](set3/challenge21.py) | Implement MT19937 Mersenne Twister |
| 22 | [set3/challenge22.py](set3/challenge22.py) | Crack an MT19937 seed |
| 23 | [set3/challenge23.py](set3/challenge23.py) | Clone MT19937 from its output |
| 24 | [set3/challenge24.py](set3/challenge24.py) | MT19937 stream cipher and crack it |

---

## Set 4 — Stream Crypto & Randomness *(coming soon)*

CTR attacks, length extension attacks on SHA-1 and MD4, and timing attacks on HMAC.

[Cryptopals Set 4](https://cryptopals.com/sets/4)

| Challenge | File | Concept |
|-----------|------|---------|
| 25 | [set4/challenge25.py](set4/challenge25.py) | Break CTR with random-access edit oracle |
| 26 | [set4/challenge26.py](set4/challenge26.py) | CTR bitflipping attack |
| 27 | [set4/challenge27.py](set4/challenge27.py) | Recover key from CBC with IV=Key |
| 28 | [set4/challenge28.py](set4/challenge28.py) | Implement SHA-1 keyed MAC |
| 29 | [set4/challenge29.py](set4/challenge29.py) | SHA-1 length extension attack |
| 30 | [set4/challenge30.py](set4/challenge30.py) | MD4 length extension attack |
| 31 | [set4/challenge31.py](set4/challenge31.py) | HMAC timing attack (50ms leak) |
| 32 | [set4/challenge32.py](set4/challenge32.py) | HMAC timing attack (5ms leak, statistical) |

---

## Set 5 — Diffie-Hellman and Friends *(coming soon)*

Number-theoretic cryptography: DH key exchange, MITM parameter injection, SRP, and RSA.

[Cryptopals Set 5](https://cryptopals.com/sets/5)

| Challenge | File | Concept |
|-----------|------|---------|
| 33 | [set5/challenge33.py](set5/challenge33.py) | Implement Diffie-Hellman |
| 34 | [set5/challenge34.py](set5/challenge34.py) | DH MITM key-fixing attack |
| 35 | [set5/challenge35.py](set5/challenge35.py) | DH malicious g parameter attack |
| 36 | [set5/challenge36.py](set5/challenge36.py) | Implement SRP |
| 37 | [set5/challenge37.py](set5/challenge37.py) | Break SRP with zero key |
| 38 | [set5/challenge38.py](set5/challenge38.py) | Simplified SRP offline dictionary attack |
| 39 | [set5/challenge39.py](set5/challenge39.py) | Implement RSA |
| 40 | [set5/challenge40.py](set5/challenge40.py) | E=3 RSA broadcast attack |

---

## Set 6 — RSA and DSA *(coming soon)*

RSA homomorphic attacks, signature forgery, DSA nonce recovery, and Bleichenbacher's padding oracle.

[Cryptopals Set 6](https://cryptopals.com/sets/6)

| Challenge | File | Concept |
|-----------|------|---------|
| 41 | [set6/challenge41.py](set6/challenge41.py) | Unpadded RSA message recovery oracle |
| 42 | [set6/challenge42.py](set6/challenge42.py) | Bleichenbacher's e=3 RSA signature forgery |
| 43 | [set6/challenge43.py](set6/challenge43.py) | DSA key recovery from weak nonce |
| 44 | [set6/challenge44.py](set6/challenge44.py) | DSA key recovery from repeated nonce |
| 45 | [set6/challenge45.py](set6/challenge45.py) | DSA parameter tampering |
| 46 | [set6/challenge46.py](set6/challenge46.py) | RSA parity oracle |
| 47 | [set6/challenge47.py](set6/challenge47.py) | Bleichenbacher PKCS 1.5 oracle (simple) |
| 48 | [set6/challenge48.py](set6/challenge48.py) | Bleichenbacher PKCS 1.5 oracle (complete) |

---

## Set 7 — Hashes *(coming soon)*

CBC-MAC forgery, compression side-channels, hash multicollisions, MD4 differential cryptanalysis, and RC4 bias attacks.

[Cryptopals Set 7](https://cryptopals.com/sets/7)

| Challenge | File | Concept |
|-----------|------|---------|
| 49 | [set7/challenge49.py](set7/challenge49.py) | CBC-MAC message forgery |
| 50 | [set7/challenge50.py](set7/challenge50.py) | Hashing with CBC-MAC |
| 51 | [set7/challenge51.py](set7/challenge51.py) | Compression ratio side-channel attack |
| 52 | [set7/challenge52.py](set7/challenge52.py) | Iterated hash multicollisions |
| 53 | [set7/challenge53.py](set7/challenge53.py) | Kelsey-Schneier expandable messages |
| 54 | [set7/challenge54.py](set7/challenge54.py) | Kelsey-Kohno Nostradamus attack |
| 55 | [set7/challenge55.py](set7/challenge55.py) | MD4 differential collision attack |
| 56 | [set7/challenge56.py](set7/challenge56.py) | RC4 single-byte bias attack |

---

## Set 8 — Abstract Algebra *(access required)*

Elliptic curve cryptography, GCM attacks, and advanced DH attacks. Set 8 is not publicly available —
access is granted by the Cryptopals authors to participants who complete Sets 1-7.

See [set8/README.md](set8/README.md) for the challenge list.
