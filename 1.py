def romanToInt(s: str) -> int:
    
    a = {"I" : 1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
    
    if len(s)<=1 :
        return a[s]

    result = romanToInt(s[0]) + romanToInt(s[1:]) 
    
    return result

print(romanToInt("IVX"))