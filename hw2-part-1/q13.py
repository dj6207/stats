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

# round_digits = 5

# total_keyboards = 25
# mechanical_defect = 14
# electrical_defect = 11

# print(f"Ways to randomly select 7 keyboards {combination(total_keyboards, 7)}")

# # we select 2 out of the 11 electrical defect keyboards and 5 out of the 14 mechanical defect keyboards
# print(f"Ways a sample of 7 keyboards so that exactly 2 have an electrical defects {combination(electrical_defect, 2) * combination(mechanical_defect,5)}")

# at_least_six = (combination(mechanical_defect, 6) * combination(electrical_defect, 1) + combination(mechanical_defect, 7))/combination(25, 7)
# print(f"7 keyboard randomly selected, probability that at least 6 of these will have a mechanical defects {round(at_least_six, round_digits)}")

round_digits = 5

total_keyboards = 25
mechanical_defect = 14
electrical_defect = 11

print(f"Ways to randomly select 5 keyboards {combination(total_keyboards, 5)}")

# we select 2 out of the 11 electrical defect keyboards and 5 out of the 14 mechanical defect keyboards
print(f"Ways a sample of 5 keyboards so that exactly 2 have an electrical defects {combination(electrical_defect, 2) * combination(mechanical_defect,3)}")

at_least_six = (combination(mechanical_defect, 4) * combination(electrical_defect, 1) + combination(mechanical_defect, 5))/combination(25, 5)
print(f"5 keyboard randomly selected, probability that at least 4 of these will have a mechanical defects {round(at_least_six, round_digits)}")
