#<------- Decorator ------->#
def greet(func):

    def wrapper():
        #before
        print('Hello')
        func()
        #after
        print('Good bye')
    return wrapper


@greet
def sayName():
    print('Zan Ye Htet')

sayName()

#<------- Decorator ------->#
""" 
def greet(func):

    def wrapper(name):
        #before
        print('Hello')
        func(name)
        #after
        print('Good bye')
    return wrapper


@greet
def sayName(name):
    print(name)

sayName('John') 

"""