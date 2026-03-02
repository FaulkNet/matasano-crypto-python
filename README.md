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

## Crypto Challenge Set 1

The first set covers the fundamentals — encoding, XOR, and frequency analysis. These feel basic but they
underpin every attack in the later sets.

For the full problem set visit the [Cryptopals Website](https://cryptopals.com/sets/1).

| Challenge | Title | Concept |
|-----------|-------|---------|
| [challenge1.py](challenge1.py) | Hex to Base64 | Encoding and byte representation |
| [challenge2.py](challenge2.py) | Fixed XOR | Bitwise XOR on equal-length buffers |
| [challenge3.py](challenge3.py) | Single-byte XOR cipher | Breaking XOR with frequency analysis |
| [challenge4.py](challenge4.py) | Detect single-character XOR | Applying frequency analysis at scale |
| [challenge5.py](challenge5.py) | Repeating-key XOR | The Vigenère cipher at the byte level |

## Running the Challenges

Each challenge is a standalone script. Run any of them with:

```
python challenge1.py
```

Challenge 4 requires `challenge4.txt` (included in this repo) and imports the solver from `challenge3.py`,
so both files must be present in the same directory.
