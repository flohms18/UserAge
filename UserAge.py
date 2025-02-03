def UserAge():
    age = int(input("Enter your age: "))
    if age < 18:
        print("You are" + str(age) + "you are a minor.")
        
    else:
        print("You are" + str(age) + "you are a major.")

UserAge()