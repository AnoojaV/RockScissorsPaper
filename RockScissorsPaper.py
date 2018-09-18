p1 = 'Scissors'
p2 = 'Rock'

if p1 == p2:
    print('draw')

elif p1 == 'Rock' and p2 == 'Scissors':
    print(p1)
elif p1 == 'Rock' and p2 == 'Paper':
    print(p2)

elif p1 == 'Paper' and p2 == 'Scissors':
    print(p2)
elif p1 == 'Paper' and p2 == 'Rock':
    print(p1)

elif p1 == 'Scissors' and p2 == 'Rock':
    print(p2)
elif p1 == 'Scissors' and p2 == 'Paper':
    print(p1)

else:
    print('You have not choosen anything ')