Flower pot?
print("Alarm!") #Telling code to print Alarm
snooze = input ("Snooze?")#Telling code that the input for when "Snooze" is shown is snooze
    
if snooze == "yes":#Varible if snooze
    while True:#Creating a while true loop
        print ("Alarm!")# Telling code to print Alarm
        snooze = input ("Snooze?")#Inupot of snooze
        if snooze == "yes":#If statement saying if yes do this
            continue#Saying if yes repeat while true loop
        elif snooze == "no":#If no breaks while true loop
            break#break while true loop
        else:#Else Statement
            print("invalid input") #Telling code to prind invalid input if another answer pops up       

elif snooze == "no":#Saying outside of while true loop
    print ("get out of bed")#telling code to print "Get out of Bed"

shower_brush = input ("Shower and brush teeth?")#Input of shower and brush teath

if shower_brush == "yes":#If Statement
    print ("Smelling good! Walking downstairs")#Print Smelling good! Walking Downstairs

elif shower_brush == "no":#Elif Statement
    print ("Very smelly")#Print very smelly

sayhitomom = input ("Say hi to Mom?")#Diffrent input from actually print

if sayhitomom == "no":#If Statement
    while True:#While True Loop
        print ("Get attacked and die")# Print "get Attacked and die"
        sayhitomom = input ("Say hi to mom?")#Input again
        if sayhitomom == "no":#If Statement
            continue#Telling code to continue while true loop
        elif sayhitomom == "yes":#Diffrent input
            break#Breaks while true loop
        else:#Else..
            print ("invalid input")#If anything else just say "Invalid input"

bikewalk = input ("Bike or take bus to school")#Input of bikewalk

if bikewalk == "bike":#If statement
    print ("Got on the bike, biked to school")#If "bike" print "Got on the bike, biked to school"
elif bikewalk == ("take bus"):#Telling code with another elif statement after if statement
    print ("Took the bus to school")#Tellung code to print "Took bus to school if input is take bus
print ("Thank you for hel;ing me do my morning routine! Now I am at school and ready to learn!")#A thank you and a ending to my code! Thanks !


