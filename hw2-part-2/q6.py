round_digits = 5

# When two events are mutually independent in probability theory, it means the occurrence of one event does not affect the probability of the occurrence of the other event. In other words, knowing that one event has occurred does not change the likelihood that the other event will occur.
# The events are (mutually) independent

# Receiver functions through warranty period
A1 = 0.94
# Speaker function through warranty period
A2 = 0.91 
# CD player function through warranty period
A3 = 0.7
P_All_Function = A1 * A2 * A3
# (a) All 3 function through warranty period
print(f"(a): {round(P_All_Function, round_digits)}")

# (b) At least one component needs service during warrant period
print(f"(b): {round(1 - P_All_Function, round_digits)}")

# (c) All 3 need service
P_All_Need_Service = (1 - A1) * (1 - A2) * (1 - A3)
print(f"(c): {round(P_All_Need_Service, round_digits)}")

# (d) only receiver needs service
print(f"(d): {round((1 - A1) * A2 *A3, round_digits)}") 

# (e) exactly one of three need service
only_receiver_need_service = (1 - A1) * A2 * A3
only_speaker_need_service = A1 * (1 - A2) * A3
only_cd_need_service = A1 * A2 * (1 - A3)
print(f"(e): {round(sum([only_cd_need_service, only_receiver_need_service, only_speaker_need_service]), round_digits)}")
