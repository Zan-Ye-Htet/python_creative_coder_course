#------- Function -------#

def greet(name):
    print(f'Good day, {name}')

greet('John')

def greet2(name='Andrew'):
    print(f'Good day, {name}')

greet2()

def greet(name):
    print(f'Good day, {name}')

greet(name='Batman') # If there is another parameter, you can put it without positoinally