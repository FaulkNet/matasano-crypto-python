# Challenge 27: Recover the key from CBC with IV=Key
#
# Some CBC implementations reuse the key as the IV to avoid storing a
# separate IV. This is a serious mistake.
#
# When IV=Key, the following attack recovers the key:
#   1. Encrypt any plaintext P1 || P2 || P3 (three blocks).
#   2. Tamper with the ciphertext: send C1 || 0x00...00 || C1
#      (replace blocks 2 and 3 with zero-block and C1).
#   3. Observe the decrypted output. CBC decryption gives:
#        P'1 = Decrypt(C1) XOR IV  = Decrypt(C1) XOR Key
#        P'2 = Decrypt(0)  XOR C1
#        P'3 = Decrypt(C1) XOR 0   = Decrypt(C1)
#   4. Compute P'1 XOR P'3:
#        [Decrypt(C1) XOR Key] XOR [Decrypt(C1)] = Key
#
# The oracle for this attack is an ASCII compliance check: the receiver
# raises an exception containing the (high-ASCII) decoded bytes if any
# plaintext byte has its high bit set. This leaks P'1 and P'3.
#
# Task:
#   Implement the CBC-with-IV=Key encrypt/decrypt system, implement the
#   attack, and verify you recovered the correct key.

import os

# TODO: implement encrypt, compliant_decrypt (raises on high-ASCII), and key recovery
