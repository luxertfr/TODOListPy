def addTask() :
    print("Welcome here")
    while True:
        nameTask = input("How do you want to name the task : ")
        while True:
            verif = input(f"Do you want to name the task {nameTask} ? (yes/no) ").lower()
            if verif == "yes":
                print(f"{nameTask} has been added to your task.")
                return
            elif verif == "no":
                print("Let's try again")
                break
            else :
                print("Invalid input. Please answer 'yes' or 'no'.")
            
addTask()