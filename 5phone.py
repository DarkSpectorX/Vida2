def show():
    print(2*"\n")
    print(20 * "-")
    print("\033[92mAdd 1 to create (first name, last name, phone, address)")
    print("Add 2 to modify (first name, last name, phone, address)")
    print("Add 3 to search (first name, last name, phone, address)\033[m")
    
    
def get_input(pr):
    v = input(pr).strip()
    return None if v.lower() == "n" else v

result =[]
while True:
    show()
    choose = input("Add you'r choosen : ").strip()
    match choose:
        # Add user
        case "1" : 
            first_name =input("Add first name : ").strip()
            if first_name.lower() == "n":
                continue
            last_name = input("Add lase name : ").strip()
            if last_name.lower() == "n":
                continue
            phone =input("Add phone number : ").strip()
            if phone.lower() == "n":
                continue
            address =input("Add address number : ").strip()
            if address.lower() == "n":
                continue
            new_contact = [first_name,last_name,phone,address]
            result.append(new_contact)
        
        #Remove, Edit, Show User        
        case "2":
            print("add a to edit\nadd b to remove\n add c to show phone book")
            choose2 = input("Add please : ").lower().strip()
            match choose2:
                #Edit user
                case "a":
                    edit_usr = input("Which user you want to edit it ? ...(Just first name and last name...)").split()
                    if edit_usr == "n":
                                    break
                    for index,person in enumerate(result):
                        try:
                            if edit_usr[0] == person[0] and edit_usr[1] == person[1]:
                                first_name =input("Add first name : ").strip()
                                if first_name.lower() == "n":
                                    break
                                last_name = input("Add lase name : ").strip()
                                if last_name.lower() == "n":
                                    break
                                phone =input("Add phone number : ").strip()
                                if phone.lower() == "n":
                                    break
                                address =input("Add address number : ").strip()
                                if address.lower() == "n":
                                    break
                                new_contact = [first_name,last_name,phone,address]
                                result[index] = new_contact
                        except:
                            print("Invalid input")    
                #Remove user
                case "b":
                    remove_usr = input("Which user you want to remove it ? ...(Just first name and last name...)").split()
                    
                    for index,person in enumerate(result):
                        try:
                            if remove_usr[0] == person[0] and remove_usr[1] == person[1]:
                                result.pop(index)
                                continue
                        except:
                            print("Invalid input !!")
                        else:
                            print("This user doesn't Exist ...")
                            continue 
                
                #Show phone book
                case "c":
                    print(result)
                
        case "3":
            search_input = input("Add your name : ").strip().split()
            for person in result:
                if person in search_input:
                    print(result[person])
                    
        case _ :
            print("\nInvalid input")
                
                    

    
    