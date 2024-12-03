import json

with open('Day1/day1.json', 'r') as input_text:
  input_text = input_text.read()

input_text = json.loads(input_text)

left = []
right = []

for i in input_text:
  left.append(int(i.split()[0]))
  right.append(int(i.split()[1]))

right = sorted(right)
left = sorted(left)

answers = []
for i in range(len(right)):
  answers.append(abs(right[i] - left[i]))

print(sum(answers))
