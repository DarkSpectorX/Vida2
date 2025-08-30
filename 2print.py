usr_input = input("Add paragraph : ").split()

usr_dic = dict()

for word in usr_input:
    for char in word:
        usr_dic[char] = usr_dic.get(char, 0) + 1
        
sorted_usr_dic = dict(sorted(usr_dic.items()))    
print(sorted_usr_dic)