students = []
eligible_students = []
not_eligible = []
MIN_AGGREGATE = 75
MIN_SUBJECT_MARKS = 60
MIN_ATTENDANCE = 75
MAX_INCOME = 200000
n = int(input("Enter number of students: "))
for i in range(n):
    print("\nEnter details of Student", i + 1)
    name = input("Enter student name: ")
    marks = []
    for j in range(5):
        mark = float(input("Enter subject " + str(j + 1) + " marks: "))
        marks.append(mark)
    attendance = float(input("Enter attendance percentage: "))
    income = float(input("Enter annual family income: "))
    aggregate = sum(marks) / len(marks)
    student = {
        "name": name,
        "marks": marks,
        "aggregate": aggregate,
        "attendance": attendance,
        "income": income
    }
    students.append(student)
    if (aggregate >= MIN_AGGREGATE and
        min(marks) >= MIN_SUBJECT_MARKS and
        attendance >= MIN_ATTENDANCE and
        income <= MAX_INCOME):
        eligible_students.append(student)
    else:
        not_eligible.append(student)
eligible_students.sort(
    key=lambda x: (
        -x["aggregate"],
        -x["attendance"],
        x["income"],
        x["name"].lower()
    )
)
print("\n===== ELIGIBLE STUDENTS =====")
if len(eligible_students) > 0:
    print("Rank\tName\t\tAggregate\tAttendance\tIncome")
    for rank, student in enumerate(eligible_students, start=1):
        print(
            rank, "\t",
            student["name"], "\t\t",
            round(student["aggregate"], 2), "%\t\t",
            student["attendance"], "%\t\t",
            student["income"]
        )
else:
    print("No students are eligible for scholarship.")
print("\n===== NOT ELIGIBLE STUDENTS =====")
for student in not_eligible:
    print(student["name"])
print("\nTotal Students:", n)
print("Eligible Students:", len(eligible_students))
print("Not Eligible Students:", len(not_eligible))
print("\nScholarship Allocation Process Completed!")
