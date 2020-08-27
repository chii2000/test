"""
def palindrome(x):
    x1 = list(str(x))
    for i in range(x1):
        x1[i] = x1[len(x1)-i]
        y = x1
        y1 = len(y)
        for j in y1:
            
    return y1
    
    if x1 == y:
        return True
    else:
        return False

print(palindrome(134431))
"""
#再帰的
def palindrome(input):
    return palindrome2(list(str(input)))
def palindrome2(x):
    if len(x) > 2:
        return True
    if x[0] != x[len(x)-1]:
        return False
    return palindrome2(x[1:len(x)-1])

print(palindrome(134431))

#
def palindrome3(input):
    return palindrome4(list(str(input)))
def palindrome4(x):
    for i in range(len(x)//2):
        if x[i] != x[len(x)-i-1]:
            return False
    return True

print(palindrome3(14541))
print(palindrome3(34))

#
def palindrome5(input):
    x = list(str(input))
    rev = x[::-1]
    return x == rev

print(palindrome5(1551))









    



    

