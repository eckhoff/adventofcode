import re

# Define the regex patterns
pattern = r"mul\(([1-9][0-9]{0,2}),([1-9][0-9]{0,2})\)"
block_pattern = r"don\'t\(\).*?do\(\)"

# Read the file content
file_path = "input.txt"  # Replace with your file path
with open(file_path, 'r') as file:
    content = file.read()

# Remove text inside "don't()...do()" blocks
excluded_content = re.sub(block_pattern, "", content, flags=re.DOTALL)

# Find all valid `mul(x,y)` occurrences outside the excluded blocks
matches = re.findall(pattern, excluded_content)

# Calculate the result
result = 0
if matches:
    for match in matches:
        result += int(match[0]) * int(match[1])

print("Result:", result)



