def car_information(manufacturer, model, **car_info):
    """Return a dictionary of information about a car."""
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    return car_info

def print_car(car):
    """Print the information about a car."""
    for key, value in car.items():
        if isinstance(value, str):
            print(f"{key.title()}: {value.title()}")
        else:
            print(f"{key.title()}: {value}")

car = car_information('subaru', 'outback', color='blue', tow_package=True, moon_roof=True)
print_car(car)