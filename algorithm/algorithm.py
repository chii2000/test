#
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

#
def selection_sort(l):
    for i in range(len(l)-1):
        min_val = min(l[i+1:])
        min_ind = l.index(min_val)

        if l[i] > min_val:
            l[i], l[min_ind] = l[min_ind], l[i]
    return l

a = [1, 4, 2, 3, 8, 6]
print(selection_sort(a))

#
def insertion_sort(l):
    for i in range(1, len(l)):
        key = l[i]
        j = i - 1
        while j >= 0 and l[j] > key:
            l[j+1] = l[j]
            j -= 1

        l[j+1] = key
    
    return l

#
import bisect

def insertion_sort1(m):
    for k in range(1, len(m)):
        bisect.insort(m, m.pop(k), 0, k)
    return m

def merge_sort(l):
    if len(l) <= 1:
        return l

    mid = len(l) // 2
    left = l[:mid]
    right = l[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return list(merge(left, right))

def merge(left, right):
    merged = []
    l_i, r_i = 0, 0

    while l_i < len(left) and r_i < len(right):
        if left[l_i] <= right[r_i]:
            merged.append(left[l_i])
            l_i += 1
        else:
            merged.append(right[r_i])
            r_i += 1

    if l_i < len(left):
        merged.append(left[l_i:])
    if r_i < len(right):
        merged.append(right[r_i:])
    return merged


"""
    while len(left) > 0 and len(right) > 0:
        if left[0] > right[0]:
            l.append(left[0])
            del left[0]
        else:
            l.append(right[0])
            del right[0]

    if len(left) > 0:
        l.append(left)
    else:
        l.append(right)

    return l

"""

#
def quick_sort(l):
    if len(l) <= 1:
        return l

    pivot = l[0]
    right = []
    left = []

    for i in range(1, len(l)):
        if l[i] < pivot:
            left.append(l[i])
        else:
            right.append(l[i])

    r = quick_sort(right)
    l = quick_sort(left)

    return l + [pivot] + r

#
def liner_search(seq, tar):
    ind = 0
    s = len(seq)
    while ind < s:
        if seq[ind] == tar:
            return ind
        ind += 1

    return None

a = [1, 4, 6, 2, 5, 15]
b = 2
print(liner_search(a, b))