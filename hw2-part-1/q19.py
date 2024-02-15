# at_least_one_allergy = 0.06
# severe_reaction = 0.43
# round_digits = 5

# # (a) If a child younger than 18 is randomly selected, what is the probability that he or she has at least one food allergy and a history of severe reaction?
# print(f"Randomly selected child with allergy and sever reaction {round(at_least_one_allergy * severe_reaction, round_digits)}")

# also_allergic_other_food = 0.3
# # (b) If a child younger than 18 is randomly selected, what is the probability that he or she is allergic to multiple foods?
# print(f"Allergic to other food {round(at_least_one_allergy * also_allergic_other_food, round_digits)}")

at_least_one_allergy = 0.07
severe_reaction = 0.37
round_digits = 5

# (a) If a child younger than 18 is randomly selected, what is the probability that he or she has at least one food allergy and a history of severe reaction?
print(f"Randomly selected child with allergy and sever reaction {round(at_least_one_allergy * severe_reaction, round_digits)}")

also_allergic_other_food = 0.2
# (b) If a child younger than 18 is randomly selected, what is the probability that he or she is allergic to multiple foods?
print(f"Allergic to other food {round(at_least_one_allergy * also_allergic_other_food, round_digits)}")