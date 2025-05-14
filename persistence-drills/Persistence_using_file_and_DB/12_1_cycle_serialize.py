import pickle

class A:
    def __init__(self):
        self.name = "Object A"
        self.ref_b = None  # Reference to object B

class B:
    def __init__(self):
        self.name = "Object B"
        self.ref_a = None  # Reference to object A

# Create instances of A and B
a = A()
b = B()

# Create a cyclic reference
a.ref_b = b
b.ref_a = a

# Serialize objects to a file
with open("cyclic_objects.pkl", "wb") as f:
    pickle.dump((a, b), f)
print("Cyclic objects saved.")
