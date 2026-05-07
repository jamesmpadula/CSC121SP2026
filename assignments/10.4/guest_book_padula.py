#James Padula
#4/21/2026
#CSC-121-OA1

filename = "guest_book.txt"

print("Enter 'quit' when you are finished.")

while True:
    name = input("\nWhat is your name? ")

    if name == "quit":
        break
    else:
        print(f"Hello {name}, you have been added to the guest book.")
        
        with open(filename, 'a') as f:
            f.write(f"{name}\n")