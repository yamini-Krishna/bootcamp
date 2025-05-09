import sys

for line in sys.stdin:
    line = line.strip()          # Remove leading/trailing whitespace
    line = line.upper()          # Convert to uppercase
    print(line)                  # Print the result
