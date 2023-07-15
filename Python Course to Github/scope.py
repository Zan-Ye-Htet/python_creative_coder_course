#------- Scope -------#

# Global
name = "Zan Ye Htet"

def sayMyName():
    # local
    name ="John"
    print(name)

sayMyName()

print(name)

# Global in Local
carType = "Oil"

def printCarType():
    # Updating Global Car Type locally 
    global carType
    carType ="Electric"
    print(name)

printCarType()

print(carType)