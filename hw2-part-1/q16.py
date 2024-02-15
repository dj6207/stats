import numpy as np

round_digits = 5

# Given data
#   O A B AB
# 1
# 2
# 3
data = np.array([
    [0.082, 0.108, 0.009, 0.004],
    [0.133, 0.141, 0.018, 0.005],
    [0.215, 0.210, 0.055, 0.020]
])

# Calculate sum of each column
column_sums = np.sum(data, axis=0)

# Calculate sum of each row
row_sums = np.sum(data, axis=1)

# A = {type A selected}, B = {type B selected}, and C = {ethnic group 3 selected}
print(f"P(A) = {round(column_sums[1], round_digits)}")
print(f"P(C) = {round(row_sums[2], round_digits)}")
print(f"P(A ∩ C) = {data[2][1]}")

# Probability of A given C P(A∩C)/P(C)
print(f"P(A|C) = {round(data[2][1]/row_sums[2], round_digits)}")
# Probability of C given A P(A∩C)/P(A)
print(f"P(C|A) = {round(data[2][1]/column_sums[1], round_digits)}")

# If the selected individual does not have type B blood, what is the probability that he or she is from ethnic group 1?
# P(E) probability of selecting an individual who does not have type B blood
# P(D∩E) probability of selecting an individual from ethnic group 1 who does not have type B blood.
# P(D∩E)/P(E)
print(round((row_sums[0]-data[0][2])/(sum(column_sums) - column_sums[2]), round_digits))