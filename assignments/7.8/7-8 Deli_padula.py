
#James Padula
#3/10/2026
#CSC-121-OA1

sandwich_orders = ["French Dip", "Italian", "Cheesesteak", "Chicken Parm"]

finished_sandwiches = []

for sandwich in sandwich_orders:
    print("I made your " + sandwich + " sandwich.")
    finished_sandwiches.append(sandwich)  

print("\nEvery sandwich has been made:")
for sandwich in finished_sandwiches:
    print("- " + sandwich)