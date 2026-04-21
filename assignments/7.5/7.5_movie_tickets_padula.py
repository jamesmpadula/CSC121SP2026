#James Padula
#3/10/2026
#CSC-121-OA1

tickets = int(input("How many tickets are you purchasing? "))
total = 0

for i in range(tickets):
    age = int(input("Enter age of ticket holder " + str(i + 1) + ": "))

    if age < 3:
        price = 0
    elif age <= 12:
        price = 10
    else:
        price = 15

    total += price

print("Total cost is $", total)