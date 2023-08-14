mark = int(input("Enter your marks: "))
print("mark:", mark)
if mark >= 80:
    print("A+")
elif mark >= 70:
    print("A-")
elif mark >= 60:
    print("B")
elif mark >= 50:
    print("C")
elif mark >= 40:
    print("Pass")
else:
    print("Fail")
