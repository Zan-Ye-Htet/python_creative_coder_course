#------- Class -------#
class Car:
    def __init__(self, name, wheels):
        self.name = name
        self.wheels = wheels
    
    def drive(self):
        print(f'{self.name} is driving.')

lambo = Car("Lamborghini", 4)
lambo.drive()

tesla = Car('Tesla', 4)
tesla.drive()

