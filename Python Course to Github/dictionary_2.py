#------- Dictionary_2 -------#
person = {}

key = input('key :')
name = input('name :')

person[key] = name

print(person)

print(person['name'])


while True:
    key = input('key :')
    name = input('name :')
    person[key] = name

    another = input('another y/n:')
    if another == 'y':
        continue
    else:
        break
print(person)