import numpy as np

round_digits = 5

#   N L M H
# L
# M
# H

data = np.array([
    [0.04, 0.05, 0.05, 0.02],
    [0.07, 0.11, 0.20, 0.11],
    [0.02, 0.03, 0.15, 0.15]
])

column_sums = np.sum(data, axis=0)
row_sums = np.sum(data, axis=1)

# (a)
print(f"(a) {round(data[1][3], round_digits)}")

# (b)
print(f"(b) low auto {round(row_sums[0], round_digits)}")
print(f"(b) low homeowner {round(column_sums[1],round_digits)}")

# (e)
print(f"(e) {round(column_sums[1] + row_sums[0] - data[0][1], round_digits)}")

# (f)
print(f"(f) {round(1 - (column_sums[1] + row_sums[0] - data[0][1]), round_digits)}")
