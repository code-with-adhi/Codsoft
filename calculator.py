#initializing a variable for while loop
W = 1

while W == 1:
    #getting user input for 1st integer
    A = int(input('Enter an integer: '))

    #getting user input for the operator
    B = str(input('Enter an operator: '))

    #getting user input for 2nd integer
    C = int(input('Enter an integer: '))

    #for addition operation
    if B == '+':
        D = A+C

    #for subtraction operation
    elif B == '-':
        D = A-C

    #for multiplication operation
    elif B == '*':
        D = A*C

    #for division operation
    elif B == '/':
        D = A/C
    
    #for floor division operation
    elif B == '//':
        D = A//C

    print('The answer is: ', D)

    I = str(input('To continue press "y" and to terminate press "n": '))

    if I == 'y':
        W = 1
    
    else:
        W = 0
