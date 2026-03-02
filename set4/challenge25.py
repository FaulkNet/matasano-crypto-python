# Challenge 25: Break "random access read/write" AES CTR
#
# CTR mode supports random access: to edit byte N of the ciphertext, just
# re-encrypt the plaintext at that position with the same keystream byte.
# This "edit" capability turns out to be a devastating oracle.
#
# Setup:
#   1. Decrypt challenge25.txt (AES-ECB with key "YELLOW SUBMARINE") to get
#      the plaintext.
#   2. Re-encrypt it under AES-CTR with a random key.
#   3. Expose this function:
#        edit(ciphertext, key, offset, newtext) -> new_ciphertext
#      which decrypts, splices in newtext at offset, and re-encrypts.
#
# The attack:
#   Call edit(ciphertext, key, 0, ciphertext) — i.e. "overwrite" the
#   entire plaintext with the ciphertext itself.
#   The result is: AES_CTR(ciphertext, key) = ciphertext XOR keystream.
#   But the original ciphertext is also plaintext XOR keystream.
#   So: result XOR ciphertext = keystream, and keystream XOR ciphertext
#   = plaintext. One more XOR and you have the original plaintext.
#
# This shows that any encryption scheme allowing the encryptor to be used
# as an edit oracle leaks the plaintext — even without knowing the key.
#
# Data file: challenge25.txt (Base64-encoded AES-ECB ciphertext, key "YELLOW SUBMARINE")

from base64 import b64decode

KEY_ECB: bytes = b'YELLOW SUBMARINE'

with open('challenge25.txt', 'r') as f:
    ecb_ciphertext: bytes = b64decode(f.read())

# TODO: decrypt ECB ciphertext, re-encrypt with CTR, implement edit oracle, run attack
