isbn = int(input('ISBN:'))
total = 0
tenth = int(isbn % 10)
isbn = int(isbn / 10)
for x in range(9):
    numIs = int(isbn % 10)
    multiply = numIs * (9-x)
    total = total + multiply
    isbn = isbn / 10
lastNum = int(total % 11)
if lastNum == tenth:
    lastNum = lastNum * 10
    total = total + lastNum
    if total % 11 == 0:
        print('Legit')
    else:
        print('Not legit')
else:
    print('Not legit')
    
