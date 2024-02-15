round_digits = 5

data = "180.6	181.7	180.9	181.7	182.5	181.5  181.4	182.1	182.1	180.4	181.8	180.6"
d = [float(i) for i in data.split()]
print(d)
data = sorted([float(i) for i in data.split()])

def calculate_variance_and_std(data: list) -> (float, float):
    mean = sum(data) / len(data)
    sample_variance = sum((x - mean) ** 2 for x in data) / (len(data) - 1)
    sample_std_deviation = sample_variance ** 0.5
    return sample_variance, sample_std_deviation

data_v, data_std_dev = calculate_variance_and_std(data)

# (a)
print(f"Range: {round(data[-1] - data[0], round_digits)}")

# (b)
print(f"Variance: {round(data_v, round_digits)}")

# (c)
print(f"Std Dev: {round(data_std_dev, round_digits)}")