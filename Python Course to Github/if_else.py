#------- Condition -------#

age = int(input('age : '))

if age <= 18: 
    print('You are young!')
elif age >= 19 and age <= 60:
    print('You are middle age!')
else :
    print('You are old!')



tired = input('Are you tired? "y/n"')

if tired == 'y':
    print('Drink water.')
elif tired == 'n' :
    print('Get back to work!')
else:
    print('Enter only y or n!\n TO RUN AGAIN: \'python if_else.py\' in terminal!')