name = str(input("ENTER THE EMPLOYEE'S NAME: "))
tenure = int(input("TENURE: "))


if tenure >= 0 and tenure <= 5:
    print("You are a Bronze.")
elif tenure >= 6 and tenure <= 10:
    print("You're a Silver.")
elif tenure >= 11 and tenure <= 15:
    print("You're a Gold.")
elif tenure >= 16:
    print("You're a Platinum.")

age = int(input("What is your current age: "))
if age >= 60:
    print("You're eligible for retirement.")
else:
    print("You're not eligible for retirement.")