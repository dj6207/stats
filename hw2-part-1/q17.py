import numpy as np

round_digits = 5

#   S M L
# R
# D

data = np.array([
    [0.12, 0.24, 0.16],
    [0.24, 0.12, 0.12]
])

# Calculate sum of each column
column_sums = np.sum(data, axis=0)

# Calculate sum of each row
row_sums = np.sum(data, axis=1)

# (a)
# probability that the individual purchased a small cup?
print(column_sums[0])
# probability that the individual purchased a cup of decaf coffee?
print(row_sums[1])

# (b)
# selected individual purchased a small cup, what now is the probability that he/she chose decaf coffee?
print(round(data[1][0]/column_sums[0] ,round_digits))

# (c)
# selected individual purchased decaf, what now is the probability that a small size was selected?
print(round(data[1][0]/row_sums[1], round_digits))