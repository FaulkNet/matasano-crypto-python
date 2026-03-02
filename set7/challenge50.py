# Challenge 50: Hashing with CBC-MAC
#
# CBC-MAC is sometimes misused as a hash function (with a known key or no
# key). This challenge demonstrates collision attacks against it.
#
# The target:
#   A JavaScript snippet is "authenticated" with CBC-MAC:
#     alert('MZA who was that?');
#   Key: "YELLOW SUBMARINE", IV: 0
#   Known CBC-MAC: 296b8d7cb78a243dda4d0a61d33bbdd1
#
# Forge a new JavaScript snippet that:
#   1. Alerts a different message: alert('Ayo, the Wu is back!');
#   2. Produces the same CBC-MAC: 296b8d7cb78a243dda4d0a61d33bbdd1
#   3. Is valid, runnable JavaScript.
#
# Attack (CBC-MAC length extension):
#   Let T = CBC-MAC(key, 0, original_message).
#   Any message starting with original_message || padding || block
#   where block = T XOR first_block_of_extension will produce a CBC-MAC
#   equal to CBC-MAC(key, 0, extension) — which you can freely choose.
#
#   So: construct your forged message as:
#     alert('MZA who was that?');
#     [padding to block boundary as JS comment]
#     [glue block = T XOR first_block_of("alert('Ayo...');\n")]
#     alert('Ayo, the Wu is back!');
#
# Task: implement the forgery and verify the MAC matches.

KEY: bytes = b'YELLOW SUBMARINE'
ORIGINAL: bytes = b"alert('MZA who was that?');\n"
TARGET_MAC: str = '296b8d7cb78a243dda4d0a61d33bbdd1'

# TODO: implement the length extension forgery
