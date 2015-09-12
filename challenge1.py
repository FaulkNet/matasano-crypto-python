import base64
import binascii

hexString = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
expectedResult = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'


def hex_str_to_base64(string):
    return base64.standard_b64encode(binascii.unhexlify(string)).decode('utf-8')


assert hex_str_to_base64(hexString) == expectedResult
