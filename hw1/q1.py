import re

round_digits = 5

keys = "3.0–<3.5	3.5–<4.0	4.0–<4.5	4.5–<5.0	5.0–<5.5  5.5–<6.0	6.0–<6.5	6.5–<7.0	7.0–<7.5	7.5–<8.0"
values = "5	14	27	33	23 15	6	1	5	1"
keys = keys.split()
reg = lambda i: [float(j) for j in re.findall("\d+\.\d+", i)]
keys = [tuple(reg(i)) for i in keys]
values = values.split()
data_dict = dict()

if len(keys) == len(values):
    for index, key in enumerate(keys):
        data_dict[key] = int(values[index])
else:
    print("Error key len and value len dont match")

# print(data_dict)
# print([k[1] for k, v in data_dict.items()])
total = sum([v for _, v in data_dict.items()])

# (a) What proportion of the observations are less than 5? (Round your answer to three decimal places.)
a = 5
portion_less_than_a = sum([v for k, v in data_dict.items() if (k[1] <= float(a))])
print(f"less than {a}: {round(portion_less_than_a/total, round_digits)}")

# (b) What proportion of the observations are at least 6?
b = 6
portion_at_least_b = sum([v for k, v in data_dict.items() if k[0] >= float(b)])

print(f"at least {b}: {round(portion_at_least_b/total, round_digits)}")
