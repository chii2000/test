#添削2
def check_character(object, character):
    return object.count(character)

print(check_character([1, 2, 4, 5, 5, 3], 5))
print(check_character('orgjodjflwkejeeefia', 'e'))

#総合添削
def binary_search(numbers, target_number):
    low = 0
    high = len(numbers) - 1
    while low <= high:
        mid = (low + high) // 2
        if numbers[mid] == target_number:
            print('{0}は{1}番目にあります'.format(target_number, mid))
            return
        elif numbers[mid] < target_number:
            low = mid + 1
        else:
            high = mid - 1

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print(binary_search(numbers, 7))S

 