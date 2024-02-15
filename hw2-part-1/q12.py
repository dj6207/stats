# Choices for each component
receivers = ['Kenwood', 'Onkyo', 'Sony', 'Sherwood']
cd_players = ['Onkyo', 'Pioneer', 'Sony', 'Technics']
speakers = ['Boston', 'Infinity']
turntables = ['Onkyo', 'Sony', 'Teac', 'Technics']

# (a) Total selections without restrictions
total_selections = len(receivers) * len(cd_players) * len(speakers) * len(turntables)

# (b) Both receiver and CD player are Sony
sony_receiver_cd = 1 * 1 * len(speakers) * len(turntables)

# (c) No Sony components
no_sony_receivers = len([r for r in receivers if r != 'Sony'])
no_sony_cd_players = len([cd for cd in cd_players if cd != 'Sony'])
no_sony_turntables = len([t for t in turntables if t != 'Sony'])
no_sony_selections = no_sony_receivers * no_sony_cd_players * len(speakers) * no_sony_turntables

# (d) At least one Sony component
at_least_one_sony = total_selections - no_sony_selections

# (e) Probability calculations
# At least one Sony component
prob_at_least_one_sony = at_least_one_sony / total_selections

# Exactly one Sony component
exact_one_sony_receiver = 1 * no_sony_cd_players * len(speakers) * no_sony_turntables
exact_one_sony_cd = no_sony_receivers * 1 * len(speakers) * no_sony_turntables
exact_one_sony_turntable = no_sony_receivers * no_sony_cd_players * len(speakers) * 1
exact_one_sony = exact_one_sony_receiver + exact_one_sony_cd + exact_one_sony_turntable

prob_exact_one_sony = exact_one_sony / total_selections

round_digits = 5

# print(total_selections, sony_receiver_cd, no_sony_selections, at_least_one_sony, round(prob_at_least_one_sony, 3), round(prob_exact_one_sony, 3))
print(f"Total selection: {total_selections}")
print(f"Both receiver and compact are sony: {sony_receiver_cd}")
print(f"No sony: {no_sony_selections}")
print(f"At least one sony: {at_least_one_sony}")
print(f"At least one sony component: {round(prob_at_least_one_sony, round_digits)}")
print(f"Exactly one sony component: {round(prob_exact_one_sony, round_digits)}")