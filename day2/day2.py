#🔢 Write a program to search for an element in a list and return "Found" or "Not Found" (Don’t return index).

list_a=["shiva","jayamma",4,"Anjaneyullu"]

if "shiva" in list_a:
    print("Found")
else:
    print("Not Found ")

#✍️ Ask the user to input a list of names. Then search for a given name using input()

def userInputSeach(list_a,userInput):
    word=userInput
    if word in list_a:
        return "Found"
    return "Not Found"
userInput=input("Please Enter Name: ")
print(userInputSeach(list_a,userInput,))