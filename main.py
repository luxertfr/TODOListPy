from task import addTask


def main() :
    print("Welcome in this TODO list")
    print("--- Main Menu ---")
    print("1. Add a new task")
    print("2. Remove a task")
    print("3. Complete a task")
    print("4. Edit a task")
    print("5. Working on it ...")
    print("6. Working on it ...")
    print("7. Working on it ...")
    print("8. Working on it ...")
    menu = input("Select a menu : ") 
    if menu == "1":
        addTask()
    elif menu == "2":
        print("2")
    elif menu == "3":
        print("3")
    elif menu == "4":
        print("4")
    elif menu == "5":
        print("5")
    elif menu == "6":
        print("6")
    else : 
        print("Try to write the number correctly.")
        
            
    