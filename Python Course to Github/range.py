#------- range() -------#

for num in range(7): #(exclusive)
    print(num)
print("")

for num in range(3,5): #(inclusive,exclusive)
    print(num)
print("")

for num in range(1,20,4): #(inclusive,exclusive,steps)
    print(num, end=" ")
print(" ")

for sth in range(3):
    print('Hello World')

# Rare but there a another way for looping with range
pizzas = ['chessy', 'spicy', 'mayo chicken', 'chicken chessy']
for num in range(len(pizzas)):
    print(pizzas[num])

# Normal way with putting numbers beside
num = 1
for pizza in pizzas:
    print(f'{num}.{pizza}')
    num+=1