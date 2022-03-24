# Author: CCG 3/2/22

grades = {"End S1 Labs":0, "Start S2 Labs":100, "Mid-year Project Proposal":100, "Cycle 10 Practice Quiz":100, "Cycle 10 Quiz":0}

print(grades)

for assign in grades:
    print(assign)

for assign, grade in grades.items():
    if grade >= 70:
        print(assign, grade)

for assign, grade in grades.items():
    if grade >= 50:
        print(assign, grade)
