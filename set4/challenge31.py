# Challenge 31: Implement and break HMAC-SHA1 with an artificial timing leak
#
# HMAC (Hash-based MAC) is the correct way to build a MAC from a hash:
#   HMAC(key, message) = H((key XOR opad) || H((key XOR ipad) || message))
# This construction is immune to length extension attacks.
#
# However, if verification compares bytes one at a time and returns early
# on the first mismatch, the comparison leaks timing information. An
# attacker can determine the correct byte at each position by observing
# which byte value takes the longest to reject — it passed the first N
# bytes of comparison before failing on byte N+1.
#
# Setup:
#   Start a web server (Flask or similar) at localhost:9000.
#   Endpoint: GET /test?file=<filename>&signature=<hex_sig>
#     - Compute HMAC-SHA1 of the file contents with a secret key.
#     - Compare against the provided signature using insecure_compare():
#         compare byte-by-byte, sleep 50ms per byte, return False on mismatch.
#     - Return 200 if valid, 500 if invalid.
#
# The attack:
#   For each byte position 0-19 (HMAC-SHA1 = 20 bytes):
#     Try all 256 values. Time the response for each.
#     The correct byte takes ~50ms longer than the others.
#     Advance to the next position with that byte fixed.
#
# Task:
#   Implement the server and the timing attack client.
#   Recover the correct HMAC for a chosen filename.

# TODO: implement HMAC-SHA1, the timing-vulnerable server, and the attack client
