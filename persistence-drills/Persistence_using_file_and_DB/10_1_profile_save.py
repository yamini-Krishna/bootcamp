import pickle

class Profile:
    def __init__(self, name, email):
        self.name = name
        self.email = email

# Create and save an old profile
profile = Profile("Yamini", "yamini@example.com")

with open("profile.pkl", "wb") as f:
    pickle.dump(profile, f)
print("Old profile saved.")
