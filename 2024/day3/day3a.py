import re

# Define the regex pattern
pattern = r"mul\(([1-9][0-9]{0,2}),([1-9][0-9]{0,2})\)"

# Open the text file
file_path = "input.txt"  # Replace with the path to your file
with open(file_path, 'r') as file:
    content = file.read()

# Find all matches in the file content
matches = re.findall(pattern, content)

# Print results
result = 0

if matches:
    for match in matches:
        result = result + (int(match[0]) * int(match[1]))

print(result)