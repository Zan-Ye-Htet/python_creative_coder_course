#------- Class 2 -------#

class Car:
    sterringWheel = 1 # Class lvl attribute
    def __init__(self, name, wheels):
        self.name = name
        self.wheels = wheels
    
    def drive(self):
        print(f'{self.name} is driving.')

    @classmethod
    def common(cls): # cls not self
        print(f'All cars have only {cls.sterringWheel} sterring wheel.') # cls.classAttribute


Car.common()
