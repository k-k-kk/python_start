import csv

students = []

with open("students.csv") as file:
    reader = csv.reader(file)
    for name, home in reader:
        students.append({"name": name, "home": home})



for student in sorted(students, key = lambda student: student["name"]):   
    #key=你定义的函数 也行
    print(f"{student['name']} is in {student['home']}")       