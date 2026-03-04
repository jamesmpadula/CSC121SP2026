#James Padula
#3/3/2025
#CSC-121-OA1

# 6.9 Favorite Places

favorite_places = {
    "Jordan": ["rock climbing gym", "mountains"],
    "Ethan": ["skatepark"],
    "Mayson": ["beach", "coffee shop"]
}

for name in favorite_places:
    print(name)
    print("Favorite places:")
    
    for place in favorite_places[name]:
        print(place)
    
    print() 