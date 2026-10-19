students = [
 ("Alice", 78),
 ("Bob", 45),
 ("Charlie", 90),
("Diana", 62),
("Kent", 30)
]

for name,score in students:
    print(f"Student name is: {name}, Student score is: {score}")


for name,score in students:
    if score >= 60:
        print(name)
        
count = 0
for name,score in students:
    if score >= 50:
        count = count + 1
print(f"Total of {count} student(s) passed")
