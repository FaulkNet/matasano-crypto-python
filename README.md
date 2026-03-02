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

## Set 1 — The Basics

The first set covers the fundamentals — encoding, XOR, and frequency analysis. These feel basic but they
underpin every attack in the later sets.

For the full problem set visit the [Cryptopals Set 1 page](https://cryptopals.com/sets/1).

| Challenge | File | Concept |
|-----------|------|---------|
| 1 | [set1/challenge1.py](set1/challenge1.py) | Encoding and byte representation (hex → Base64) |
| 2 | [set1/challenge2.py](set1/challenge2.py) | Bitwise XOR on equal-length buffers |
| 3 | [set1/challenge3.py](set1/challenge3.py) | Breaking single-byte XOR with frequency analysis |
| 4 | [set1/challenge4.py](set1/challenge4.py) | Detecting single-byte XOR across many ciphertexts |
| 5 | [set1/challenge5.py](set1/challenge5.py) | Repeating-key XOR (the Vigenère cipher at the byte level) |

### Running Set 1

Each challenge is a standalone script. Run any of them from the `set1/` directory:

```
cd set1
python challenge1.py
```

Challenge 4 requires `challenge4.txt` (included) and imports the solver from `challenge3.py`,
so both files must be present in the same directory.

---

## Set 2 — Block Crypto *(coming soon)*

Set 2 moves into block ciphers and is where things start to get serious. The challenges build up from
a padding scheme through full CBC mode and then tear it all back down through a sequence of increasingly
powerful attacks.

For the full problem set visit the [Cryptopals Set 2 page](https://cryptopals.com/sets/2).

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

The stub files are in place with full problem descriptions. Solutions coming soon.
