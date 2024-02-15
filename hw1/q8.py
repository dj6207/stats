round_digits = 5

sample_size = 10
data = "F    F    S    F    S    S    S    S    F    F"
data = data.split()
total = len(data)

data_dict = dict()
for i in data:
    if data_dict.get(i):
        data_dict[i] += 1
    else:
        data_dict[i] = 1

# (a) What is the value of the sample proportion of successes
succ_prop = data_dict.get("S")/total
print(f"Success {round(succ_prop, round_digits)}")

# (b) Replace each S with a 1 and each F with a 0
s_f = lambda i: 1 if i == "S" else 0
new_data = [s_f(i) for i in data]
print(f"Replace each S with a 1 and each F with a 0: {round(sum(new_data)/total, round_digits)}")

# (c)
new_total = 25
target_prop = 0.68
print(f"How many S for {target_prop}: {(new_total * target_prop) - (total * succ_prop)}")
