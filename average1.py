#!python3
# average1.py

numbers = []
sum     = 0
lowest  = None
highest = None

while True:
  try: 
    line = input("Enter number or Enter to finish: ")
    if not line:
      break
    number = int(line)
    numbers.append(number)
    sum += number
    if lowest is None or number < lowest:
      lowest = number
    if highest is None or number > highest:
      highest = number
  except ValueError as err:
    print(err)

numbers.sort()

print('Numbers: ', numbers)
print('Count = ', len(numbers), ' Sum = ', sum,
      ' Lowest: ', lowest, 'Highest: ', highest,
      ' Mean = ', sum / len(numbers))
