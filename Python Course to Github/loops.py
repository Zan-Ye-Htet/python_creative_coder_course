#------- Loops -------#

names = ['Zan Ye Htet', 'Aung Aung', 'Kyaw Kyaw', 'John', 'Su Su']

for name in names:
    print(name)

colors = ['Blue', 'Pink', 'Yellow', 'Red', 'Black' ]

for color in colors:
    if color == 'Yellow':  # If this thig is false it will go down
        print(f'We got {color}.')
        # put ---break--- if we want to stop when we got our color
        break
    else :
        print(f'{color}.') # This will go up again

fruits = ['Apple', 'Orange', 'Watermelon']
for fruit in fruits:
    if fruit == 'Apple' or fruit == 'Orange':
        print(f'{fruit} is an fruit.')
    elif fruit == 'Watermelon':
        print(f'{fruit} is a fruit.')
    # else:
    #    print(f'{fruit} is a fruit.')
    