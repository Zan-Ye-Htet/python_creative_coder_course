lists = ['I am Zan Ye Htet.', '\nI am 26 years old.']

with open('./about_2.txt', 'w') as file:
    file.writelines(lists)