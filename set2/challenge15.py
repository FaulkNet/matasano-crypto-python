# Challenge 15: PKCS#7 padding validation
#
# In Challenge 9 we added PKCS#7 padding. Now we validate and strip it.
# This sounds simple but getting it wrong is the root cause of padding
# oracle attacks — one of the most powerful and widely-exploited attacks
# against real-world CBC implementations (see Challenge 17 in Set 3).
#
# Rules for valid PKCS#7 padding:
#   - The last byte N indicates the number of padding bytes.
#   - The final N bytes must all equal N.
#   - N must be between 1 and the block size (inclusive).
#   - A full block of padding (e.g. 16 bytes of \x10) is valid.
#
# Valid:
#   b'ICE ICE BABY\x04\x04\x04\x04'  ->  b'ICE ICE BABY'
#
# Invalid (raise an exception):
#   b'ICE ICE BABY\x05\x05\x05\x05'  ->  padding byte is 5 but only 4 present
#   b'ICE ICE BABY\x01\x02\x03\x04'  ->  bytes don't all match the last byte
#
# Task:
#   Implement pkcs7_unpad(data: bytes) -> bytes
#   Raise a ValueError (with a descriptive message) for invalid padding.

# TODO: implement


assert pkcs7_unpad(b'ICE ICE BABY\x04\x04\x04\x04') == b'ICE ICE BABY'

try:
    pkcs7_unpad(b'ICE ICE BABY\x05\x05\x05\x05')
    assert False, 'should have raised'
except ValueError:
    pass

try:
    pkcs7_unpad(b'ICE ICE BABY\x01\x02\x03\x04')
    assert False, 'should have raised'
except ValueError:
    pass

print('challenge15: OK')
