round_digits = 5

def find_fifth_deviation(deviations: list):
    # Calculate the fifth deviation
    fifth_deviation = -sum(deviations)
    return fifth_deviation

def are_samples_the_given_deviation_from_mean(samples: list, deviations: list):
    result = set()
    for sample in samples:
        temp = [round(sample[i] - deviations[i], round_digits) for i in range(len(deviations))]
        print(temp)
        temp_set = set()
        for i in temp: temp_set.add(i)
        if len(temp_set) == 1 and temp_set.pop() == sum(deviations):
            result.add(tuple(sample))
    return result

data = "0.5, 0.8, 1.2, 1.5"
data = [float(i) for i in data.replace(",", " ").replace('−', '-').split()]

samples = [
    "4.5, 4.8, 5.2, 5.5, 0",
    "1.5, −0.2, 2.2, 2.5, −5.0",
    "−3.5, −3.2, −2.8, −2.5, −4",
    "−0.5, −0.2, 0.2, 0.5, 0"
]
samples = [[float(j) for j in i.replace(",", " ").replace('−', '-').split()] for i in samples]

fifth_deviation = find_fifth_deviation(data)
valid_sample = are_samples_the_given_deviation_from_mean(samples, data)

print(fifth_deviation)
print(valid_sample)