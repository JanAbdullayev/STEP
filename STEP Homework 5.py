import random

class pets:
    dog_name = "Chira"
    cat_name = "Nia"
    dog_age = 1
    cat_age = 1
    dog_strength = 10
    dog_IQ = 66
    dog_satiety = 100
    dog_energy = 100
    cat_strength = 5
    cat_IQ = 84
    cat_satiety = 100
    cat_energy = 100
    dog_moneygain = dog_IQ + dog_strength
    cat_moneygain = cat_IQ + cat_strength
class characters:
    character1_name = "Michael"
    character2_name = "Lina"
    michael_age = 18
    lina_age = 18
    michael_strength = 50
    michael_IQ = 104
    michael_satiety = 100
    michael_energy = 100
    michael_money = 1000
    lina_strength = 25
    lina_IQ = 118
    lina_satiety = 100
    lina_energy = 100
    lina_money = 1000
    michael_moneygain = michael_IQ + michael_strength
    lina_moneygain = lina_IQ + lina_strength

def dog_char():
    print("3. ",pets.dog_name,"'s characteristics:")
    print("Age:", pets.dog_age)
    print("Strenghth:", pets.dog_strength)
    print("IQ:", pets.dog_IQ)
    print("Satiety:", pets.dog_satiety)
    print("Energy:", pets.dog_energy)
def cat_char():
    print("4. ",pets.cat_name,"'s characteristics:")
    print("Age:", pets.cat_age)
    print("Strenghth:", pets.cat_strength)
    print("IQ:", pets.cat_IQ)
    print("Satiety:", pets.cat_satiety)
    print("Energy:", pets.cat_energy)
def michael_char():
    print("1. ",characters.character1_name,"'s characteristics:")
    print("Age:", characters.michael_age)
    print("Strenghth:", characters.michael_strength)
    print("IQ:", characters.michael_IQ)
    print("Satiety:", characters.michael_satiety)
    print("Energy:", characters.michael_energy)
    print("Money:", characters.michael_money)

def lina_char():
    print("2. ",characters.character2_name,"'s characteristics:")
    print("Age:", characters.lina_age)
    print("Strenghth:", characters.lina_strength)
    print("IQ:", characters.lina_IQ)
    print("Satiety:", characters.lina_satiety)
    print("Energy:", characters.lina_energy)
    print("Money:", characters.lina_money)

def start(): #menu
    print(" ")
    michael_char()
    print(" ")
    lina_char()

    print("Pets : ")

    print(" ")
    print("Dog")
    print(" ")
    dog_char()
    print(" ")
    print("Cat")
    print(" ")
    cat_char()


    print(" ")
    global choose
    choose = int(input("Choose one of them (1/2/3/4) : "))

start()

if choose == 1:
    print(" ")
    print("Chose action:")
    print(" ")
    print("1. Sleep /n 2. Study /n 3.Eat /n 4. Work")
    print(" ")
    print("5. Teach Chira /n 6. Train Chira /n 7. Feed Chira /n 8. Make Chira Energetic /n 9.Menu")
    action_choise_michael = input("Choice (1/2/3/4/5/6/7/8) : ")
elif choose == 2:
    print(" ")
    print("Chose action:")
    print(" ")
    print("1. Sleep /n 2. Study /n 3.Eat /n 4. Work")
    print(" ")
    print("5. Teach Nia /n 6. Train Nia /n 7. Feed Nia /n 8. Make Nia Energetic /n 9.Menu")
    action_choise_lina = input("Choice (1/2/3/4/5/6/7/8) : ")
elif choose == 3:
    print(" ")
    print("Chose action:")
    print(" ")
    print("1. Sleep /n 2. Study /n 3.Work /n 4.Menu")
    action_choise_dog = input("Choice (1/2/3/4) : ")

elif choose == 4:
    print(" ")
    print("Chose action:")
    print(" ")
    print("1. Sleep /n 2. Study /n 3.Work /n 4.Menu")
    action_choise_cat = input("Choice (1/2/3/4) : ")

if action_choise_michael == 1:
    characters.michael_energy += 10
    characters.michael_satiety -= 5
    start()
elif action_choise_michael == 2:
    characters.michael_energy -= 5
    characters.michael_IQ += 1
    start()
elif action_choise_michael == 3:
    characters.michael_money -= 20
    characters.michael_satiety += 33
    start()
elif action_choise_michael == 4:
    characters.michael_energy -= 10
    characters.michael_money += characters.michael_moneygain
    start()

elif action_choise_michael == 5:
    characters.michael_energy -= 10
    pets.dog_IQ += 1
    start()
elif action_choise_michael == 6:
    characters.michael_energy -= 20
    pets.dog_strength += 10
    start()
elif action_choise_michael == 7:
    characters.michael_energy -= 5
    pets.dog_satiety += 25
    start()
elif action_choise_michael == 8:
    characters.michael_energy -= 5
    pets.dog_satiety += 25
    start()
elif action_choise_michael == 9:
    start()


if action_choise_lina == 1:
    characters.lina_energy += 10
    characters.lina_satiety -= 5
    start()
elif action_choise_lina == 2:
    characters.lina_energy -= 5
    characters.lina_IQ += 1
    start()
elif action_choise_lina == 3:
    characters.lina_money -= 20
    characters.lina_satiety += 33
    start()
elif action_choise_lina == 4:
    characters.lina_energy -= 10
    characters.lina_money += characters.lina_moneygain
    start()

elif action_choise_lina == 5:
    characters.lina_energy -= 10
    pets.cat_IQ += 1
    start()
elif action_choise_lina == 6:
    characters.lina_energy -= 20
    pets.cat_strength += 10
    start()
elif action_choise_lina == 7:
    characters.lina_energy -= 5
    pets.cat_satiety += 25
    start()
elif action_choise_lina == 8:
    characters.lina_energy -= 5
    pets.cat_satiety += 25
    start()
elif action_choise_lina == 9:
    start()



if action_choise_dog == 1:
    characters.dog_energy += 10
    characters.dog_satiety -= 5
    start()
elif action_choise_dog == 2:
    characters.dog_energy -= 5
    characters.dog_IQ += 1
    start()
elif action_choise_dog == 3:
    characters.michael_money += pets.dog_moneygain
    characters.dog_energy -= 10
    start()
elif action_choise_dog == 4:
    start()

if action_choise_cat == 1:
    characters.cat_energy += 10
    characters.cat_satiety -= 5
    start()
elif action_choise_cat == 2:
    characters.cat_energy -= 5
    characters.cat_IQ += 1
    start()
elif action_choise_cat == 3:
    characters.lina_money += pets.cat_moneygain
    characters.cat_energy -= 10
    start()
elif action_choise_cat == 4:
    start()