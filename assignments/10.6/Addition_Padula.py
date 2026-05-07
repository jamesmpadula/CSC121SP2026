#James Padula
#4/21/2026
#CSC-121-OA1

print("Let's add some numbers!")
                                           #first number
first_number = input("Enter a number: ")

second_number = input("Enter another number: ")
#second number
try:
    total = int(first_number) + int(second_number)

except ValueError:         #error message
    print("Oops! You have to enter numbers.") 

else:
    print(f"The answer is {total}")  #print total