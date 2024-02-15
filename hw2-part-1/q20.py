carry_lyme = 0.14
carry_hge = 0.06
carry_at_least_one_also_carry_both = 0.06
round_digits = 5

# P(L) = 0.14
# P(H) = 0.06
# P(L∩H|L∪H) all ticks that carry at least one of these diseases P(L∪H) carry both P(L∩H)
# Find P(L∩H|H)
# 0.06 = P(L∩H)/P(L∪H)
# 0.06 * P(L∪H) = P(L∩H)
# 0.06 * (P(L) + P(H) - P(L∩H)) = P(L∩H)
# 0.06 * (0.14 + 0.06 - P(L∩H)) = P(L∩H)
# (0.012 - 0.06 * P(L∩H)) = P(L∩H)
# 0.012 = 1.06 * P(L∩H)
# 0.012/1.06 = P(L∩H)
# (0.012/1.06)/0.06
both_lyme_and_hge = ((carry_lyme + carry_hge) * carry_at_least_one_also_carry_both)/(1 + carry_at_least_one_also_carry_both)
print(f"Tick with HGE also carry Lyme {round(both_lyme_and_hge/carry_at_least_one_also_carry_both, round_digits)}")
