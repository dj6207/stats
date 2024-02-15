# round_digits = 5

# prob_stop_first = 0.35
# prob_stop_second = 0.55
# prob_stop_at_least_one = 0.7

# # (a)
# prob_stop_at_both = prob_stop_at_least_one - (prob_stop_at_least_one - prob_stop_first) - (prob_stop_at_least_one - prob_stop_second)
# print(f"(a) {round(prob_stop_at_both, round_digits)}")

# # (b)
# print(f"(b) {round(prob_stop_first - prob_stop_at_both, round_digits)}")

# # (c)
# print(f"(c) {round(prob_stop_at_least_one - prob_stop_at_both, round_digits)}")

round_digits = 5

prob_stop_first = 0.35
prob_stop_second = 0.45
prob_stop_at_least_one = 0.5

# (a)
prob_stop_at_both = prob_stop_at_least_one - (prob_stop_at_least_one - prob_stop_first) - (prob_stop_at_least_one - prob_stop_second)
print(f"(a) {round(prob_stop_at_both, round_digits)}")

# (b)
print(f"(b) {round(prob_stop_first - prob_stop_at_both, round_digits)}")

# (c)
print(f"(c) {round(prob_stop_at_least_one - prob_stop_at_both, round_digits)}")
