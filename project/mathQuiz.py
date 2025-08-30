import time as tm
import random as rnd

def questionGenerator ():
    
    # Step 1 -> generate two random numbers
    a = rnd.randint(1, 100)
    b = rnd.randint(1, a)
    
    # Step 2 -> Generate Operator 
    operator_list = [ "+", "-", "*"]
    selected_operator = rnd.choice(operator_list)
    
    print(f"{a} {selected_operator} {b} = ? ")
    
    match selected_operator:
        case "+":
            return a + b
        case "-":
            return a - b
        case "*":
            return a * b

my_result = ["Result   = "]
my_quest =  ["Question = "]
my_answer = ["myAnswer = "]
print("--------Welcome -------")
while True:
    
    print("\n\nadd 1 to start game \nAdd 2 to show my result\nAdd 3 to Reset your result!")
    choose = input("Add your choose : ").strip()
    match choose:
        case "1":
            try:
                question_number_limit = int(input("\nHow many math number : "))
            except:
                print("Invalid input ...")
                continue
                
            question_number = 0
            score = 0
            while question_number < question_number_limit:
                
                # step 1 -> Generate random question  (Done) 
                result = str(questionGenerator())
                start_time = tm.time()
                my_quest.append(result)
                
                # step 2 -> Get user answer (Done)
                user_input = input("\nEnter your Answer : ").strip()
                my_answer.append(user_input)
                # step 3 -> Check the answer time (Done) 
                end_time = tm.time()
                time_dif = end_time - start_time
                
                if time_dif < 5:
                    if result == user_input :
                        score += 1
                        my_result.append("✅")
                        print(f"Perfect ...✅")
                    else:
                        print(f"Wrong answer!❌")
                        my_result.append("❌")
                else :
                    print("you are too late ! ...")
                    my_result.append("❌")
                
                question_number += 1
                
        case "2":
            print(my_result)
            print(my_quest)
            print(my_answer)
        case "3":
            my_result = [my_answer[0]]
            my_quest  = [my_quest[0]]
            my_answer = [my_answer[0]]
        
        case _ :
            print("Invalid input")
            