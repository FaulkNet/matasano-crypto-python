# Challenge 55: MD4 Collisions
#
# Wang et al. (2004) found MD4 collisions in under 2^8 operations by
# exploiting differential paths — carefully chosen conditions on the
# internal state that, when satisfied, cause two slightly different messages
# to hash to the same value.
#
# MD4 processes each 64-byte block through three rounds of 16 operations each.
# Wang's attack identifies bitwise conditions on intermediate state words that
# must hold for the differential to cancel out. Most first-round conditions
# can be "massaged in" directly by adjusting message words and back-solving.
#
# Given message M, construct M' = M with specific bits flipped such that
# MD4(M) = MD4(M'). The bit differences between M and M' follow a fixed
# differential pattern from Wang's paper.
#
# Algorithm overview:
#   1. Pick a random 64-byte message M.
#   2. First-round corrections: for each of the 16 first-round operations,
#      compute the expected state word, check which condition bits are wrong,
#      fix them in the state, back-solve to adjust the corresponding message
#      word, then verify no earlier conditions were disturbed.
#   3. Some second-round conditions can also be enforced (more complex).
#   4. Compute M' = M XOR delta (fixed differential).
#   5. If MD4(M) == MD4(M'): collision found! Otherwise retry with new M.
#
# Expected success rate: ~1 in a few hundred random M values.
#
# Task: implement the Wang attack and find an MD4 collision.
#   Print both M and M' and verify MD4(M) == MD4(M').

# TODO: implement Wang et al MD4 collision attack
