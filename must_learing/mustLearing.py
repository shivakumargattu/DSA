# Write a program to print the exact phrase "Hello, World!"

user=input(" Please Enter user name: ")
print("Hello " + user + " Nice to meet you")

# Write a function that takes an integer and returns "Even" if the number is even, otherwise "Odd."

def isEven(num):
    if num%2==0:
        print("Even Number")
    else:
        print("Odd Number")
num=int(input( "Please Enter Number"))
isEven(num)

# Write a function that concatenates two given strings and returns the result.
twoStr="Shiva Kumar"
withouSpace=""
for i in twoStr:
    if i==" ":
        withouSpace+=""
    else:
        withouSpace+=i

print(withouSpace)


