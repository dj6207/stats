round_digits = 5
round_near_five = lambda data: [round(i / 5) * 5 for i in data]

def median(data: list) -> float:
    mid = len(data) // 2
    sorted_data = sorted(data)
    if len(data) % 2 == 0:
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2
    return sorted_data[mid]

data = "108.6  	117.4  	128.4  	120.0  	103.7  	112.0  	98.3  	121.5  	123.2  "
data = [float(i) for i in data.split()]
rounded_data = round_near_five(data)

print(f"Data: {data}")
print(f"Rounded Data: {rounded_data}")

# (a)
print(f"Median {median(rounded_data)}")

# (b)
new_data = "108.6  	117.7  	128.4  	120.0  	103.7  	112.0  	98.3  	121.5  	123.2  "
new_data = [float(i) for i in new_data.split()]
rounded_new_data = round_near_five(new_data)
print(f"New Median {median(rounded_new_data)}")