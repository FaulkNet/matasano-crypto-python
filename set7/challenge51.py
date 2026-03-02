# Challenge 51: Compression Ratio Side-Channel Attacks
#
# TLS and other protocols compress data before encrypting it. Compression
# exploits repetition — if your injected string appears elsewhere in the
# plaintext, it compresses better and the ciphertext is shorter.
# Observing ciphertext length leaks information about plaintext content.
#
# Setup:
#   A session cookie is included in every request:
#     "sessionid=TmV2ZXIgcmV2ZWFsIHRoZSBXdSBUYW5nIFNlY3JldCE="  (example)
#   The oracle compresses and encrypts:
#     oracle(payload) -> len(encrypt(compress(format_request(payload))))
#
# Attack (byte-by-byte):
#   To recover byte N of the session ID:
#     Craft payloads ending in "sessionid=" + known_prefix + guess
#     for each possible next character.
#     The payload that produces the shortest ciphertext contains the
#     correct next character (it compressed better because it matched).
#
# Complications:
#   - DEFLATE works at bit granularity; length changes may only appear
#     at byte boundaries. Add padding to force byte alignment.
#   - False positives: multiple candidates may tie. Try adding more
#     padding or using a different prefix to disambiguate.
#
# Part 1: Use a stream cipher (CTR) as the outer encryption.
# Part 2: Repeat with CBC. The padding to block-size creates more noise
#         but the fundamental attack is the same.

# TODO: implement the compression oracle and the byte-by-byte recovery attack
