import json
import re

with open('Day3/day3p1.json', 'r') as input_text:
  input_text = json.loads(input_text.read())

matches = re.findall(r'mul\((\d+),(\d+)\)', input_text)

total_sum = 0
for a, b in matches:
  total_sum += int(a) * int(b)
  
print(total_sum)
