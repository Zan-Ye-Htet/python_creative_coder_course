#<------- Write ------->#

with open('./about.txt', 'w') as file:
    file.write('I am Zan Ye Htet.')
    file.write('\nI am 26 year old.')

# other work

with open('./about.txt', 'a') as file: # a = amend(add)
    file.write('\nI am currently learning data analysis and data science.')
    