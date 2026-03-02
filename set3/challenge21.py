# Challenge 21: Implement the MT19937 Mersenne Twister RNG
#
# The Mersenne Twister is the most widely used PRNG in the world — it is
# Python's random.random(), PHP's rand(), Ruby's rand(), etc. It is NOT
# cryptographically secure, and the rest of Set 3 exploits that.
#
# You must implement it yourself. Do NOT use Python's random module.
#
# MT19937 parameters:
#   w=32, n=624, m=397, r=31
#   a=0x9908B0DF
#   b=0x9D2C5680, c=0xEFC60000
#   s=7, t=15, u=11, l=18
#   f=1812433253
#
# Algorithm (from Wikipedia):
#   Initialization:
#     MT[0] = seed
#     for i in 1..623: MT[i] = lowest 32 bits of (f * (MT[i-1] XOR (MT[i-1] >> (w-2))) + i)
#
#   Generate numbers (twist when index reaches 624):
#     y = (MT[index] & upper_mask) | (MT[(index+1) % 624] & lower_mask)
#     MT[index] = MT[(index + m) % 624] XOR (y >> 1) XOR (0 if y%2==0 else a)
#     index += 1
#     return temper(MT[index-1])
#
#   Tempering:
#     y ^= (y >> u)
#     y ^= (y << s) & b
#     y ^= (y << t) & c
#     y ^= (y >> l)
#     return lowest 32 bits of y
#
# Task:
#   Implement class MT19937 with seed(value) and extract_number() -> int.

# TODO: implement MT19937
