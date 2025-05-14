import json

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    @classmethod
    def from_json(cls, json_string):
        # Convert JSON string back to dictionary
        data = json.loads(json_string)
        return cls(data["title"], data["author"], data["pages"])

# Example usage
json_input = '{"title": "Python Basics", "author": "John Doe", "pages": 250}'
book = Book.from_json(json_input)

print(book.title)
print(book.author)
print(book.pages)
