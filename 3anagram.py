# usr_string1= input()
# usr_string2= input()

# s1 = sorted(usr_string1)
# s2 = sorted(usr_string2)


# if s1==s2:
#     print("Anagram")
# else:
#     print("Not Anagram")

usr_string1= input().split()
usr_string2= input().split()

usr_dict1 =dict()
usr_dict2 =dict()

for word in usr_string1:
    for char in word:
        usr_dict1[char] = usr_dict1.get(char,0) + 1   

for word in usr_string2:
    for char in word:
        usr_dict2[char] = usr_dict2.get(char,0) + 1 
        

if usr_dict1 == usr_dict2:
    print("Anagram")
else:
    print("No Anagram")

    


