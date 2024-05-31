#Name: Nate Weintrub
#Date: 5/13/2024
#Project Description:This is a system that helps keep your passwords! It has 4 options and you should try it out!
#Sources: Myself, Ms.Marciano, Google



webs = []#Makes webs equal an empty list that can be filled
users = []#Makes users equal an empty list that can be filled
pwds = []#Makes passwords equal an empty list that can be filled

while True:#Start of a while true loop for option
    webs.append(input("Website Name: "))#Letting user input website names into list
    users.append(input("Website Username: "))#Letting user input username names into list
    pwds.append(input("Website Password: "))#Letting user input passwords names into list
    print("Stored!")#Teeling the user that the info is stored

    done = input("Finished? ")#Then asking user if they are done

    if done == "yes":#If the user responds with yes
        break#Breaks the function, ends that portion of code

print ('''Option A: End code 
Option B: Add more website entries
Option C: Print all websites username and password 
Option D: Print specific website username password entry''')#This prints Option: and gives the user a choice based on which letter they click
while True:#Start of while true loop after they say what option
    choice = input("Option Choice: ")#Basically aking the user repsonse a input that could be A B C D either one

    if choice == "A":#If the input was A
        print("Ending Code") #Printing edning code
        break#Thens break the code and goes back to start
    elif choice == "B":#If the user chose option B
        webs.append(input("Website Name: "))#Using the while true loop at the top, saying add website name
        users.append(input("Website Username: "))#Using the while true loop at the top, saying add username name
        pwds.append(input("Website Password: "))#Using the while true loop at the top, saying add  name
        print("Stored!")#Just telling the user that the code is now stored and they can acess it!
    elif choice == "C":#If the users choice was C
        for i in range(len(webs)):#In range of the list, list of webs
            print (f'''web #{i+1}: {webs[i]}''')#Print the first set of webs, adds one to tell sets apart
            print (f'''user #{i+1}: {users[i]}''')#Prints the first set of users, add one to tell apart and organized
            print (f'''pwd #{i+1}: {pwds[i]}''')#Prints the firt set of passwords, add one to tell apart and organized
    elif choice == "D":#If the users choice was D
        print ("Please type in a stored website")
        website = input("Enter website: ")#Asking user to enter a specific website
        if website in webs:#If the website is in webs
            i = webs.index(website)#Website index, finding out if the website is in the list
            print (f'users: {users[i]}')#Then printing the username that comes along with it
            print (f'pwd: {pwds[i]}')#Then pritning the password that comes along with it
        if website not in webs:#If its not in the webs
            print ("Website not identifide, ending code")#Notifying the user that the code is ending
            break#breaking code, code ends, becuase the website was wrong
    
        