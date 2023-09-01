print("Insert three grades to evaluate your grades.")
x = int(input("Science: "))
y = int(input("Math: "))
z = int(input("Research: "))

grades = [
    ["Science",x],
    ["Math",y],
    ["Research",z]
]

average = int((x+y+z)/3)
def honors(average):
    if average > 100 or average <= 50:
         print("Invalid Grade. Please Try again.")
    elif average >= 98:
        print("You have with highest honors. Congratulations!")
    elif average >= 95:
        print("You have with high honors. Congratulations!")
    elif average >= 90:
        print("You are with honors. Congratulations!")
    elif average >= 75:
         print("You passed.")
    elif average < 75:
          print("You failed.")

failGrades = []
for i in grades:
    failGrades.append(i[1])

failed = []
for a in failGrades:
    if a < 75:
        failed.append(a)

failedSubj = []
passedSubj = []
for subject in grades:
    if subject[1] < 75:
        failedSubj.append(subject[0])
    elif subject[1] > 75:
        passedSubj.append(subject[0])

if len(failed) != 0 and average > 51:
    print("You failed in " + str(len(failed)) + " subject(s) with the grade of " + str(failed) + " in " + str(failedSubj) + ".")

if average > 75 and average <= 100 and len(failed) == 0:
    print("You passed all subjects "+str(passedSubj)+" with an average of "+str(average)+".")
    honors(average)
elif average > 75 and len(failed) != 0:
    print("Despite having failed subject, you passed with an average of "+str(average)+".")
    honors(average)
elif average < 51:
    honors(average)
elif average < 75 and average >= 51 and len(failed) != 0:
    print("Since you failed most of your subject, your average is only "+str(average)+".")
    honors(average)
else:
    honors(average)