import yaml

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    @classmethod
    def from_dict(cls, data):
        return cls(data['make'], data['model'], data['year'])

# Example YAML string
yaml_data = """
make: Toyota
model: Corolla
year: 2020
"""

# Convert YAML string to dictionary
data = yaml.safe_load(yaml_data)

# Create Car object
car = Car.from_dict(data)

print(car.make)
print(car.model)
print(car.year)
