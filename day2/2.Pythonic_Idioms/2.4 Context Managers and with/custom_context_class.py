
class MyContext:
    def __enter__(self):
        print("Entering")
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting")
with MyContext():
    print("Inside")
# Output:
# Entering
# Inside
# Exiting
