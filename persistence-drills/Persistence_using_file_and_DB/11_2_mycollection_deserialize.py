import pickle

# Define the same custom collection class
class MyCollection:
    def __init__(self, items=None):
        self.items = items if items else []

    def add(self, item):
        self.items.append(item)

    # Deserialize the collection from a file
    @staticmethod
    def load(filename):
        with open(filename, 'rb') as f:
            return pickle.load(f)

# Load the collection from a file
loaded_collection = MyCollection.load("my_collection.pkl")
print("Loaded collection items:", loaded_collection.items)
