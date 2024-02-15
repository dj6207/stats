# round_digits = 5

# # disappear aircraft discovered
# # P(Discovered)
# discovered = 0.72
# # P(Not Discovered)
# not_discovered = 0.28
# # discovered aircraft with emergency locator
# # P(Have EL|Discovered)
# discovered_w_el = 0.68
# # P(No El|Discovered)
# discovered_wo_el = 0.32
# # not discovered aircraft with out emergency locators
# # P(No EL|Not Discovered)
# not_discovered_wo_el = 0.88
# # P(Have EL|Not Discovered)
# not_discovered_w_el = 0.12

# P_el = (discovered * discovered_w_el) + (not_discovered * not_discovered_w_el)
# P_wo_el = 1 - P_el

# # Bayes' theorem
# # P(A|B) = (P(B|A)*P(A))/(P(B))

# # (a) If has emergency locator, prob that it will not be discovered
# # P(Not Discovered|Have EL)) = P(Have El| Not Discovered) * P(Not Discovered) / P(Have El)
# print(f"(a) {round((not_discovered_w_el * not_discovered)/P_el, round_digits)}")


# # (b) If does not have el, prob it is discovered
# # P(Discovered|No EL) = P(No EL|Discovered) * P(Discovered) / P(No EL)
# print(f"(b) {round((discovered_wo_el * discovered)/P_wo_el, round_digits)}")

round_digits = 5

# disappear aircraft discovered
# P(Discovered)
discovered = 0.78
# P(Not Discovered)
not_discovered = (1 - discovered)
# discovered aircraft with emergency locator
# P(Have EL|Discovered)
discovered_w_el = 0.63
# P(No El|Discovered)
discovered_wo_el = (1 - discovered_w_el)
# not discovered aircraft with out emergency locators
# P(No EL|Not Discovered)
not_discovered_wo_el = 0.86
# P(Have EL|Not Discovered)
not_discovered_w_el = (1 - not_discovered_wo_el)

P_el = (discovered * discovered_w_el) + (not_discovered * not_discovered_w_el)
P_wo_el = 1 - P_el

# Bayes' theorem
# P(A|B) = (P(B|A)*P(A))/(P(B))

# (a) If has emergency locator, prob that it will not be discovered
# P(Not Discovered|Have EL)) = P(Have El| Not Discovered) * P(Not Discovered) / P(Have El)
print(f"(a) {round((not_discovered_w_el * not_discovered)/P_el, round_digits)}")


# (b) If does not have el, prob it is discovered
# P(Discovered|No EL) = P(No EL|Discovered) * P(Discovered) / P(No EL)
print(f"(b) {round((discovered_wo_el * discovered)/P_wo_el, round_digits)}")