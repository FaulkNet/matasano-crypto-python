# Challenge 32: Break HMAC-SHA1 with a slightly less artificial timing leak
#
# Same attack as Challenge 31, but the per-byte sleep is reduced from 50ms
# to 5ms (or even 1ms). The timing signal is now small enough that network
# jitter and OS scheduling noise can swamp it on a single measurement.
#
# Solution: statistical averaging.
#   For each candidate byte at each position, send multiple requests and
#   average (or take the median of) the response times. More samples = more
#   confidence. With enough samples, even a 1ms signal becomes detectable
#   above the noise floor.
#
# Tips:
#   - Start with ~5-10 samples per candidate and tune upward if the attack
#     is unreliable.
#   - The median is more robust than the mean against outlier spikes.
#   - Consider adaptive re-testing: if the top two candidates are very close,
#     collect more samples for just those two before deciding.
#
# This challenge demonstrates that real-world timing attacks (e.g. remote
# timing attacks on TLS padding) are feasible even with small signals,
# given statistical rigor and enough measurements.

# TODO: extend Challenge 31's server (reduce sleep to 5ms) and update the attack to use averaging
