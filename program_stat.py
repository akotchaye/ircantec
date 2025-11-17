import pyttsx3

# Programme qui permet de faire des calculs statistiques
# Moyenne, Médiane, Mode, Variance, Ecart-type
import statistics


# fonction pour calculer la moyenne
def moyenne(liste):
    return statistics.mean(liste)


# fonction pour calculer la variance
def varian(liste):
    return statistics.variance(liste)


# fonction pour calculer l'écart-type
def ecart_type(liste):
    return statistics.stdev(liste)


# fonction pour calculer le minimum
def minimum(liste):
    return min(liste)


# fonction pour calculer le maximum
def maximum(liste):
    return max(liste)


# fonction pour compter le nombre d'éléments
def count(liste):
    return statistics.len(liste)


# fonction pour afficher le menu
def menu(my_user_list):
    print("1. Moyenne")
    print("2. Variance")
    print("3. Ecart-type")
    print("4. Minimum")
    print("5. Maximum")
    print("6. Nombre d'éléments")
    choice = int(input("choisissez une option : "))
    if choice == 1:
        print("Moyenne : ", moyenne(my_user_list))
    elif choice == 2:
        print("Variance : ", varian(my_user_list))
    elif choice == 3:
        print("Ecart-type : ", ecart_type(my_user_list))
    elif choice == 4:
        print("Minimum : ", minimum(my_user_list))
    elif choice == 5:
        print("Maximum : ", maximum(my_user_list))
    elif choice == 6:
        print("Nombre d'éléments : ", len(my_user_list))
    else:
        print("Option invalide")


def main():
    # declaration d'une liste vide
    user_list = list()
    # nombre d'éléments à entrer
    user_number = int(input("combien de nobre souhaitez-vous entrer ? "))
    # boucle pour entrer les éléments
    for i in range(user_number):
        number = int(input("entrez un nombre : "))
        user_list += (number,)
    # message pour continuer
    rep = "o"
    while rep == "o":
        menu(user_list)
        rep = input("souhaitez-vous continuer ? (o/n) ")


def text_to_speech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


# point d'entrée du programme
if __name__ == "__main__":
    text_to_speech("Bonjour Jean-luc !)")
