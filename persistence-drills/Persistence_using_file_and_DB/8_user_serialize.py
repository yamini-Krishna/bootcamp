import json

class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password  # Sensitive info

    def to_safe_json(self):
        # Only include non-sensitive info
        return json.dumps({
            'username': self.username,
            'email': self.email
        })

# Example usage
user = User("yamini", "yamini@example.com", "secret123")
safe_json = user.to_safe_json()
print(safe_json)
