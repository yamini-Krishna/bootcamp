# pickle_deserialize_person.py
import pickle
from person import Person  # Needed so pickle knows the class

with open("person.pkl", "rb") as f:
    loaded_person = pickle.load(f)

print(loaded_person.name)
print(loaded_person.institutions)
print(loaded_person.colleagues)
