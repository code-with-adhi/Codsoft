#importing random module to make the program choose a random object in the list
import random

#initializing a list with valid inputs
Keys= ['ROCK', 'PAPER','SCISSORS']
print('***************RULES*************** \n1.You can only choose a valid input \n2.Each round contributes 1 point, player who wins a match gets 1 point \n3.If the match ends in draw nobody gets a point ')
print('Valid moves: ', Keys)
w=1
while w == 1:   
    score_a = 0
    score_z = 0
    AB = 0
    CD = 0
    while (score_a<5 or score_z<5) and ((AB != 1) or (CD != 1)):
        B = str(input('Enter your choice(rock or paper or scissors): '))
        A= B.upper()#using upper function so that the program won't be case sensitive
        Z = random.choice(Keys)
        if A in Keys:
            if A=='ROCK' and Z=='PAPER':
                score_z = score_z + 1
                print(f'Your Choice : {A} \nSystem Choice : {Z} \nSystem Wins')
                print(f'Your score : {score_a} \nSystem score: {score_z}')

            elif A=='ROCK'and Z== 'SCISSORS':
                score_a = score_a + 1
                print(f'Your Choice : {A} \nSystem Choice : {Z} \nYou Win')
                print(f'Your score : {score_a} \nSystem score: {score_z}')

            elif A=='PAPER' and Z=='ROCK':
                score_a = score_a + 1
                print(f'Your Choice : {A} \nSystem Choice : {Z} \nYou Win')
                print(f'Your score : {score_a} \nSystem score: {score_z}')

            elif A=='PAPER' and Z == 'SCISSORS':
                score_z = score_z + 1
                print(f'Your Choice : {A} \nSystem Choice : {Z} \nSystem Wins')
                print(f'Your score : {score_a} \nSystem score: {score_z}')
            
            elif A=='SCISSORS' and Z=='PAPER':
                score_a = score_a + 1
                print(f'Your Choice : {A} \nSystem Choice : {Z} \nYou Win')
                print(f'Your score : {score_a} \nSystem score: {score_z}')
            
            elif A == 'SCISSORS' and Z=='ROCK':
                score_z = score_z + 1
                print(f'Your Choice : {A} \nSystem Choice : {Z} \nSystem Wins')
                print(f'Your score : {score_a} \nSystem score: {score_z}')
            
            elif A == Z:
                print(f'Your Choice : {A} \nSystem Choice : {Z} \nDraw')
                print(f'Your score : {score_a} \nSystem score: {score_z}')
            
            if score_a == 5:
                print('You won the match \nTHANKS FOR PLAYIING\n')
                AB = 1
                break

            elif score_z == 5:
                print('System won the match\n THANKS FOR PLAYING\n')
                CD = 1
                break
        else:
            print('Enter a valid input')

    Y=str(input('If you like to play again enter"y: "'))
    if Y== 'y':
        w = 1
    else:
        w = 0
