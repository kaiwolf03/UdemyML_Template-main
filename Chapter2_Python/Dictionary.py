students = {"Ben": 1, "Kaya": 2, "Peter": 1, "Tobi": 4}
print(students)

student1 = students["Ben"]
print(student1)

students["Ben"] = 6
print(students)

students["Julia"] = 1
print(students)

students.pop("Julia")
print(students)

for key in students:
    print(key)

for key in students.values():
    print(key)

for key, value in students.items():
    print(key, value)
