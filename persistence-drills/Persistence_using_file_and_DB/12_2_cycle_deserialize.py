import pickle

class A:
    def __init__(self):
        self.name = "Object A"
        self.ref_b = None  # Reference to object B

class B:
    def __init__(self):
        self.name = "Object B"
        self.ref_a = None  # Reference to object A

# Deserialize objects from a file
with open("cyclic_objects.pkl", "rb") as f:
    a, b = pickle.load(f)

# Check if the cyclic reference is intact
print(f"{a.name} -> {a.ref_b.name}")
print(f"{b.name} -> {b.ref_a.name}")
