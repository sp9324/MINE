grade = int(input("enter grade between 4 and 10: "))
performance = ""
gradeLetter = ""
if grade == 4:
    performance = "poor"
    gradeLetter = "D"

elif grade == 5:
    performance = "below average"
    gradeLetter = "C"

elif grade == 6:
    performance = "average"
    gradeLetter = "C+"

elif grade == 7:
    performance = "good"
    gradeLetter = "B"

elif grade == 8:
    performance = "very good"
    gradeLetter = "B+"

elif grade == 9:
    performance = "excellent"
    gradeLetter = "A"

elif grade == 10:
    performance = "outstanding"
    gradeLetter = "A+"

if 4 <= grade <= 10:
        print("your grade is", gradeLetter, "and", performance, "performance.")
else:
    print("out of range")
