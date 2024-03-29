#importing random module to choose random variables
import random

#importing string module to get all Alphabets in a single string
import string

#getting user input on number of characters in password
A = int(input('Enter the number of characters in password: '))

#using ascii_letters function to get all alphabets
Alphabet= string.ascii_letters

#taking numbers as string to avoid errors while concatenating strings
Numbers = str(1234567890)

Alphanumeric = Alphabet + Numbers

W = 1
while W == 1:
    #intializing an empty string 
    Password=''

    for i in range (A):
        B = random.choice(Alphanumeric)
        Password += B
    print(Password)
    
    Z=str(input('Are you satisfied with your password(enter"y" if yes)?: '))
    if Z == 'y':
        print('Thnaks for using password generator')
        W = 0
    else:
        print('Generated another password')
        W = 1