round_digits = 5

num_part = " 0	    1	    2	    3	    4	    5	    6	    7	    8	    9	    10	    11	    12	    13	    14"
freq = "1	2	3	12	11	15	19	10	9	4	5	3	3	2	1"

# num_part = num_part.split()
num_part = [int(i) for i in num_part.split()]
# freq = freq.split()
freq = [int(i) for i in freq.split()]

data_dict = dict()
if len(num_part) == len(freq):
    for i, k in  enumerate(num_part):
        data_dict[k] = freq[i]
else:
    print("Make sure num_part len and freq len are the same")

total = sum([v for k, v in data_dict.items()])

# (a)
# Proportion of the sampled wafers had at least x particle
x = 1
at_least_x = sum([v for k, v in data_dict.items() if k >= x])
print(f"at least {x}: {round(at_least_x/total, round_digits)}")

# Proportion of the sampled wafers had at least y particle
y = 5
at_least_y = sum([v for k, v in data_dict.items() if k >= y])
print(f"at least {y}: {round(at_least_y/total, round_digits)}")

# (b)
# between 5 and 10 bidders, inclusive
range_b1 = range(5, 11)
in_range_b1 = sum([v for k, v in data_dict.items() if k in range_b1])
print(f"between {range_b1} inclusive: {round(in_range_b1/total, round_digits)}")

# between 5 and 10 bidders, not inclusive
range_b2 = range(6, 10)
in_range_b2 = sum([v for k, v in data_dict.items() if k in range_b2])
print(f"between {range_b2} not inclusive: {round(in_range_b2/total, round_digits)}")

