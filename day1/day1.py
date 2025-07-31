    # 🧠 Practice Problems for Linear Search + Python Basics

# 1: Find the Position
# Given a list of numbers and a target, return the index if found, else return -1.

list_a=[10, 20, 30, 40] 
target = 30 # Output: 2

def linearSearch(nums,target):
    for index in range(len(nums)):
        if nums[index]==target:
            return index
    
    return -1
print(linearSearch(list_a,target))




