def userageinseconds(age):
    return age * 365 * 24 * 60 * 60


age = int(input("Enter your age:"))
print("The age is", userageinseconds(age))
