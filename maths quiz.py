import random
print("-------------------------------------------------------------------------------")
name = input("What is your name?")
score = 0

#menu = input("

for i in range(1,11):
    randomNumber = random.randint(1,4)
    randomQNumber = random.randint(1,5)
    randomQNumber2 = random.randint(1,5)

    if randomNumber == 1:
        print("-------------------------------------------------------------------------------")
        a1 = float(input("What is " + str(randomQNumber) + "+" + str(randomQNumber2) + "?"))
        print("-------------------------------------------------------------------------------")
        if a1 == randomQNumber + randomQNumber2:
            print("Correct")
            score = score + 1
        else:
            print("Sorry, it's wrong!")
    elif randomNumber == 2:
        print("-------------------------------------------------------------------------------")
        a2 = float(input("What is " + str(randomQNumber) + "-" + str(randomQNumber2) + "?"))
        print("-------------------------------------------------------------------------------")
        if a2 == randomQNumber - randomQNumber2:
            print("Correct")
            score = score + 1
        else:
            print("Sorry, it's wrong!")
    elif randomNumber == 3:
        print("-------------------------------------------------------------------------------")
        a3 = float(input("What is " + str(randomQNumber) + "/" + str(randomQNumber2) + "?"))
        print("-------------------------------------------------------------------------------")
        if a3 == randomQNumber / randomQNumber2:
            print("Correct")
        else:
            print("Sorry, it's wrong!")
    else:
        print("-------------------------------------------------------------------------------")
        a4 = float(input("What is " + str(randomQNumber) + "*" + str(randomQNumber2) + "?"))
        print("-------------------------------------------------------------------------------")
        if a4 == randomQNumber * randomQNumber2:
            print("Correct")
            score = score + 1
        else:
            print("Sorry, it's wrong")
print("-------------------------------------------------------------------------------")
print("Thank you for playing " + name + ". Your score was " + str(score) + "/10")
print("-------------------------------------------------------------------------------")
