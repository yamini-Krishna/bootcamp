# pickle_serialize_person.py
import pickle
from person import Person

person = Person("Alice", ["Uni A", "Uni B"], ["Bob", "Charlie"])

with open("person.pkl", "wb") as f:
    pickle.dump(person, f)

print("Serialized person to person.pkl")
