import random
Food = ["Baconator Jr.", "Chicken Burger", "Cheeseburger","Quadruple Mega Burger", "Plain Bread Burger","Healthy Burger", "Chicken Tenders", "Bacon","Goop", "Yummy Goop"]##List of all the foods you can order
Sides = ["Spicy Fries", "Spicy Sweet Potato Fries", "Fries", "Chicken Nuggets", "Salad", "Wings", "Spicy Wings", "Cookie", "Dangerous Cookie", "Goop"]##Entrees list
Bev = ["Cofee", "Sludge", "Soda", "Dangerous Sludge", "Goofy Sludge", "Chocolate Frosty", "Vanilla Frosty","Mystery Sludge","Soupy Soup","Not so soupy soop"]##Drink List-Challenge

number_of_items = int(input("How many items would you like?"))##Prints and asking how my menu dishes they want

for i in range(number_of_items):##Saying for i in range of the number of items
         print(f"{random.choice(Food)} followed by {random.choice(Sides)} and {random.choice(Bev)}")##Choosing the set amount of random options from the list and pritning them.
