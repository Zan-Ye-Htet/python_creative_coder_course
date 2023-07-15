from urllib.request import urlretrieve

link = input('Image download link : ')

fileName = input('File Name : ')

urlretrieve(link, 'image/' + fileName + '.png')