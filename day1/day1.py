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


# 🔹 Problem 2: Check if Fruit Exists
# Given a list of fruits, return "Found" or "Not Found".

fruits=["apple", "banana", "mango"]
targetF = "grape"
# Output: "Not Found"

def fruitSearch(fruits,targetF):
    for fruit in fruits:
        if fruit==targetF:
            return "Found"
    return "Not Found"
print(fruitSearch(fruits,targetF))


#🔹 Problem 3: Count Occurrences

# Return how many times the target appears in the list.

list_b= [1, 2, 3, 2, 4, 2]
targetNum = 2

# Output: 3
def OccurecesNum(nums,targetNum):
    count=0
    for num in nums:
        if num==targetNum:
            count+=1
           
    return count
print(OccurecesNum(list_b,targetNum))


# 🔹 Problem 4: First and Last Occurrence
# Return the first and last index of a target element. If not found, return -1, -1.
list_c=[1, 2, 2, 3, 4, 2]
target_occ = 1
# Output: First: 1, Last: 5
def Occurrence_first_last(nums,target):
    index=[]
    for num in range(len(nums)):
        if nums[num]==target:
            index.append(num)
    if len(index)>=1:
        print(f"firs index {index[0]}, last index {index[-1]}")
    else:
        print(f"firs index: -1, last index:-1")

Occurrence_first_last(list_c,target_occ)




