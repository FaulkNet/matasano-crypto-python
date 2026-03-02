from challenge3 import get_max_single_char_xor

# Challenge 4: Detect single-character XOR
#
# challenge4.txt contains 326 hex-encoded strings. Exactly one of them has
# been encrypted with single-byte XOR. The goal is to find it.
#
# This challenge extends Challenge 3 by making us search across many
# ciphertexts rather than just one. It demonstrates that frequency analysis
# scales: even when the signal is buried among hundreds of decoys, the
# correctly decrypted plaintext stands out clearly from the noise because
# English text scores so much higher than garbage bytes.
#
# In practice this mirrors real-world scenarios where an attacker must
# identify which of many intercepted messages is encrypted and with what
# scheme — the statistical signature of English leaks through simple XOR
# regardless of how many red herrings surround it.

results: list = []
with open('challenge4.txt', 'r') as f:
    for line in f.readlines():
        stripped: str = line.strip()
        if stripped:
            results.append(get_max_single_char_xor(stripped))

print(max(results, key=lambda x: x[0]))
