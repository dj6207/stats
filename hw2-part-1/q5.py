A1 = 0.22
A2 = 0.25
A3 = 0.28

A1_i_A2 = 0.11
A1_i_A3 = 0.05
A2_i_A3 = 0.07

A1_i_A2_i_A3 = 0.01

round_digits = 5

# (a) A1∪A2
A1_u_A2 = A1 + A2 - A1_i_A2
print(f"(a) {round(A1_u_A2, round_digits)}")

# (b) A1'∩A2'
A1n_i_A2n = 1 - A1_u_A2
print(f"(b) {round(1 - A1_u_A2, round_digits)}")

# (c) A1∪A2∪A3
A1_u_A2_u_A3 = A1 + A2 + A3 - A1_i_A2 - A1_i_A3 - A1_i_A3 - A1_i_A2_i_A3
print(f"(c) {round(A1_u_A2_u_A3, round_digits)}")

# (d) A1'∩A2'∩A3'
print(f"(d) {round(1 - A1_u_A2_u_A3, round_digits)}")

# (e) A1' ∩ A2' ∩ A3
print(f"(e) {round(A3 - A1_i_A3 - A2_i_A3 + A1_i_A2_i_A3, round_digits)}")

# (f) (A1' ∩ A2') ∪ A3
print(f"(f) {round(A1n_i_A2n + A1_i_A3 + A2_i_A3 - A1_i_A2_i_A3, round_digits)}")
