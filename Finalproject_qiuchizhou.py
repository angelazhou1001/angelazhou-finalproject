#Beginning of the ninja project
def begin():
     print("Welcome to the land of ninjas.You've ve seen them in movies and Japanese anime. But what exactly are ninjas? While some aspects of the ninja way may be outdated, the principles and techniques remain valuable for anyone who is interested in espionage and deception. I'm sure you have been dreaming of becoming a ninja. This game will teach you how to become an kickass ninja. Are you ready?!?")
     firstanswer = input()
     if firstanswer == "no":
         print("I'm sorry. You've failed.")
     else:
         print("Let's go!")
begin()

#Step1
def step1():
    input("Press 'Enter' key to start")
    print("Step 1: Learn the Ninja way")
    input("What is the ninja way? Type your answer here...")
    print("Ok, step 1 is to educate yourself on the history of ninja. For example, you might want to read Masaaki Hatsumi's book, Secrets From The Ninja Grandmaster. Most ninja were freelance mercenaries who used their skills to support their families. Some ninja, however, were employed by lords and government officials. And some worked solely for their own clan. The ninja lifestyle was diverse. You will need to direct your lifestyle accordingly.")
step1()

#Step2
def step2():
    input("Press 'Enter' key to go to step 2")
    step2answer = input("Now let's move to step 2. When you are a ninja, do you want other people to know it?(yes or no?)")
    if step2answer == "yes":
        print("You will be in danger if other people especially your enemies know that you are a ninja.Try to answer the question again!")
    else:
        print("You are right. Understand that silence is a valuable asset. One's decision to live by ninjutsu discipline is not and should not be public knowledge. Your first responsibility is to learn and practice ninjutsu in secrecy, and privately.")

    input("Press 'Enter' key to continue with step 2")
    step2answer = input("You just made your decision, we just want to double check, can you confirm you want other people to know it?(yes or no?)")
    if step2answer == "yes":
         print("Sorry, you will be in danger if other people especially your enemies know that you are a ninja.Try to answer the question again!")
    else:
         print("You are right again! Understand that silence is a valuable asset. One's decision to live by ninjutsu discipline is not and should not be public knowledge. Your first responsibility is to learn and practice ninjutsu in secrecy, and privately.")

step2()

#Step3

def step3():
    weight = int(input("What's your weight?(type your weight in format of lb)"))
    height = int(input("What's your height?(use XX format. Say if you are 5'7, please put 57)"))
    bodyindex = (weight*0.45)/((height*0.025)**2)
    if bodyindex <= 18.5:
        print("You need to eat more!");
    elif 18.5 < bodyindex < 24.9:
        print("You are in perfect shape to be a ninja!")
    else:
        print("You need to exercise more!");
        input("Press 'Enter' key to go to step 2")
step3()


#Step4
print("There are several exercises to do to become a professional ninja:running,swordcraft,bojutsu,sojutsu and kenjutsu. Enter the exercises into the Exercise_to_do based on the order you prefer")
Exercise_to_do= []
first_to_do = input(('Enter the first exercise item: '))
second_to_do = input(('Enter the second exercise item: '))
third_to_do = input(('Enter the third exercise item: '))
forth_to_do = input(('Enter the forth exercise item: '))


Exercise_to_do.append(first_to_do)
Exercise_to_do.append(second_to_do)
Exercise_to_do.append(third_to_do)
Exercise_to_do.append(forth_to_do)


#Exercise_to_do = ['running','running','swordcraft','bojutsu','sojutsu','kenjutsu']

def step4(Exercise_to_do):
    for exercise in Exercise_to_do:
        print ("{} is part of the practice needed to be a ninja".format(exercise))
step4(Exercise_to_do)

#Step5
print("After the exercises, you still need to complete the fighting courses to become a real ninja")
input("Press 'Enter' key to continue")
print("The following is the fighting stages you need to pass")
Fights_against = {
 "stage1":"Complete the training course",
 "stage2":"defeat a samurai",
 "stage3":"defeat a general"}
print(Fights_against)

print("Now the fighting stages are clear, it's your time to complete the fighting challenges.")
input("Press 'Enter' key to continue")
def step5(Fights_against):
  for stage,fight in Fights_against.items():
      print ("You have completed {}, completing {} is a extraordinary accomplishment in the process of becoming a ninja".format(stage,fight))
step5(Fights_against)
#Step6
input("Press 'Enter' key to continue")
def step6():
  print ("Congratulations!!You are now a qualified ninja!")
step6()
