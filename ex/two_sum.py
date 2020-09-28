#
def twoSum(nums, target):
        h = {}
        for i, v in enumerate(nums):
            n = target - v
            if n in h:
                return [h[n], i]
            h[v] = i
        return []
nums = [0, 3, 6, 7, 10, 17]
target = 9
print(twoSum(nums, target))

#class
class solution:
    def twoSum(self, nums, target):
        h = {}
        for i, v in enumerate(nums):
            n = target - v
            if n not in h:
                h[v] = i
        return [h[n], i]

print(twoSum(nums, target))


#papa
def two(nums, target):
    l = len(nums)
    for i in range(l):
        for j in range(i+1, l):
            if nums[i]+nums[j] == target:
                return [i, j]
    return []
target = 30
print(two(nums, target))













