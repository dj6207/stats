# P(A)
# P(B)
A = 0.6
B = 0.3

round_digits = 5
A_intersect_B = 0.2

# (b) Probability that the selected student has at least one of these two types of cards?
print(f"Have at least one of the cards {round(A + B - A_intersect_B, round_digits)}")

# (c) Probability that the selected student has neither type of card?
print(f"Have neither card {round(1 - (A + B - A_intersect_B), round_digits)}")

# (e) Calculate the probability that the selected student has exactly one of the two types of cards.
print(f"Have exactly one of the card {round(A + B - 2 * A_intersect_B, round_digits)}")