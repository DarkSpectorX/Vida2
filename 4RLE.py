RED = "\033[91m"
GREEN = "\033[92m"
RESET ="\033[0m"


# sum all of char in string

# usr_string1 = input("Add string : ").split()
# usr_dict1=dict()

# for word in usr_string1:
#     for char in word:
#         usr_dict1[char] = usr_dict1.get(char,0) + 1   
        
# for key,value in usr_dict1.items():
#     print(f"{key}{value}" ,end="")
# print()

usr_string = input("Add string : ").strip()
if not usr_string:
    print("Invalid input")
else:
    temp =usr_string[0]
    counter = 1

    for i in range(1, len(usr_string)):
        if usr_string[i] == temp:
            counter += 1
        else:
            print(f"{RED}{temp}{GREEN}{counter}{RESET}",end="")
            temp = usr_string[i]
            counter = 1
    print(f"{RED}{temp}{GREEN}{counter}")
        
    

    