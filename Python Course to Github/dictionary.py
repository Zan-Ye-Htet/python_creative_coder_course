#------- Dictionary -------#

person = {
    'name': 'Zan Ye Htet',
    'age': 26
}

person['hair_color'] = "black" # Even though double quotes it will covert to single quotes
print(person)

# Asking if there's sth in dictionary
print('age' in person)

#------- "in" logic in dictionary -------#  

if 'name' in person: 
    print('Someone\'s here')  

#------- Change keys into list -------#

person_key_2_list = list(person.keys())
print(person_key_2_list)

#------- Change values into list -------#

person_value_2_list = list(person.values())
print(person_value_2_list)