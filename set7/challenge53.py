# Challenge 53: Kelsey and Schneier's Expandable Messages
#
# A second preimage attack: given message M, find M' != M with H(M) = H(M').
# Naively this takes 2^b work. For long messages, Kelsey-Schneier reduces this.
#
# Key insight: intermediate hash states are reachable via many paths.
# For a message of 2^k blocks, we can exploit this structure.
#
# Step 1 — Build an expandable message:
#   An expandable message can produce any length in [k, k + 2^k - 1] blocks.
#   At each level i (from k down to 1):
#     Find a collision between:
#       (a) a single block M_short from state s_{i-1}
#       (b) a (2^(k-i) + 1)-block message M_long from state s_{i-1}
#     Both lead to the same next state s_i.
#   After k levels, we have k (short, long) pairs.
#   To produce a specific length L: choose short or long at each level.
#
# Step 2 — Map the target:
#   Hash M block by block, recording the intermediate state after each block.
#   Store: state -> block_index
#
# Step 3 — Find a bridge:
#   From the expandable message's final state s_k, find a single block B
#   that leads to some intermediate state in the map.
#   Expected work: 2^b / (len(M) - k)
#
# Step 4 — Construct the forgery:
#   Choose expandable message length so that total = (bridge target index - 1).
#   Append B and the suffix of M from the bridge point onward.
#
# Task: implement this against your toy MD hash from Challenge 52.

# TODO: implement expandable messages and the second preimage attack
