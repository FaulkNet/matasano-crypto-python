# Challenge 52: Iterated Hash Function Multicollisions
#
# Merkle-Damgård hashes have a surprising property: finding 2^n collisions
# takes only n * 2^(b/2) work, not 2^(n*b/2). This is the multicollision
# attack by Joux (2004).
#
# Why: finding a single collision in a b-bit hash takes ~2^(b/2) work
# (birthday bound). If you have a collision (M1, M2) on state s0, then for
# ANY continuation C, both (M1||C) and (M2||C) hash to the same final state.
# So one collision doubles your collision set. Find n such pairs to get 2^n
# colliding messages with n * 2^(b/2) work.
#
# Part 1: Implement a toy MD hash (b=16 or 32 bits) using AES as the
#   compression function. Implement f(n) that generates 2^n collisions.
#
# Part 2: Breaking cascaded hashing.
#   H(m) = h1(m) || h2(m)  (concatenate two hash outputs)
#   Claim: this should have 2^(b1+b2) security. Reality: much weaker.
#   Attack:
#     1. Generate 2^(b2/2) collisions in h1 (cheap if b1 is small).
#     2. With ~2^(b2/2) messages all having the same h1, birthday-search
#        for a pair that also collides in h2. Expected: 2^(b2/2) tries.
#     Total work: 2^(b1/2) * (b2/2) + 2^(b2/2)
#     Not 2^((b1+b2)/2).
#
# Task: implement both parts and report the number of compression function
#   calls required to find the cascaded collision.

# TODO: implement toy MD hash and demonstrate multicollision + cascaded hash attack
