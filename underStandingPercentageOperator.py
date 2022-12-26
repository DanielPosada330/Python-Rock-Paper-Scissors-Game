# Write your code here :-)

import sys
yeses = 0
nos = 0
while True:
    print('%s Y, %s N' % (yeses, nos))
    while True:
        print('Enterr your answer: (y)es (n)o or (q)uit')
        playerMove = input()
        if playerMove == 'q':
            sys.exit()
        if playerMove == 'y' or playerMove == 'n':
            break
    if playerMove == 'y':
        print('Yes')
        yeses = yeses + 1
    elif playerMove == 'n':
        print('No')
        nos = nos + 1
