names = []

grades = []

for i in range(5):
    
    name = input("Enter a students name: \n")
    
    names.append(name)
    
    grade = int(input("Enter that person's grade (in %): \n"))
    
    grades.append(grade)
    
print(max(grades))

max_val = max(grades)

position = grades.index(max_val)

print(names[position])

avgG = sum(grades)

av = avgG/len(grades)

print(av)
    