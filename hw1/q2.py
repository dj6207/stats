round_digits = 5

data = "2	6 3	20 4	24 5	18 6	13 7	8 8	5 9	6 10	2 11	1"
data = data.split()
bidders = [int(i) for i in data[::2]]
contracts = [int(i) for i in data[1::2]]
data_dict = dict()
if len(bidders) == len(contracts):
    for i, k in  enumerate(bidders):
        data_dict[k] = contracts[i]
else:
    print("Make sure bidder len and contract len are the same")

total = sum(contracts)

# (a)
# at most x bidders
x = 5
at_most_x = sum([v for k, v in data_dict.items() if k <= 5])
print(f"at most {x}: {round(at_most_x/total, round_digits)}")

# at least y bidders
y = 5
at_least_x = sum([v for k, v in data_dict.items() if k >= 5])
print(f"at least {y}: {round(at_least_x/total, round_digits)}")

# (b)
# between 5 and 10 bidders, inclusive
range_b1 = range(5, 11)
in_range_b1 = sum([v for k, v in data_dict.items() if k in range_b1])
print(f"between {range_b1} inclusive: {round(in_range_b1/total, round_digits)}")

# between 5 and 10 bidders, not inclusive
range_b2 = range(6, 10)
in_range_b2 = sum([v for k, v in data_dict.items() if k in range_b2])
print(f"between {range_b2} not inclusive: {round(in_range_b2/total, round_digits)}")
