# Challenge 54: Kelsey and Kohno's Nostradamus Attack
#
# Can you "predict" the outcome of a future event — say, a baseball season —
# before it happens, then reveal a commitment that matches?
# With a weak hash function, yes.
#
# The attack works by building a collision tree BEFORE the event:
#
# Pre-commitment (k parameter controls tree depth):
#   1. Generate 2^k random "leaf" blocks (one for each possible outcome).
#   2. Pair them up, find collisions between each pair -> 2^(k-1) states.
#   3. Repeat until one final state remains. This is your "prediction hash."
#   4. Publish H = hash(tree_root || padding) as your commitment.
#
# Post-event forgery:
#   1. Write your actual prediction for the event.
#   2. Hash it to some intermediate state.
#   3. Find a "glue block" that collides this state into one of the 2^k leaves.
#   4. Follow the tree path from that leaf to the root.
#   5. Your full message: prediction || glue || (leaf path through tree).
#   6. Its hash == your original commitment.
#
# The suffix is only k+1 blocks long — compact enough to be plausible.
# Cost: 2^k leaf pairs * 2^(b/2) per collision for the tree.
# vs. naive: 2^b for a direct second preimage.
#
# Task: implement against your toy MD hash from Challenge 52.
#   Predict something plausible (e.g. sports scores), commit, then reveal.

# TODO: build the collision tree, commit, then forge after "event" is known
