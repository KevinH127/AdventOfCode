import json

with open('Day2/day2.json', 'r') as input_text:
  input_text = input_text.read()

input_text = json.loads(input_text)

safe = 0

def is_safe(list_of_numbers):
  if int(list_of_numbers[0]) - int(list_of_numbers[1]) > 0:
    increase = 1
  elif int(list_of_numbers[0]) - int(list_of_numbers[1]) < 0:
    increase = 0
  else:
    return False

  match increase:
  
    case 0:
      for i in range(len(list_of_numbers)-1):
        if int(list_of_numbers[i]) - int(list_of_numbers[i+1]) not in [-1,-2,-3]:
          return False
      return True

    case 1:
      for i in range(len(list_of_numbers)-1):
        if int(list_of_numbers[i]) - int(list_of_numbers[i+1]) not in [1,2,3]:
          return False
      return True

for numbers in input_text:
  numbers = numbers.split()
  if is_safe(numbers):
    safe += 1

print(safe)


    