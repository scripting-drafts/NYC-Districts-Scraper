import re
from sys import argv

script, input_file = argv

file = open(input_file)
convertedList = []

for line in file:
    convertedLine = re.sub('\,', '\",\"', line)
    convertedList.extend(convertedLine)

convertedList.insert(0, '[\"')
convertedList.append('\"]')

fileNew = open('fileNew.txt', 'w+')

for lines in convertedList:
    fileNew.write(lines)

fileNew.close()
