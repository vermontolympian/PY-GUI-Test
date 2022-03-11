#!/usr/bin/python
from inspect import _void
import random
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import StringVar
from turtle import color
from email import message
import random

def charEncode(character, b):
    '''
    This function takes in a character and the base it needs to be encoded in
    it then converts the character to ASCII
    then converts the base 10 number into base b
    '''
    x = ord(character)

    assert(x >= 0) 
    assert(1< b < 37) 
    r = '' 
    import string 
    while x > 0: 
        r = string.printable[x % b] + r 
        x //= b 
    return r
    charEncode()

def charDecode(character, b):
    '''
    This function takes in an encoded character and the base it is in
    it then converts the number (character) from base b to base 10
    then it converts the base 10 number (ASCII) into a normal character
    '''
    assert(1 < b < 37) 
    charInt = int(character, b)
    return str(chr(charInt))
    charDecode()

def Encode(msg):
    #Picks a random int from 3 to 9 to use as the base
    base = random.randint(3,9)

    print("Encoding message...")
    print("")
    
    #Creates the message to be returned
    encodedMessage = "*" + str(base)

    #Encodes each individual character in the base and appends it to the string that is to be returned
    for i in range(len(msg)):
        character = msg[i]
        encodedChar = charEncode(character, base)
        # print(encodedChar)
        encodedMessage += ":" + encodedChar
    
    encodedMessage += "*"
    print(encodedMessage)
    print("")
    return encodedMessage
    Encode()

def Decode(msg):
    print("Decoding message...")
    print("")
    decodedMsg = ""
    base = int(msg[1])

    #Remove '*'
    shortMsg = msg.replace("*", "")

    #Remove base
    withoutBase = shortMsg[2:]

    #Split the string into each character
    splitMsg = withoutBase.split(":")

    #Decode each character and add them to the message
    for i in range(len(splitMsg)):
        decodedMsg += charDecode(splitMsg[i], base)
    
    print(decodedMsg)
    print("")
    return decodedMsg
    Decode()

while 1:
    #Takes in keyboard input into the terminal and saves it as the message
    message = input("Type message here: ")  
    if message[0] == "*":   #Determines if the message is already encoded
        Decode(message)
    else:
        Encode(message)
    