import pickle

# Define a custom collection class
class MyCollection:
    def __init__(self, items=None):
        self.items = items if items else []

    def add(self, item):
        self.items.append(item)

    # Serialize the collection to a file
    def save(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump(self, f)
        print(f"Collection saved to {filename}!")

# Create a collection and add items
my_collection = MyCollection()
my_collection.add("Item 1")
my_collection.add("Item 2")
my_collection.add("Item 3")

# Save the collection to a file
my_collection.save("my_collection.pkl")
