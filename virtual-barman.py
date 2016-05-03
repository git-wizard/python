#title
print("*********************VIRTUAL_BARMAN*********************** \n")

#for loop checking age, after 3 attempts it stops.
for i in range(1, 4):
    #age variable
    age = int(input("    How old are you?  "))
    print("--------------------------------------------------")

    #age check
    if age > 17:
    #drink variable
        drink = input("    What can i get you?  ")
        print("--------------------------------------------------")
        print("    One " + drink + " is coming right up")
    #breaks the for loop
        break
    #Under_age
    elif age > 10:
        print("   No alcoholic drinks for you, sorry. \n   You're under age. Here's what you can have: \n")
        print("Hot beverages: \n   Hot Chocolate \n   Tea \n   Coffee")
        print("--------------------------------------------------")
        print("Cold beverages: \n   Coca Cola \n   Ice Tea \n   Milkshakes (ask for 'milkshake') \n   Lemonade \n   orangade")
    #space
        print("--------------------------------------------------")
    #choices
        above_ten = input("   Would you like any of the choices listed?")
        print("--------------------------------------------------")
    #milkshake_choice
        if above_ten == 'milkshake':
            for y in range(1, 100):
                print("Here are the options for milkshakes: \n")
                print("   Chocolate \n   Strawberry \n   Banana \n   Berry mix \n")
                milkshake = input("Which one would you like? ")
        #milkshake_choices_list
                if milkshake == 'banana':
                    print("--------------------------------------------------")
                    print("Your milkshake is being made!")
                    print("--------------------------------------------------")
                    break
                elif milkshake == 'berry mix':
                    print("--------------------------------------------------")
                    print("Your milkshake is being made.")
                    print("--------------------------------------------------")
                    break
                elif milkshake == 'starberry':
                    print("--------------------------------------------------")
                    print("Your milkshake is being made.")
                    print("--------------------------------------------------")
                    break
                elif milkshake == 'chocolate':
                    print("--------------------------------------------------")
                    print("Your milkshake is being made.")
                    print("--------------------------------------------------")
                    break
                else:
                    print("Sorry, not a choice, try again.")
    #coffee_choices        
        elif above_ten == 'coffee':
            coffee = input("What kind of coffee would you like")

        break
    
