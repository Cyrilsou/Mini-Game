import random
import tkinter


def input_range():
    users_min_range = int(input("Choisissez la valeur minimale de la plage : "))
    users_max_range = int(input("Choisissez la valeur maximale de la plage : "))
    #print("La plage que vous avez choisie est : " + str(users_min_range) + "-" + str(users_max_range))
    #print("La plage que vous avez choisie est : ", users_min_range, "-", users_max_range)
    if users_min_range < users_max_range:
        print("La plage que vous avez choisie est : %d - %d" % (users_min_range, users_max_range))
        chance_of_succes = users_max_range - users_min_range + 1
        print("Vous avez une probabilité de 1 sur %d de gagner" % chance_of_succes)
        generate_random(users_min_range, users_max_range)
    else:
        print("La valeur minimale est plus grande que la maximale. Veuillez choisir à nouveau")
        input_range()

def generate_random(p_min_number, p_max_number):
    random_number = random.randint(p_min_number, p_max_number)
    print("Le nombre selectioner est : %d" % random_number)
    time_to_guess(random_number, p_min_number, p_max_number)


def main():
    n = input("1- Jouer\n2- Ne pas jouer\n\nPlease enter a number :")

    if n == '1':
        request_user_name() , input_range()
    if n == '2':
        None

def time_to_guess(p_number_to_guess, p_min_number, p_max_number):
    user_guess = None
    counting_guesses = 1

    while user_guess != p_number_to_guess:
        print("Essaie n° %d : " % counting_guesses)
        user_guess = int(input("Quel est le chiffre aléatoire ?"))

        if user_guess < p_min_number or user_guess > p_max_number:
            print("veuillez choisir un nombre dans la plage.")

            #time_to_guess(p_number_to_guess, p_min_number, p_max_number)
        else:
            print("Bravo, Tu as trouver le nombre")
            if user_guess > p_number_to_guess:
                print("Le nombre que tu as choisi est supérieur au nombre à trouver")
            elif user_guess < p_number_to_guess:
                print("Le nombre que tu as choisi est plus petit que le nombre à trouver")
        counting_guesses = counting_guesses + 1






def  request_user_name():
    users_name = input("quelle est votre nom : ")
    print("Vous êtes : " + users_name)

def crack_the_code():
    guessed_word = input("Vous avez une dernière mission...\nEssayer de deviner le mot suivant : *i*to*r*\n")
    counting_guesses = 1
    while guessed_word != "victoire":
        print("Essaie n° %d : " % counting_guesses)
        counting_guesses = counting_guesses + 1
        guessed_word = input("Veuillez réessayer\n")

    print("Félicitations ! Vous avez deviné le mot !")




main()
crack_the_code()

