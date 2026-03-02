# Challenge 22: Crack an MT19937 seed
#
# The following routine is used "in the wild":
#   1. Wait a random amount of time (40-1000 seconds).
#   2. Seed MT19937 with the current Unix timestamp.
#   3. Wait another random amount of time.
#   4. Return the first 32-bit output of the RNG.
#
# You receive that output. Recover the seed.
#
# The attack is trivial: Unix timestamps are sequential integers in a
# predictable range. Try every timestamp near "now" as a seed, generate
# the first MT19937 output, and check if it matches. The correct seed is
# the one that produces the observed output.
#
# For testing: simulate the routine by sleeping (or just faking the wait
# with arithmetic) and record the output. Then write the cracker.
#
# This demonstrates why seeding a PRNG with the current time is dangerous:
# the seed space is tiny (only ~86400 values per day), making exhaustive
# search feasible in milliseconds.

import time

# TODO: implement the simulated routine and the seed cracker
