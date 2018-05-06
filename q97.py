#does python even overflow makes you think

power = 7830457

val = 28433 * (2**power) + 1

mod = 10000000000

val %= mod

print val