#James Padula
#3/2/2026
#CSC-121-OA1

rivers = {                         #river and country dictionary
    'amazon': 'brazil',
    'parana': 'argentina',
    'orinoco': 'venezuela'
}
for river, country in rivers.items():
    print(f"The {river.title()} River runs through {country.title()}.")

print("\nRivers:")                 #print river name
for river in rivers.keys():
    print(river.title())

print("\nCountries:")              #print country name
for country in rivers.values():
    print(country.title())