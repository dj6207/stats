round_digits = 5

# Reg
A1 = 0.4
# Plus
A2 = 0.35
# Prem
A3 = 0.25

# B = fill gas
# P(B|A1) reg fill up = P(A1|B) * P(B) / P(A1)
P_B_knowing_A1 = 0.2
# P(B|A2) plus fill up
P_B_knowing_A2 = 0.4
# P(B|A3) prem fill up
P_B_knowing_A3 = 0.5

# C = use credit card
# P(C| P(B|A1) ) = P( P(B|A1) |C) * P(C) / P(B|A1)
P_C_knowing_P_B_knowing_A1 = 0.7

# P(C| 1 - P(B|A1))
P_C_knowing_P_not_B_knowing_A1 = 0.5

# P(C| P(B|A2))
P_C_knowing_P_B_knowing_A2 = 0.6

# P(C| 1 - P(B|A2))
P_C_knowing_P_not_B_knowing_A2 = 0.5

# P(C| P(B|A3))
P_C_knowing_P_B_knowing_A3 = 0.5

# P(C| 1 - P(B|A3))
P_C_knowing_P_not_B_knowing_A3 = 0.4

# Bayes' theorem
# P(A|B) = (P(B|A)*P(A))/(P(B))

# (a)
print(f"plus, fill, credit: {round(A2 * P_B_knowing_A2 * P_C_knowing_P_B_knowing_A2, round_digits)}")

# (b)
print(f"prem, no fill, credit: {round(A3 * (1 - P_B_knowing_A3) * P_C_knowing_P_not_B_knowing_A3, round_digits)}")

# (c) 
P_A3_B_C = A3 * P_B_knowing_A3 * P_C_knowing_P_B_knowing_A3
P_A3_not_B_C = A3 * (1 - P_B_knowing_A3) * P_C_knowing_P_not_B_knowing_A3
print(f"prem, cred: {round(P_A3_B_C + P_A3_not_B_C, round_digits)}")

# (d)
P_A1_B_C = A1 * P_B_knowing_A1 * P_C_knowing_P_B_knowing_A1
P_A2_B_C  = A2 * P_B_knowing_A2 * P_C_knowing_P_B_knowing_A2
P_A3_B_C = A3 * P_B_knowing_A3 * P_C_knowing_P_B_knowing_A3
print(f"fill, credit: {round(sum([P_A1_B_C, P_A2_B_C, P_A3_B_C]), round_digits)}")

# (e)
P_A1_not_B_C = A1 * (1 - P_B_knowing_A1) * P_C_knowing_P_not_B_knowing_A1
P_A2_not_B_C = A2 * (1 - P_B_knowing_A2) * P_C_knowing_P_not_B_knowing_A2
P_A3_not_B_C = A3 * (1 - P_B_knowing_A3) * P_C_knowing_P_not_B_knowing_A3
P_C = sum([P_A1_B_C, P_A1_not_B_C, P_A2_B_C, P_A2_not_B_C, P_A3_B_C, P_A3_not_B_C])
print(f"credit card: {round(P_C, round_digits)}")

# (f)
# P(A3|C) = P(C|A3) * P(A3) / P(C)
P_C_knowing_A3 = (P_B_knowing_A3 * P_C_knowing_P_B_knowing_A3) + ((1 - P_B_knowing_A3) * P_C_knowing_P_not_B_knowing_A3)
print(f"P(A3|C): {round((P_C_knowing_A3 * A3)/P_C, round_digits)}")

