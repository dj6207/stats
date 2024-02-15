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

# Day Shift: 10 workers
# Swing Shift: 8 workers
# Graveyard Shift: 6 workers
# Total Workers: 10 + 8 + 6 = 24
day_shift = 10
swing_shift = 8
graveyard_shift = 6
total = day_shift + swing_shift + graveyard_shift

# (a) How many selections result in all 3 workers coming from the day shift?
# What is the probability that all 3 selected workers will be from the day shift? (Round your answer to four decimal places.)
day_shift_selection = combination(day_shift, 3)
prob_day_shift = day_shift_selection / combination(total, 3)
print(f"3 workers comming from the day shift selection {day_shift_selection}")
print(f"All 3 workers from day shift {round(prob_day_shift, round_digits)}")

# (b) What is the probability that all 3 selected workers will be from the same shift? (Round your answer to four decimal places.)
same_shift_selection = combination(day_shift, 3) + combination(swing_shift, 3) + combination(graveyard_shift, 3)
prob_same_shift = same_shift_selection / combination(total, 3)
print(f"Probability that all 3 selected workers will be from the same shift {round(prob_same_shift, round_digits)}")

# (c) What is the probability that at least two different shifts will be represented among the selected workers? (Round your answer to four decimal places.)
prob_at_least_two_shifts = 1 - prob_same_shift
print(f"Probability that at least two different shifts will be represented among the selected {round(prob_at_least_two_shifts, round_digits)}")