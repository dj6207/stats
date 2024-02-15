round_digits = 5

#  y = number of culs-de-sac and z = number of intersections
y = "1	0	1	0	0	2	0	1	1	1	2	1	0	0	1	1	0	1	1	1	1	0	0	0 1	1	2	0	1	2	2	1	1	0	2	1	1	0	1	5	0	3	0	1	1	0	0	"
y = [int(i) for i in y.split()]

data_dict_y = dict()
for i in y:
    if data_dict_y.get(i):
        data_dict_y[i] += 1
    else:
        data_dict_y[i] = 1

total_y = sum([v for k, v in data_dict_y.items()])

# (a)
# no culs-de-sac
a_x = 0
no_y = sum([v for k, v in data_dict_y.items() if k == a_x])
print(f"{a_x} culs-de-sac: {round(no_y/total_y, round_digits)}")

# at least one cul-de-sac
a_y = 1
at_least_one_y = sum([v for k, v in data_dict_y.items() if k >= a_y])
print(f"at least {a_y} cul-de-sac: {round(at_least_one_y/total_y, round_digits)}")


z = "1	8	6	1	1	5	3	0	0	4	4	0	0	1	2	1	4	0	4	0	3	0	1	1 0	1	3	2	4	6	6	0	1	1	8	3	3	5	0	5	2	3	1	0	0	0	3	"
z = [int(i) for i in z.split()]
data_dict_z = dict()
for i in z:
    if data_dict_z.get(i):
        data_dict_z[i] += 1
    else:
        data_dict_z[i] = 1

total_z = sum([v for k, v in data_dict_z.items()])
# (b)
# at most fiver intersections
b_x = 5
at_most_five = sum([v for k, v in data_dict_z.items() if k <= b_x])
print(f"at most {b_x}: {round(at_most_five/total_z, round_digits)}")

# fewer than five intersections
b_y = 5
fewer_than_five = sum([v for k, v in data_dict_z.items() if k < b_y])
print(f"fewer than {b_y}: {round(fewer_than_five/total_z, round_digits)}")
