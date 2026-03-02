# Challenge 17: The CBC padding oracle
#
# This is widely considered the best-known attack on modern block cipher
# cryptography in widespread use. A "padding oracle" is any system that
# tells you whether a decrypted ciphertext has valid PKCS#7 padding — even
# just an error message that differs between "bad padding" and "bad MAC" is
# enough.
#
# Setup:
#   Function 1 — encrypt():
#     Randomly select one of the 10 strings below, pad it, encrypt with
#     AES-CBC using a random key (saved for Function 2), and return the
#     ciphertext and IV.
#
#   Function 2 — padding_oracle(ciphertext, iv) -> bool:
#     Decrypt the ciphertext and return True if the PKCS#7 padding is valid,
#     False otherwise. Do NOT return the plaintext.
#
# The attack:
#   To decrypt byte N of block B, isolate the last byte of the preceding
#   ciphertext block (C[B-1]). XOR it with guesses 0-255 until the oracle
#   returns True — that means your guess XOR'd with the decrypted byte
#   equals \x01 (valid single-byte padding). Invert to get the plaintext
#   byte. Then work backwards for \x02\x02, \x03\x03\x03, etc.
#
#   Repeat for every block, using the IV as the "preceding block" for the
#   first block.
#
# This attack requires only ~128 oracle queries per byte on average,
# decrypting any CBC ciphertext completely without the key. It was used
# against ASP.NET's ViewState and numerous SSL/TLS implementations.
#
# Plaintexts (base64-encoded — pick one randomly):
PLAINTEXTS = [
    'MDAwMDAwTm93IHRoYXQgdGhlIHBhcnR5IGlzIGp1bXBpbmc=',
    'MDAwMDAxV2l0aCB0aGUgYmFzcyBraWNrZWQgaW4gYW5kIHRoZSBWZWdhJ3MgYXJlIHB1bXBpbicn',
    'MDAwMDAyUXVpY2sgdG8gdGhlIHBvaW50LCB0byB0aGUgcG9pbnQsIG5vIGZha2luZw==',
    'MDAwMDAzQ29va2luZyBNQydzIGxpa2UgYSBwb3VuZCBvZiBiYWNvbg==',
    'MDAwMDA0QnVybmluZyAnZW0sIGlmIHlvdSBhaW4ndCBxdWljayBhbmQgbmltYmxl',
    'MDAwMDA1SSBnbyBjcmF6eSB3aGVuIEkgaGVhciBhIGN5bWJhbA==',
    'MDAwMDA2QW5kIGEgaGlnaCBoYXQgd2l0aCBhIHNvdXBlZCB1cCB0ZW1wbw==',
    'MDAwMDA3SVAgZG93biwgbXkgc3R5bGUncyBsaWtlIGEgY2hlbWljYWwgc3BpbGw=',
    'MDAwMDA4U2Vuc2F0aW9uYWwsIEludGVybmF0aW9uYWw=',
    'MDAwMDA5T3BlcmF0aW9uYWwgYW5kIHdhaXRpbmcgZm9yIHRoZSBuZXh0IGJsb3c=',
]

import os
from base64 import b64decode

# TODO: implement encrypt(), padding_oracle(), and the attack
