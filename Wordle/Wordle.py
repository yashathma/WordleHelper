from email.mime import text
from re import search
from subprocess import list2cmdline
import pandas

def hasLetter(given, word):
    for letter in given:
        if letter not in word:
            return False
    return True

def hasLetterAtInd(word, list):
    for letter in list:
        index = int(letter[2]) - 1
        char = letter[0]
        if word[index] != char:
            return False
    
    return True

def remove(word, given):
    for str in given:
        for char in str:
            if char in word:
                return False
    return True



txt = pandas.read_csv("/Users/yash/Desktop/Wordle/5LetterWords.csv")
txt = txt["Words"].tolist()

given = input("Which words do you know are in the word but dont know where they are?")
given = given.split(", ")
txtTwo = []

for word in txt:
    if hasLetter(given,word):
        txtTwo.append(word)

print("these are the words you can use now")
print(txtTwo)

given =input("Which letters do you know the indx of?")

given = given.split(", ")
txtThree = []

for word in txtTwo:
    if hasLetterAtInd(word,given):
        txtThree.append(word)

print("Here are the words you can use")
print(txtThree)


given = input('What are the useless words?')
given = given.split(", ")
txtFour = []
for word in txtThree:
    if remove(word, given):
        txtFour.append(word)

print("These are the words you can use:")
print(txtFour)

dict = {'a': 0, 'c': 0, 'b': 0, 'e': 0, 'd': 0, 'g': 0, 'f': 0, 'i': 0, 'h': 0, 'k': 0,
'j': 0, 'm': 0, 'l': 0, 'o': 0, 'n': 0, 'q': 0, 'p': 0, 's': 0, 'r': 0, 'u': 0, 
't': 0, 'w': 0, 'v': 0, 'y': 0, 'x': 0, 'z': 0}

for words in txtFour:
    for letter in word:
        print(letter)
        dict[letter] += 1


print(dict)







#print(given)
