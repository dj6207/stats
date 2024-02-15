round_digits = 10

# A boiler has four identical relief valves. The probability that any particular valve will open on demand is 0.95. Assume independent operation of the valves.
P_any_valve_open = 0.95

# P(at least one opens)=1−P(none open)
print(f"At least one open: {round(1 - (1 - P_any_valve_open)**4, round_digits)}")

# P(at least one failed to open) = 1 - P(All open)
print(f"At least one failed: {round(1 - P_any_valve_open**4, round_digits)}")