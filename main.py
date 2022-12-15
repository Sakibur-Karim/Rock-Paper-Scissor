import random

win = 0
lose = 0
ties = 0

print('ROCK, PAPER, SCISSORS')

while True:
    print('%s Wins, %s Losses, %s Tie' %(win,lose,ties))
    while True:
        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
        user_input = input()
        if user_input == 'r' or input == 'p' or input == 'q':
            break
    if user_input == 'r':
        print('Rock vs ')
    elif user_input == 'p':
        print('Paper vs ')
    elif user_input == 's':
        print('Scissor vs ')

    computer_input = random.randint(1,3)
    if computer_input == 1:
        output ='r'
        print('rock')
    if computer_input == 2:
        output ='p'
        print('paper')
    if computer_input == 3:
        output ='s'
        print('scissor')
    
    if user_input == output :
        print('ties')
        ties += 1
    if user_input == 'r' and output  == 'p':
        print('You win')
        win +=1