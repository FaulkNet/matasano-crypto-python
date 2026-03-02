# Challenge 30: Break an MD4 keyed MAC using length extension
#
# Identical attack to Challenge 29, but against MD4 instead of SHA-1.
#
# MD4 differences from SHA-1:
#   - 128-bit output (four 32-bit state words: A, B, C, D)
#   - Little-endian (SHA-1 is big-endian) — critical for state extraction
#     and for encoding the bit-length in the padding
#   - 64-byte blocks (same as SHA-1)
#   - Padding: \x80, zeros, then 64-bit LE bit-count to reach 64-byte boundary
#
# You'll need to implement MD4 from scratch (do not use any library).
# Pseudocode is readily available. The attack is structurally the same as
# Challenge 29: extract the four state words from the known MAC output,
# resume hashing your extension message from that state with the correct
# byte count, and produce a forged MAC.
#
# Historical note: MD4 was broken for collision resistance by Wang et al
# in 2004 (see Challenge 55 for MD4 collisions). It should never be used.

# TODO: implement MD4 from scratch and the length extension attack
