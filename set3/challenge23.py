# Challenge 23: Clone an MT19937 RNG from its output
#
# MT19937's output is its internal state passed through a "tempering"
# function. The tempering function is invertible — you can undo it to
# recover the raw state values. With 624 consecutive outputs you can
# reconstruct the entire 624-element internal state array and clone the
# generator perfectly.
#
# The tempering operations and their inverses:
#   y ^= y >> 18                   inverse: y ^= y >> 18  (self-inverse)
#   y ^= (y << 15) & 0xEFC60000    inverse: y ^= (y << 15) & 0xEFC60000 (self-inverse)
#   y ^= (y << 7) & 0x9D2C5680     inverse: recover bit-by-bit from LSB up
#   y ^= y >> 11                   inverse: recover bit-by-bit from MSB down
#
# Task:
#   1. Create an MT19937 instance seeded with any value.
#   2. Collect 624 outputs.
#   3. Implement untemper(y: int) -> int that reverses the tempering.
#   4. Build a new MT19937 instance by directly injecting the untempered
#      state values (bypassing the normal seeding process).
#   5. Verify that the cloned generator produces the same sequence as the
#      original for all subsequent outputs.
#
# This shows that MT19937 is completely transparent to an observer — it
# provides zero security as a stream cipher. Hashing the output (e.g.
# with SHA-256) would break this attack.

# TODO: implement untemper() and the clone attack
