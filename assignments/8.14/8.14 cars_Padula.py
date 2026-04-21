#James Padula
#3/23/2026
#CSC-121-OA1

def make_car(manufacturer, model, **car_info):
    """Build a dictionary containing everything we know about a car."""
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    return car_info

#call function
my_car = make_car('mazda', '3', color='black', transmission='automatic')
print(my_car)