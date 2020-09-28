def selection_sort(l):
    for i in range(len(l)-1):
        min_val = min(l[i+1:])
        min_ind = l.index(min_val)

        if l[i] > min_val:
            l[i], l[min_ind] = l[min_ind], l[i]
    return l

a = [1, 4, 2, 3, 8, 6]
print(selection_sort(a))
