isbn = int(input('ISBN:'))
total = 0
#Taking the last number
tenth = int(isbn % 10)
isbn = int(isbn / 10)
#This part is for finding the sum of the first 9 numbers
for x in range(9):
    numIs = int(isbn % 10)
    multiply = numIs * (9-x)
    total = total + multiply
    isbn = isbn / 10
#Finding the last number through the sum
lastNum = int(total % 11)
#Check if the last number found through the sum is equal to the last number
#given by the input
if lastNum == tenth:
    total = total + (lastNum * 10)
    #Checking for the legitimacy for the 2nd time
    if total % 11 == 0:
        print('Valid')
    else:
        print('Invalid')
else:
    print('Invalid')
    
