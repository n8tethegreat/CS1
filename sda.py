import random ##Telling for a random choice

computer = 0 ##Computer Score
player = 0 ##Player Score
while True: ##Start of While true loop
    play = str.lower(input("Want to play Rock Paper Scissors?" ))#Print value for plau

    if play == "yes":##If the person says yes code will continue
        user_rps = input ("Choose your weapon: ")
        
        if user_rps in ["rock", "paper", "scissors"]:##Saying if the player pets in something it will change to something
            bot_rps = random.choice(["rock", "paper", "scissors"])##Bot is going to pick from this list at random
            print ("Bot chose " + bot_rps)##Telling code to print what it chose _ is input score

            if user_rps == bot_rps:##Showing code that user and bot put in sma ething
                print("Tie")#Printing that this results in a tie
            elif user_rps == "scissors" and bot_rps == "paper":##Showing user chose scissors and bot chose paper
                player +=1##Adding 1 to player score
                print("You Win")##Telling code to print to user that they won
            elif user_rps == "rock" and bot_rps == "paper":##Telliung code that user chose rock and bot chose papaer
                computer +=1##adding 1 to computer score
                print ("You Lose")##Printing "You Lose"
            elif user_rps == "paper" and bot_rps == "rock":##Telling code that if user chooses paper and bot chooses rock..
                player +=1##Telling code to add 1 to player score
                print ("You Win")##Teling code to print "You win"
            elif user_rps == "paper" and bot_rps == "scissors":#Telling code that if user chooses paper and bot chooses scissors....
                computer +=1##Adding to computer score
                print ("You Lose")##Telling code to print you loses
            elif user_rps == "scissors" and bot_rps == "rock":#Telling code if user chooses scissors and bot chooses rock....
                computer +=1#Computer add 1
                print ("You Lose")#Prining you lose
            elif user_rps == "rock" and bot_rps == "scissors":##If user chooese rock and bot chooses scissors....
                player +=1##Player add 1
                print ("You Win")#Printing "You win"
            print ("computer score;", computer)#Telling code to print computer score
            print ("player score;", player)#Telling code to print player 

        else:#Elif Statement
            print("invalid")#Telling code to print invalid







