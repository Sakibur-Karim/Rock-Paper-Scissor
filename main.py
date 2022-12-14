import random

choices = ['rock', 'paper', 'scissors']

win = 0
loss = 0
ties = 0

while True:
    print('%s Wins, %s Losses, %s Ties.' % (win, loss, ties))
    user_input = input('Choose rock(r), paper(p), or scissors(s): ')
    
