# Challenge 29: Break a SHA-1 keyed MAC using length extension
#
# SHA-1 (like all Merkle-Damgård hashes) is vulnerable to length extension.
# Given Hash(key || message) and len(key || message), you can compute
# Hash(key || message || glue_padding || extension) for any extension,
# without knowing the key.
#
# Why: the hash output IS the internal state after processing all blocks.
# You can resume hashing from that state, processing new blocks, and the
# result is a valid hash of key || message || glue_padding || extension.
#
# Glue padding is the standard SHA-1 padding appended to key || message:
#   \x80 followed by zeros, then a big-endian 64-bit bit-count,
#   padded to a 64-byte block boundary.
#
# Attack:
#   Given:
#     original_message = "comment1=cooking%20MCs;userdata=foo;comment2=%20like%20a%20pound%20of%20bacon"
#     original_mac = SHA1_MAC(unknown_key, original_message)
#
#   Forge a valid MAC for:
#     original_message || glue_padding || ";admin=true"
#
#   Steps:
#     1. Compute glue_padding for (guessed_key_len + len(original_message)) bytes.
#     2. Set SHA-1's initial state to the five 32-bit words from original_mac.
#     3. Set the initial byte count to len(key || message || glue_padding).
#     4. Hash ";admin=true" from that state.
#     5. Verify the forged MAC validates correctly.
#     6. Try key lengths 1-32 until one works.

# TODO: implement the length extension attack against SHA1_MAC from Challenge 28
