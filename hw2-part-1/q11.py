# Given probabilities
P_A1 = 0.14
P_A2 = 0.10
P_A3 = 0.08
P_A1_union_A2 = 0.16
P_A1_union_A3 = 0.18
P_A2_union_A3 = 0.14
P_A1_intersect_A2_intersect_A3 = 0.02

# (a) Probability the system does not have a type 1 defect
P_not_A1 = 1 - P_A1

# (b) Probability the system has both type 1 and type 2 defects
# Using the inclusion-exclusion principle
P_A1_intersect_A2 = P_A1 + P_A2 - P_A1_union_A2

# (c) Probability the system has both type 1 and type 2 defects but not a type 3 defect
P_A1_and_A2_not_A3 = P_A1_intersect_A2 - P_A1_intersect_A2_intersect_A3

# (d) Probability the system has at most two of these defects
# This includes no defects, 1 defects, 2 defects but not all 3
P_at_most_two_defects = 1 - P_A1_intersect_A2_intersect_A3

print(f"(a) {P_not_A1}")
print(f"(b) {P_A1_intersect_A2}")
print(f"(c) {P_A1_and_A2_not_A3}")
print(f"(d) {P_at_most_two_defects}")
