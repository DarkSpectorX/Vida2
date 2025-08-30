import string 

def word_find(num:list) -> list:
    """_summary_

    Args:
        num (list): number input

    Returns:
        list: vowel sounds and consonant sounds in number input
    """
    vowel = "aeiou"
    counter_vowel = 0
    counter_nvowel = 0
    
    for word in num:
        for c in word:
            if c in vowel:
                counter_vowel += 1
            elif c.isdigit() or c in string.punctuation:
                continue
            else:                    
                  counter_nvowel += 1

    return [counter_vowel, counter_nvowel]


def search_word (num:list) -> list:
    """_summary_

    Args:
        num (list): give lists 

    Returns:
        list: find char , str, number in Args
    """
    counter_char = 0
    counter_sign = 0
    counter_number = 0
    
    for word in num: # to catch array
        for c in word: # to access each char in word
            if c in string.punctuation: # or we can use ORD to declare signs!
                counter_sign += 1
            if c.isdigit():
                counter_number += 1
            if c.isalpha():
                counter_char+= 1
                
    return [counter_char, counter_number, counter_sign]



while 1:
    
    num_input = input("Add paragraph : ").split()
    print("a -> find char, num, sign\nb -> vowel and consonants sounds.\n")
    choose_usr = input(" Add a or 1 or b or 2 : ")
    print(20 * "-")
    
    
    match choose_usr:
        case 1 | "1" | "a":
            b = search_word(num_input)
            print(f"char :{b[0]}\nnumber : {b[1]}\nsign : {b[-1]}")
            continue
        case 2 | "2" | "b":     
            c = word_find(num_input)
            print(f"vowel :{c[0]}\nnvowel : {c[1]}\n")
            continue
        case _ :
            print("Invalid input ")
            print()
            
            continue
        