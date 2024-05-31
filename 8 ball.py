##Author: Nate Weintraub
##Sources: Ms.Marciano, Mr.TA
##Date: 11/14/2023
##Bugs: One bug, or more so imperfection was that I had unnecessary lines of code. I ended up deleting some code, making it look nicer while staying just as efficient
Description:This is my code for my magic 8 ball, it gives random answers using my code

import random##Asking to Import Random later in that code

while True:##Starting a while true loop
    play = str.lower(input ("Want to play magic 8 ball"))##asks the user if they want to play magic 8 ball, then stores their response, in lowercase, in a variable play
    if play == "yes":##If the user says play
        question = input ("Ask a yes or no question then; ")##prompt the user for a question
        
        print (random.choice(["Yes", "No", "Ask Later", "No way", "50/50", "Maybe", "No shot, not in a million years", "Of course", "1 miilion percent% yes"]))##print a random response from the list
    elif play == "no":#otherwise if the user doesn’t want to play
        print("bye")#say bye
        break#break the loop
    else:#otherwise
        print("invalid!")#Print this, "Invalid!"

