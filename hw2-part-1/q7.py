round_digits = 5

total_joints = 10000
inspector_a_defects = 740
inspector_b_defects = 742
defects_judge_at_least_one = 1077

# (a)
print(f"Inspected by neither {round(1 - defects_judge_at_least_one/total_joints, round_digits)}")

# (b)
only_inspector_b = defects_judge_at_least_one - inspector_a_defects
print(f"Judge by B but not A {round(only_inspector_b/total_joints, round_digits)}")
