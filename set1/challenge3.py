# https://docs.python.org/3/library/binascii.html#binascii.unhexlify
from binascii import unhexlify

# Challenge 3: Single-byte XOR cipher
#
# The ciphertext below has been XOR'd against a single character (one byte).
# The goal is to recover the key and decrypt the message.
#
# This challenge introduces frequency analysis — the idea that English
# plaintext has a predictable distribution of characters (lots of letters,
# spaces, punctuation). By trying all 256 possible key bytes and scoring
# each candidate decryption, we can identify the most likely plaintext
# without knowing the key in advance.
#
# This is the fundamental attack against any cipher that reuses key material
# and is why one-time pads must never repeat their keys.

ciphertext: str = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'


def score_plaintext(s: str) -> float:
    """Score a string by the proportion of alphabetic characters it contains.

    English plaintext scores high because it is mostly letters. Random bytes
    or garbage output from a wrong key will score low.
    """
    letter_count: int = sum(1 for c in s if 'a' <= c <= 'z' or 'A' <= c <= 'Z' or c == ' ')
    return letter_count / len(s)


def get_max_single_char_xor(hex_string: str) -> list:
    """Try all 256 possible single-byte keys against a hex-encoded ciphertext.

    XORs each byte of the ciphertext against every possible key byte (0-255),
    scores the resulting plaintext using letter frequency, and returns the
    highest-scoring [score, plaintext] pair.
    """
    raw_bytes: bytes = unhexlify(hex_string)
    results: list = []
    for key_byte in range(256):
        plaintext: str = ''.join(chr(b ^ key_byte) for b in raw_bytes)
        results.append([score_plaintext(plaintext), plaintext])
    return max(results, key=lambda x: x[0])


if __name__ == '__main__':
    print(get_max_single_char_xor(ciphertext))
