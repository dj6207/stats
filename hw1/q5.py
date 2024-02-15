round_digits = 5
data = "A	B	C	A	A	D	E	A	C	B	F	B	A	C	F	D	B	C	D	A A	C	B	E	B	C	E	A	B	A	A	A	B	C	C	D	F	D	B	B A	F	C	B	A	C	B	E	E	D	A	B	C	E	A	A	F	C	B	D D	D	B	D	C	A	F	A	A	B	D	E	A	E	D	B	C	A	F	A C	D	D	A	A	B	A	F	D	C	A	C	B	F	D	A	E	A	C	D"
data = data.split()
total = 100

data_dict = dict()
for i in data:
    if data_dict.get(i):
        data_dict[i] += 1
    else:
        data_dict[i] = 1

for k, v in data_dict.items():
    print(f"Activity: {k}, Freq: {v}, Relative Freq: {round(v/total, round_digits)}")
print(f"Total: {total}, Relative Freq: {round(sum([v for k, v in data_dict.items()])/total, round_digits)}")
