# Challenge 49: CBC-MAC Message Forgery
#
# CBC-MAC is secure as a MAC when used correctly (fixed-length messages,
# secret key). But it breaks badly when misused.
#
# Part 1 — Attacker-controlled IV:
#   A naive bank protocol sends: message || CBC-MAC(key, IV, message)
#   where the IV is transmitted with the message.
#
#   Attack: capture a valid (message, IV, MAC) from victim account V.
#   To forge a transfer from V to attacker A:
#     target = "from=#{attacker_id}&to=#{attacker_id}&amount=1000000"
#     chosen_IV = IV XOR first_block(victim_message) XOR first_block(target)
#     The MAC of target under chosen_IV equals the original MAC.
#   The server accepts it because it trusts the client-supplied IV.
#
# Part 2 — Fixed IV, length extension:
#   Protocol upgraded to fixed IV=0. Now the MAC is secure... unless:
#   Capture M || T where T = CBC-MAC(key, 0, M).
#   Craft extension E such that M || E has the same MAC.
#   Use T as the IV for E: CBC-MAC(key, 0, M || E) = CBC-MAC(key, T, E).
#   The MAC of M || E equals CBC-MAC(key, T, E).
#   So: XOR the first block of E with T, then CBC-MAC with IV=0 gives the
#   same result as CBC-MAC of M || E.
#
# Task: implement both attacks against a simulated bank server.

# TODO: implement Part 1 (IV attack) and Part 2 (length extension)
