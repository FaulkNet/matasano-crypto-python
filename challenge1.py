# https://docs.python.org/3/library/binascii.html#binascii.unhexlify
from binascii import hexlify, unhexlify
# https://docs.python.org/3/library/base64.html#base64.b64encode
from base64 import b64encode, b64decode


input: str = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
expectedOutput: str = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'


def hex_to_base64(hexadecimal: bytes):
    raw_bytes: bytes = unhexlify(hexadecimal)
    base64_bytes: bytes = b64encode(raw_bytes)
    return base64_bytes


assert \
    hex_to_base64(input) \
        .decode('utf-8') \
    == expectedOutput
