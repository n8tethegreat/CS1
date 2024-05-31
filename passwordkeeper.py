#Name: nate Weintraub
#Title: Function Mashup
#Date: 5/29/2024
#Sources: Myself, Ms.Marciano, T/A
#Description: This is my function mashup, here are all of the functions I was required to make all in one program. There area  a series of functions ranging from a song to adding numbers

import random#Import random statement

def chorus():#Start of the function saying that this is the chorus
    print ("Twinkle Twinkle")#First line of the chorus
    print ("Little Star")#Second and last line of the chorus
def sing():#Start of function then saying that this is the song
    chorus()#Calling chorus
    print ("How I wonder what you are")#Printing part of song
    print ("Up above the world so high, like a diamond in the sky")#printing part of song
    chorus ()#Calling Chorus
def add (num1, num2):#Start of function #2
   #Stating that the addition is a number plus a different number
    print(num1+num2) #Returning the other line
def print_list(print_list):#New function started to print a list vertically
    for element in print_list:#Asking that for the amount of people in the list...
        print(element)#Prints all the players vertically
def in_list(list, element):#New function choosing whether of not a certain element is on a certain list
    return element in list#If statement if an element is on the list
def is_integer(integer):#new function choosing if a number is an integer
    if "-" in integer:
        integer = integer[1:]
    return integer.isnumeric()#uf statement if the number is numeric                         
def randomnumber():#New function starting
    low = input("low number: ")#Setting the low limit, when it is the low limit
    high = input("high number: ")#Setting the high limit, when it is the high limit
    while True:#While true loop
        if is_integer(low):#If the number is small
            break
        else:#Else if it is not
            print("Please enter an integer")
    while True:#While true loop
        if is_integer(high):#If the number is big
            break
        else:#Else statement if not
            print("Please enter an integer")
    print(random.randint(int(low),int(high)))#Telling then to return a random integer
def replace_character(string, old_ch, new_ch):#Start of new function
    new_string=""#Descriving a new string not the old string

    for s in string:#Saying that for the s in the string
        if old_ch == s:#The old character
            new_string += new_ch#Adding
        else:#Else statement for different string
            new_string += s#Creating a new string
    return new_string#Returning the new string
def main():
    sing()#Calling Sing
    print(replace_character("hello world","l","a"))#Prints the final thing relpacing the correct letter for "Heaao Worad"
    add(5, 6)
    soccer_players = ["Roanldo","Cole Palmer","Marcus Rashford","Christian Pulisic"]#List of soccer players I chose
    print_list(soccer_players)
    list = ["A","B","C","D, E"]#List of the elements
    element = "jhhjsagdsfh"#The element (Which is clearly not on the list)
    print (in_list(list, element))#Asking if the element is on the list and printing false
    integer = "4"#What the integer is
    print (is_integer(integer))#then printing the integer if its true or false
    randomnumber()#then printing the random number

    main ()#Calling all functions

