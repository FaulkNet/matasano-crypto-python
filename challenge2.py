import binascii

a = '1c0111001f010100061a024b53535009181c'  # (cypher text)
b = '686974207468652062756c6c277320657965'  # hit the bull's eye (key)
c = '746865206b696420646f6e277420706c6179'  # the kid don't play


def xor_str(string1, string2):
    return binascii.hexlify(
        "".join(
            chr(ord(leftChr) ^ ord(rightChr))
            for leftChr, rightChr
            in zip(
                binascii.unhexlify(string1.encode('utf-8')).decode('utf-8'),
                binascii.unhexlify(string2.encode('utf-8')).decode('utf-8')
            )
        ).encode('utf-8')
    ).decode('utf-8')


assert xor_str(a, b) == c
