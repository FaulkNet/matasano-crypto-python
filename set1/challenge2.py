# https://docs.python.org/3/library/binascii.html#binascii.unhexlify
from binascii import hexlify, unhexlify


a: str = '1c0111001f010100061a024b53535009181c'  # (cypher text)
b: str = '686974207468652062756c6c277320657965'  # hit the bull's eye (key)
c: str = '746865206b696420646f6e277420706c6179'  # the kid don't play


def bitwise_xor(x_raw_bytes: bytes, y_raw_bytes: bytes):
    octet_tuples: zip[tuple[str, str]] = \
        zip(
            x_raw_bytes,
            y_raw_bytes
        )
    xored_octets: list[str] = \
        [
            leftOctet ^ rightOctet
            for leftOctet, rightOctet
            in octet_tuples
        ]
    xored_bytes = bytes(xored_octets)
    return xored_bytes


assert \
    hexlify(
        bitwise_xor(
            unhexlify(a),
            unhexlify(b)
        )
    ) \
        .decode('utf-8') \
    == c
