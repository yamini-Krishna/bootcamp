import pickle

class Profile:
    def __init__(self, name, email, phone=None):
        self.name = name
        self.email = email
        self.phone = phone

    def __setstate__(self, state):
        # Add missing keys for older versions
        if 'phone' not in state:
            state['phone'] = "Not provided"
        self.__dict__.update(state)

# Load the old version
with open("profile.pkl", "rb") as f:
    loaded_profile = pickle.load(f)

print(f"Name: {loaded_profile.name}")
print(f"Email: {loaded_profile.email}")
print(f"Phone: {loaded_profile.phone}")
