marks = int(input("enter your marks"))

if marks>=90:
        grade ="Ex"
elif marks>=70:
        grade = "A"
elif marks>=50:
        grade = "B"
elif marks>=30:
        grade = "fail"

else:
        grade = "F"

print("your are grade is: ",grade)                                