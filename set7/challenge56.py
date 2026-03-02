# Challenge 56: RC4 Single-Byte Biases
#
# RC4 has well-known statistical biases in its keystream. The second byte
# of the keystream is biased toward 0 with probability ~2/256, and bytes
# at positions 16 and 32 show strong biases toward specific values.
#
# Attack:
#   The cookie: base64-decode QkUgU1VSRSBUTyBEUklOSyBZT1VSIE9WQUxUSU5F
#   (Don't decode it manually — decode it in code.)
#
#   Build an oracle: oracle(request) = RC4(request || cookie, random_key)
#   A new random key is generated for each call.
#
#   To recover cookie byte at position P:
#     Prefix your request with (15 - P % 16) bytes, so cookie[P] lands
#     at ciphertext position 15 (biased toward 0) or 31 (next bias).
#     Collect ~2^24 oracle outputs (many calls).
#     Find which plaintext byte value c makes keystream byte K satisfy
#     ciphertext[15] = c XOR K most often — the bias toward a specific
#     K value tells you which c is correct.
#
#   Actually use positions 15 and 31 (z[16] and z[32] in 1-indexed RC4
#   output) which show the strongest biases documented in AlFardan et al.
#
# Task:
#   Implement RC4, the oracle, and the statistical recovery attack.
#   Recover the full cookie.

from base64 import b64decode

COOKIE: bytes = b64decode('QkUgU1VSRSBUTyBEUklOSyBZT1VSIE9WQUxUSU5F')

# TODO: implement RC4, build oracle, run bias-based recovery attack
