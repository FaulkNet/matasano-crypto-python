from itertools import cycle

# Challenge 5: Implement repeating-key XOR
#
# XOR the plaintext against a repeating key — here 'ICE' cycling over and
# over — and encode the result as a hex string.
#
# This is the Vigenère cipher applied at the byte level. It is far stronger
# than single-byte XOR because the key is longer, but it is still broken by
# the same core idea: if the key repeats, bytes at the same position modulo
# the key length share the same key byte and can be attacked as independent
# single-byte XOR problems. Knowing the key length (via Hamming distance
# analysis, covered in Challenge 6) reduces a repeating-key XOR cipher
# to several simultaneous instances of Challenge 3.
#
# Most real stream ciphers are conceptually this pattern with a much more
# complex key stream — which is exactly why key reuse is fatal in protocols
# like RC4 and why nonces must never repeat in AES-CTR mode.

s = '''Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal'''
key = 'ICE'
expected = (
    '0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272'
    'a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f'
)

out = ''.join(['{:02x}'.format((ord(c) ^ ord(k))) for c, k in zip(s, cycle(key))])

assert out == expected
