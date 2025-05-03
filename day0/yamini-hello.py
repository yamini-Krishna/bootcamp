import sys

def say_hello(name="world"):
    print(f"Hello, {name}!")

# If an argument is passed, use it; otherwise, use the default value.
if len(sys.argv) > 1:
    say_hello(sys.argv[1])
else:
    say_hello()
