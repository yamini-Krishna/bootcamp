import json

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def to_json(self):
        # Convert object to dictionary, then to JSON string
        return json.dumps({
            "title": self.title,
            "author": self.author,
            "pages": self.pages
        })

# Example usage
book = Book("Python Basics", "John Doe", 250)
json_string = book.to_json()
print(json_string)
