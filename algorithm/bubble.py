def bubble(l):
    n = len(l)
    for i in range(n-1):
        swapped = False
        for j in range(n-1-i):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
                swapped = True
        
        if swapped == False:
            break

    return l

a = [1, 4, 7, 2, 5, 3, 10]
print(bubble(a))

