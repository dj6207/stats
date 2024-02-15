# Define the states of each component: S for success, F for failure
states = ['S', 'F']

# Initialize sets for events
A, B, C, C_prime = set(), set(), set(), set()

# Iterate through all possible states of the system
for s1 in states:
    for s2 in states:
        for s3 in states:
            outcome = (s1, s2, s3)
            functioning_components = outcome.count('S')

            # Event A: Exactly two components function
            if functioning_components == 2:
                A.add(outcome)

            # Event B: At least two components function
            if functioning_components >= 2:
                B.add(outcome)

            # Event C: System functions (1 must function; 2 or 3 must function)
            if s1 == 'S' and (s2 == 'S' or s3 == 'S'):
                C.add(outcome)
            else:
                C_prime.add(outcome)

# Perform set operations
A_union_C = A.union(C)
A_intersect_C = A.intersection(C)
B_union_C = B.union(C)
B_intersect_C = B.intersection(C)

# Print results
print(f"A = {A}")
print(f"B = {B}")
print(f"C = {C}")
print(f"C' = {C_prime}")
print(f"A ∪ C = {A_union_C}")
print(f"A ∩ C = {A_intersect_C}")
print(f"B ∪ C = {B_union_C}")
print(f"B ∩ C = {B_intersect_C}")
