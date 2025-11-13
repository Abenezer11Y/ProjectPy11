string = input("Enter your string ")

string1 = ('')
for i in string:
    string1 = i + string1

print("The original string is: ", string)
print("The reversed string is: ", string1)