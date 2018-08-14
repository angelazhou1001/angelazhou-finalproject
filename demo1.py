def begin():
     print("Welcome to the land of ninjas.You've ve seen them in movies and Japanese anime. But what exactly are ninjas? While some aspects of the ninja way may be outdated, the principles and techniques remain valuable for anyone who is interested in espionage and deception. I'm sure you have been dreaming of becoming a ninja. This game will teach you how to become an kickass ninja. Are you ready?!?")
     firstanswer = input()
     if firstanswer == "no":
         print("I'm sorry. You've failed.")
     else:
         print("Let's go!")
begin()

def step1():
    input("Press 'Enter' key to start")
    print("Step 1: Learn the Ninja way")
    input("What is the ninja way? Type your answer here...")
    print("You seem to understand it very well. Ok, step 1 is to educate yourself on the history of ninja. For example, you might want to read Masaaki Hatsumi's book, Secrets From The Ninja Grandmaster. ")
step1()

def step2():
    input("Press 'Enter' key to go to step 2")
    step2answer = input("Now let's move to step 2. When you are a ninja, do you want other people to know it?(yes or no?)")
    if step2answer == "yes":
        print("You will be in danger if other people especially your enemies know that you are a ninja.")
    else:
        print("You are right. Understand that silence is a valuable asset. One's decision to live by ninjutsu discipline is not and should not be public knowledge. Your first responsibility is to learn and practice ninjutsu in secrecy, and privately.")

step2()

def step3():
    weight = input("What's your weight?")
    height = input("What's your height?(use XX format. Say if you are 5'7, please put 57)")
    bodyindex = int((weight*0.45)/((height*0.025)*(height*0.025)))
    if bodyindex <= 18.5:
        print("You need to eat more!")
    elif 18.5 < bodyindex < 24.9:
        print("You are in perfect shape to be a Ninja!")
    else:
        print("You need to exercise more!")
step3()


    #Exercise and maintain a ninja body.

#favfood=['fried chicken','BBQ','peach','watermelon','blueberry']
#for food in favfood:
#    print(food)
#for food in range(0,len(favfood)):
#    print(favfood[food])


#def step4():

#def step5():


#def choosepath():
#    path = ""
#    while path != "1" and path != "2":
#        path = input("Which path will you choose?(1 or 2):")
#    return path
#choosepath()
