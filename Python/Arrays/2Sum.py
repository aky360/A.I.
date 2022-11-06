"""
Given an unsorted integer array, find a pair with the given sum in it.

Input:
nums = [8, 7, 2, 5, 3, 1]
target = 10
 
Output:
Pair found (8, 2)
or
Pair found (7, 3)
 
Input:
nums = [5, 2, 6, 8, 1, 9]
target = 12
Output: Pair not found
"""


def findPair(nums, target):
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                print('Pair found', (nums[i], nums[j]))
                return
 
    print('Pair not found')
 
 
if __name__ == '__main__':
 
    nums = [8, 7, 2, 5, 3, 1]
    target = 10
    findPair(nums, target)
    
    
#######################################################################################################################

def findPair(nums, target):
    nums.sort()
    (low, high) = (0, len(nums) - 1)
    
    while low < high:
        if nums[low] + nums[high] == target:        # target found
            print('Pair found', (nums[low], nums[high]))
            return
        # increment `low` index if the total is less than the desired sum;
        # decrement `high` index if the total is more than the desired sum
        if nums[low] + nums[high] < target:
            low = low + 1
        else:
            high = high - 1
 
    print('Pair not found')
 
 
if __name__ == '__main__':
 
    nums = [8, 7, 2, 5, 3, 1]
    target = 10
    findPair(nums, target)
    
#################################################################################################################################

# Function to find a pair in an array with a given sum using hashing
def findPair(nums, target):
    d = {}
 
    # do for each element
    for i, e in enumerate(nums):
 
        # if the difference is seen before, print the pair
        if target - e in d:
            print('Pair found', (nums[d.get(target - e)], nums[i]))
            return
 
        # store index of the current element in the dictionary
        d[e] = i
 
    print('Pair not found')
 
 
if __name__ == '__main__':
 
    nums = [8, 7, 2, 5, 3, 1]
    target = 10
    findPair(nums, target)
