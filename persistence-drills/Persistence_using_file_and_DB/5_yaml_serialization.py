import yaml

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def to_dict(self):
        # Convert the object to a dictionary
        return {
            'make': self.make,
            'model': self.model,
            'year': self.year
        }

# Example usage
car = Car("Toyota", "Corolla", 2020)
car_yaml = yaml.dump(car.to_dict())  # Convert dict to YAML

print(car_yaml)
