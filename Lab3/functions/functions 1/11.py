def palindrome(s):
    
    s = s.replace(" ", "").lower()
    
    return s == s[::-1]


x = str(input())
print(palindrome(x))  
 