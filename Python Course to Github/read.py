#<------- Read ------->#

""" 
file = open('./text.txt')

for line in file:
    print(line)

file.seek(0) # To go back the cursor to the start

lineLists = file.readlines()
print(lineLists)


file.seek(50)

paragraph = file.read(100)
print(paragraph)

file.close() """ # have to close  

# Good thing about this way is we don't have to close 
with open('./text.txt') as file:
    for line in file:
        print(line)

print('other work')