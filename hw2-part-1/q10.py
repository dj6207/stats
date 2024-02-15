round_digits = 5

A = 0.43
B = 0.47
C = 0.65
A_u_B = 0.6
A_u_C = 0.79
B_u_C = 0.72
A_u_B_u_C = 0.81

# (a)
print(f"(a) {round(A_u_B_u_C, round_digits)}")

# (b)
print(f"(b) {round(1 - A_u_B_u_C, round_digits)}") 

# (c)
print(f"(c) {round(A_u_B_u_C - A_u_B, round_digits)}")

# (d)
print(f"(d) {round((A_u_B_u_C - A_u_B) + (A_u_B_u_C - A_u_C) + (A_u_B_u_C - B_u_C),round_digits)}")
