# -*- coding: utf-8 -*-.


print "MENU OF THE DAY:"

menu_of_the_day = {}

with open("menu2.txt", "w+") as food_menu2:
    food_menu2.write("MENU OF THE DAY:\n")
    while True:

        dish = raw_input("Enter a dish:")
        price = raw_input("Enter a price for %s in EUR:" %(dish))
        menu_of_the_day[dish] = price


        food_menu2.write(dish + ":")
        food_menu2.write(price + " EUR\n")

        answer = raw_input("Do you want to add another dish? yes/no")
        if answer== "no":
            break

print "MENU OF THE DAY:"

for key, value in menu_of_the_day.iteritems():
    print key + ":",
    print value + " EUR"



