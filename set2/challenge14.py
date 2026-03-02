# Challenge 14: Byte-at-a-time ECB decryption (Harder)
#
# This is Challenge 12 with a twist: the oracle now prepends a random-length
# random byte string to your input before appending the secret and encrypting.
#
#   AES-128-ECB(random_prefix || your_input || secret_string, consistent_key)
#
# The prefix is fixed for the lifetime of the oracle (same bytes every call)
# but you don't know its length. This throws off the block alignment that
# Challenge 12 depended on.
#
# Strategy:
#   First, determine how long the random prefix is. Feed the oracle varying
#   amounts of your chosen byte (the "stimulus") and watch the ciphertext
#   response. When you've added enough padding to push the prefix to the end
#   of a complete block, the blocks containing your padding will become stable
#   across calls — those are your landmark. Everything before them is the
#   prefix; everything after is your controlled territory.
#
#   Once you know the prefix length (and how many bytes to add to align it),
#   the rest of the attack is identical to Challenge 12, just offset by the
#   prefix blocks.
#
# Task:
#   Implement the harder oracle (with random prefix) and the full attack.
#   Print the recovered secret string.

import os
from base64 import b64decode

SECRET: bytes = b64decode(
    'Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkg'
    'aGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBq'
    'dXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3AgTm8ganVzdCBkcm92ZSBieQo='
)

# TODO: implement oracle (with random prefix) and attack
