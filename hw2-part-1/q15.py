def factorial(n):
    """Calculate the factorial of a number."""
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def permutation(n, r):
    """Calculate permutations of n items taken r at a time."""
    return factorial(n) / factorial(n - r)

def combination(n, r):
    """Calculate combinations of n items taken r at a time."""
    return factorial(n) / (factorial(r) * factorial(n - r))

round_digits = 5

total_bulbs = 18
bulbs_13w = 6
bulbs_18w = 7
bulbs_23w = 5

# (a) Probability exactly two 23-watt bulbs are selected
prob_two_23w = (combination(bulbs_23w, 2) * combination(total_bulbs - bulbs_23w, 1)) / combination(total_bulbs, 3)
print(f"(a) {round(prob_two_23w, round_digits)}")

# (b) Probability all three bulbs have the same rating
prob_all_same = (combination(bulbs_13w, 3) + combination(bulbs_18w, 3) + combination(bulbs_23w, 3)) / combination(total_bulbs, 3)
print(f"(b) {round(prob_all_same, round_digits)}")

# (c) Probability one bulb of each type is selected
prob_one_each_type = (combination(bulbs_13w, 1) * combination(bulbs_18w, 1) * combination(bulbs_23w, 1)) / combination(total_bulbs, 3)
print(f"(c) {round(prob_one_each_type, round_digits)}")

# (d) Probability at least 6 bulbs examined before getting a 23-watt bulb
print(f"(d) {round(combination(bulbs_13w + bulbs_18w, 5)/combination(total_bulbs, 5), round_digits)}")