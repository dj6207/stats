round_digits = 5

# Reg
A1 = 0.4
# Plus
A2 = 0.35
# Prem
A3 = 0.25
# B = fill gas
# P(B|A1)
P_B_knowing_A1 = 0.2
# P(B|A2)
P_B_knowing_A2 = 0.4
# P(B|A3)
P_B_knowing_A3 = 0.3

# (a)
print(f"Next customer request plus gas + fill tank {round(A2 * P_B_knowing_A2, round_digits)}")

# (b)
P_fills_tank = (A1 * P_B_knowing_A1) + (A2 * P_B_knowing_A2) + (A3 * P_B_knowing_A3)
print(f"Prob next customer fill tank {round(P_fills_tank, round_digits)}")

# (c)

# Bayes' theorem
# P(A|B) = (P(B|A)*P(A))/(P(B))

# P(A1|B) = P(B|A1)*P(A1)/P(B)
print(f"Next cust fills tank and req reg gas {round((P_B_knowing_A1 * A1)/P_fills_tank, round_digits)}")
# P(A2|B) = P(B|A2)*P(A2)/P(B)
print(f"Next cust fills tank and req plus gas {round((P_B_knowing_A2 * A2)/P_fills_tank, round_digits)}")
# P(A3|B) = P(B|A3)*P(A3)/P(B)
print(f"Next cust fills tank and req prem gas {round((P_B_knowing_A3 * A3)/P_fills_tank, round_digits)}")
