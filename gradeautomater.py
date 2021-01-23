print("THIS PROGRAM WILL HELP YOU AUTOMATE THE GRADING SYSTEM")
SUBJECT1 = float(input(" Please enter Marks: "))
SUBJECT2 = float(input(" Please enter score: "))
SUBJECT3 = float(input(" Please enter Marks: "))
SUBJECT4 = float(input(" Please enter Marks: "))
SUBJECT5 = float(input(" Please enter Marks: "))

total = SUBJECT1 + SUBJECT2 + SUBJECT3 + SUBJECT4 + SUBJECT5
percentage = (total / 500) * 100

print("Total Marks = %.2f"  %total)
print("Marks Percentage = %.2f"%percentage)

if(percentage >= 90):
    print("A Grade")
elif(percentage >= 80):
    print("B Grade")
elif(percentage >= 70):
    print("C Grade")
elif(percentage >= 60):
    print("D Grade")
elif(percentage >= 40):
    print("E Grade")
else:
    print("FaiL")
