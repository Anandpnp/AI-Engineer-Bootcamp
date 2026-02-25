numbers = [12,45,7,89,23,56,91]
total = 0
max_number = numbers[0]
min_number = numbers[0]
for number in numbers:
    total += number    
    if number > max_number:
        max_number = number       
    if number < min_number:
        min_number = number
average = total / len(numbers)        
print(f"Total: {total}")
print(f"Average: {average}")
print(f"Max: {max_number}") 
print(f"Min: {min_number}")

odd_count= 0
even_count= 0  
for number in numbers:
    if number % 2 == 0:
        even_count += 1        
    else:
        odd_count += 1
print(f"Even Count: {even_count}") 
print(f"Odd count: {odd_count}")        
          




   



