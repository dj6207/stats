# consume coffee
cc = 0.65
# consume carbonated soda
cs = 0.5
# consume at least one of these two prod
at_least_one_of_drink = 0.75

round_digits = 5

# (a) What is the probability that a randomly selected adult regularly consumes both coffee and soda?
print(f"Consume both {round(at_least_one_of_drink - (at_least_one_of_drink - cs) - (at_least_one_of_drink - cc), round_digits)}")

# (b) What is the probability that a randomly selected adult doesn't regularly consume at least one of these two products?
print(f"Doesn't consume at least one of these two product {round(1 - at_least_one_of_drink,round_digits)}")

