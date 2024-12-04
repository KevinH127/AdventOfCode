import json
import re

with open('Day3/day3p2.json', 'r') as input_text:
    input_text = json.loads(input_text.read())

ignore_mul = False
total_sum = 0

segments = re.split(r"(don't\(\))|(do\(\))", input_text)

for segment in segments:
    if segment is None:
        continue  
    if "don't()" in segment:
        ignore_mul = True  
    elif "do()" in segment:
        ignore_mul = False  
    elif not ignore_mul:
        matches = re.findall(r'mul\((\d+),(\d+)\)', segment)
        for a,b in matches:
            total_sum += int(a) * int(b)

print(total_sum)
