#Write a Python program to get a string made of the first 2 and the last 2 chars from a given string.
#If the string length is less than 2, return instead of the empty string.
while True:
    inp_string = str(input('Input a string '))
    length = len(inp_string)
    if length < 2 :
        continue
    else:
        print(inp_string[0:2] + inp_string[length - 2:length])
# Write a program that has a variable with your name stored (in lowercase) and then asks for your name as input.
# The program should check if your input is equal to the stored name even if the given name has another case, e.g.,
# if your input is “Anton” and the stored name is “anton”, it should return True.
name = 'dmytro'
if(input('Enter my name xD = ').lower() == name ):
    print('True')
else:
    print('False')

