skills = ["QA", "Python", "Automation", "Java", "AI"]
print(skills[0])
print(skills[1])
print(skills[2])
print(skills[3])
print(skills[-1])
skills.append("PlayWright")
print(len(skills))
skills.append("Selenium")
print(len(skills))
skills.remove("Python")
print(len(skills))
skills.remove("QA")
print(len(skills))
for skill in skills:
    print(skill)
    
numbers = [5, 10, 15, 20, 25, 30]
print(numbers[0])
print(numbers[-1])
print(len(numbers))
numbers.append(35)
numbers.remove(10)
for number in numbers:
    print(number)

for number in numbers:
    if number % 2 == 0: 
        print(f"{number} is Even") 
    else:
        print(f"{number} is Odd")

