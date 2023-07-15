
words = ['apple', 'orange', 'lemon', 'lime', 'banana']
from random import randint
def randomSentenceGenerator(word):
    randomIndex = randint(0,len(words)-1)
    return f'{words[randomIndex]} {word}'

with open('./text.txt') as file:
    paragraph = file.read()
    wordLists = paragraph.split()
    list(map(randomSentenceGenerator, wordLists))
    sentenceList = list(map(randomSentenceGenerator,wordLists))
    paraCount = int(input('paragraph count : '))

    for count in range(paraCount):
        with open('./generator.txt', 'a') as write_file:
            write_file.write(''.join(sentenceList) +'\n\n')