#Write a function that reverses a string. The input string is given as an array of characters s.

#You must do this by modifying the input array in-place with O(1) extra memory.

 

#Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
s = ["h","e","l","l","o"]

def revserOfStr(str):
    left,right=0,len(str)-1

    while left<right:
        str[left],str[right]=str[right],str[left]
        left+=1
        right-=1
    return str
print(revserOfStr(s))