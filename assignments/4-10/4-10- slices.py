#James Padula
#2/17/2026
#CSC-121-OA1

guests = ['Master Chief', 'Frodo Baggins', 'Geico Gecko']

print("Dear " + guests[0] + ", you are invited to dinner at my place.")
print("Dear " + guests[1] + ", you are invited to dinner at my place.")
print("Dear " + guests[2] + ", you are invited to dinner at my place.")
 
guests.insert(0, 'Scooby Doo')
guests.insert(2, 'Patrick Star')
guests.append('Spongebob Squarepants')

print("I have found a bigger dinner table, so 3 more guests can join us.\n")
 
guests.sort()
 
for guest in guests:
    print("Dear " + guest + ", you are invited to dinner at my place.")

    print()  

print("The first three items in the list are:")
for guest in guests[:3]:
    print(guest)

print("\nThe last three items in the list are:")
for guest in guests[-3:]:
    print(guest)