import numpy as np

round_digits = 5

# Short Sleeved
#   Pl Pr St
# S
# M
# L

short_sleeved = np.array([
    [0.04, 0.02, 0.05],
    [0.09, 0.05, 0.12],
    [0.03, 0.07, 0.08]
])

short_sleeved_column_sums = np.sum(short_sleeved, axis=0)
short_sleeved_row_sums = np.sum(short_sleeved, axis=1)

# Long Sleeved
#   Pl Pr St
# S
# M
# L

long_sleeved = np.array([
    [0.03, 0.02, 0.03],
    [0.09, 0.07, 0.07],
    [0.04, 0.02, 0.08]
])

long_sleeved_column_sums = np.sum(long_sleeved, axis=0)
long_sleeved_row_sums = np.sum(long_sleeved, axis=1)

# (a) What is the probability that the next shirt sold is a medium, long-sleeved, print shirt?
print(f"Med, long, print {long_sleeved[1][1]}")

# (b) What is the probability that the next shirt sold is a medium print shirt?
# print(f"{short_sleeved_row_sums[1] + long_sleeved_row_sums[1]}")
print(f"Medium print {round(short_sleeved[1][1] + long_sleeved[1][1], round_digits)}")

# (c) What is the probability that the next shirt sold is a short-sleeved shirt? A long-sleeved shirt?
print(f"Short {sum(short_sleeved_row_sums)}")
print(f"Long {sum(long_sleeved_row_sums)}") 

# (d)
# What is the probability that the size of the next shirt sold is medium?
print(f"Medium {short_sleeved_row_sums[1] + long_sleeved_row_sums[1]}")
# What is the probability that the pattern of the next shirt sold is a print?
print(f"Print {short_sleeved_column_sums[1] + long_sleeved_column_sums[1]}")

# (e) Given that the shirt just sold was a short-sleeved plaid, what is the probability that its size was medium?
prob_short_plaid = short_sleeved_column_sums[0]
print(f"Given short plaid, Prob size is med {round(short_sleeved[1][0]/prob_short_plaid, round_digits)}")

# (f) Given that the shirt just sold was a medium plaid, what is the probability that it was short-sleeved? Long-sleeved? 
prob_med_plaid = short_sleeved[1][0] + long_sleeved[1][0]
print(f"Short {short_sleeved[1][0]/(short_sleeved[1][0] + long_sleeved[1][0])}")
print(f"Long {long_sleeved[1][0]/(short_sleeved[1][0] + long_sleeved[1][0])}")




