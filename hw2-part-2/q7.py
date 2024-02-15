round_digits = 5

# A1 = likes vehicle #1
# A2 = likes vehicle #2
# A3 = likes vehicle #3.

A1 = 0.55
A2 = 0.65
A3 = 0.7

P_A1_U_A2 = 0.8
P_A2_I_A3 = 0.4
P_A1_U_A2_U_A3 = 0.84

# (a) A1 I A2
print(f"A1 I A2: {round(A1 + A2 - P_A1_U_A2, round_digits)}")

# (b) P(A2|A3) = P(A2∩A3)/P(A3)
print(f"P(A2|A3): {round(P_A2_I_A3/A3, round_digits)}")

# (d) P(P(A2 U A3)|A1')
# Z = P(A2 U A3) 
# P(Z|A1') = P(Z∩A1')/P(A1')
P_A2_U_A3 = A2 + A3 - P_A2_I_A3
P_A2_U_A3_I_not_A1 = P_A1_U_A2_U_A3 - A1
print(f"P(P(A2 U A3)|A1'): {round(P_A2_U_A3_I_not_A1/(1 - A1), round_digits)}")
