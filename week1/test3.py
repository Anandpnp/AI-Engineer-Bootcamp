for i in range(5):
    print(i)

for j in range(0,4):
    print(j)

for k in range(1,18,5):
    print(k)

numbers = [0,5,7]
total =0
for numb in numbers:
    total = total + numb
print(total)

numbersm = [5,10,15,3]
max_number = numbersm[0]
for number in numbersm:
    if number > max_number:
        max_number = number
print(max_number)
