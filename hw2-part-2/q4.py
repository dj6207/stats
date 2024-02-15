# round_digits = 5
# A = 0.41
# B = 0.1
# AB = 0.05
# O = 0.44

# # Assuming that the phenotypes of two randomly selected individuals are independent of one another, what is the probability that both phenotypes are O?
# print(f"Both are O {round(O**2, round_digits)}")

# # What is the probability that the phenotypes of two randomly selected individuals match?
# both_match = sum([i**2 for i in [A, B, AB, O]])
# print(f"Both Match {round(both_match, round_digits)}")

round_digits = 5
A = 0.47
B = 0.15
AB = 0.04
O = 0.34

# Assuming that the phenotypes of two randomly selected individuals are independent of one another, what is the probability that both phenotypes are O?
print(f"Both are O {round(O**2, round_digits)}")

# What is the probability that the phenotypes of two randomly selected individuals match?
both_match = sum([i**2 for i in [A, B, AB, O]])
print(f"Both Match {round(both_match, round_digits)}")