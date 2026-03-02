# Challenge 28: Implement a SHA-1 keyed MAC
#
# A MAC (Message Authentication Code) proves that a message was produced by
# someone with knowledge of the secret key. The simplest construction is a
# secret-prefix MAC: MAC = Hash(key || message).
#
# This challenge has two parts:
#   1. Implement SHA-1 from scratch. Do NOT use hashlib or any library.
#      Reference the FIPS 180-4 spec or a pseudocode description.
#      SHA-1 processes 64-byte (512-bit) blocks and produces a 160-bit (20-byte) digest.
#
#   2. Implement SHA1_MAC(key, message) = SHA1(key || message)
#      and demonstrate:
#        a. Changing the message breaks the MAC.
#        b. Forging a new MAC requires knowing the key.
#
# Note: SHA-1 is broken for collision resistance (see Challenge 55) but that
# is not what is being attacked here. The length extension attack in
# Challenge 29 is the relevant vulnerability for this MAC construction.
# The weakness is structural — secret-prefix MACs are vulnerable to length
# extension regardless of which hash function is used.

# TODO: implement SHA-1 from scratch and SHA1_MAC
