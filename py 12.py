class student:
    roll = " "
    gpa = " "
rahim = student()
print(isinstance(rahim,student))
rahim.roll = 123
rahim.gpa = 3.96
print(f"roll:{rahim.roll},gpa:{rahim.gpa}")