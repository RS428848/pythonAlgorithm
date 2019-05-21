'''
Robert Song
CaesarCipher.py
05/13/19
This file is a program to encrypt or decrypt a Caesar Cipher Message
'''
string = str(input("Enter a string: "))
choice = int(input("Enter 1 for encrypt or 2 for decrypt: "))
positive = 0
while positive == 0:
    rot = int(input("Enter a positive integer for rotation: "))
    if rot>0:
        positive = 1
    else:
        positive = 0
lowerAlpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
upperAlpha = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
for letter in string:
    if letter.islower() == True:
        index = string.find(letter)
        letter = lowerAlpha[index+rot]
    elif letter.isupper() == True:
        index = string.find(letter)
        letter = upperAlpha[index+rot]
    else:
        letter = letter
print(string)