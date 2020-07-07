# the list "students" is already defined
#students = [["Will", "B"], ["Kate", "B"], ["Max", "A"], ["Elsa", "C"], ["Alex", "B"], ["Chris", "A"]]


len_students = len(students)
A_student= []

for i in range(0, len_students):
    ocena = (students[i])[1]
    if ocena == "A":
        A_student.append((students[i])[0])
    i += 1

print(A_student)