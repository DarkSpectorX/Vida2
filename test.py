


result = [["mohammad", "najafi","021", "tehran"], ["ali", "jafari","021", "tehran"]]

while True:
    print("add a to edit\nadd b to remove\n add c to show phone book")
    choose2 = input("Add please : ").lower().strip()
    match choose2:
        case "a":
            search_input = input("Add your name : ").strip().split()
            try:
                if remove_usr[0] == person[0] and remove_usr[1] == person[1]:
                    result.pop(index)
                    continue
            except:
                print("Invalid input !!")
            else:
                print("This user doesn't Exist ...")
                continue 