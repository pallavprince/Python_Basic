
### This the code for popular game rock, paper, scissors
### Player vs Computer

from random import randint

print (' Welcome to Game:''\nrock - paper - scissors''\nYou will get 10 chance to play\n')
i=0
ps=0
cs=0
while i<10:


    player=input('\nrock(r), paper(p), scissors(s): ')
    
    if player=='p' or 's' or 'r':

        print('You=', player, 'vs Computer=', end=' ')
        computer=randint(1,3)
        if computer== 1:
            comp='r'
        elif computer ==2:
            comp='p'
        elif computer ==3:
            comp='s'
        print(comp)
        if player==comp:
            print('Draw!')
        elif player=='p' and comp=='r':
            print ('You Win!')
            ps=ps+1
        elif player == 'p' and comp=='s':
            print ('computer win')
            cs=cs+1
        elif player == 's' and comp=='p':
            print ('You Win!')
            ps=ps+1
        elif player == 's' and comp=='r':
            print ('computer win')
            cs=cs+1
        elif player == 'r' and comp=='s':
            print ('You Win!')
            ps=ps+1
        elif player == 'r' and comp=='p':
            print ('computer win')
            cs=cs+1
        print('score: Computer=',cs,'You=',ps)

        i=i+1


if cs>ps:
    print("\n*****Match Over and You Loss!*****\n")

elif ps>cs:
    print("\n*****Match Over and You Win!*****\n")
    
elif ps==cs:
    print("\n*****Match Over and Draw!*****\n")
    
