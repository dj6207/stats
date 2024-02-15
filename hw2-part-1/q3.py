prob_dict = {
    "mm": 0.23,
    "sb": 0.12,
    "ib": 0.05,
    "lb": 0.05,
    "hrs": 0.16,
    "mrs": 0.25,
    "b": 0.14
}

round_digits = 5
total = sum([prob for _, prob in prob_dict.items()])

# (a) What is the probability that the selected individual owns shares in the balanced fund?
balanced_fund = prob_dict.get("b")
print(f"Individual owns share in the balanced fun {round(balanced_fund/total, round_digits)}")

# (b) What is the probability that the individual owns shares in a bond fund?
bond_fund = prob_dict.get("sb") + prob_dict.get("ib") + prob_dict.get("lb")
print(f"Owns shares in a bond fund {round(bond_fund/total, round_digits)}")

# (c) Probability that the selected individual does not own shares in a stock fund?
not_own_stock_fund = total - prob_dict.get("hrs") - prob_dict.get("mrs")
print(f"Does not own shares in stock func {round(not_own_stock_fund/total, round_digits)}")