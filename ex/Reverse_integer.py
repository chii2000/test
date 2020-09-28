
"""
class solution:
    def reverse(self, x):
        for i in range(len(x)):
            for j in range(len(x-1), i, -1):
                if x[j] < x[j-1]:
                    x[j], x[j-1] = x[j-1], x[j]
        return x

def reverse1(x):
    for i in range(len(x)):
        if x[i] < x[i+1]:
            x[i], x[i+1] = x[i+1], x[i]
    return x
    if x[3] = 0:
        y = x.remove(0)
    return y
"""

def reverse(input):
    x = list(str(input))
    rev = x[::-1]
    return rev
    






    
        
            