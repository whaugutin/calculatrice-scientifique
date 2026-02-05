from functions import verify_number
from ipyllogger import Logger
from ipyllogger import level

logger = Logger()

def main(): 
    
    logger.log("Session Starts", level=level.WARNING)

    continuer = True
    while continuer:

        options = [
            "Quitter",
            "Addition de deux nombres",
            "Soustraction de deux nombres",
            "Multiplication de deux nombres",
            "Division de deux nombres",
            "Historique des opériations"
        ]

        print("\n=== Calculatrice Scientifique ===\n")
        for i in range(len(options)):
            print(f"{i}. {options[i]}")

        option = int(verify_number(input("Choisissez une option >>> ")))

        if option == 0:
            logger.log("Session ends", level=level.WARNING)
            print("Au revoir")
            exit()

        if option not in range(6):
            print("\nChoix invalide. Choisissez une option en 0 et 5")
            continue

        if option == 5:
            with open("data.txt") as file:
                print(file.read())
            continue


        nbr_1 = verify_number(input("Entrer le premier nombre: "))
        nbr_2 = verify_number(input("Entrer le deuxième nombre: "))
        resultat = 0

        if option == 1:
            resultat = nbr_1 + nbr_2
        elif option == 2:
            resultat = nbr_1 - nbr_2
        elif option == 3:
            resultat = nbr_1 * nbr_2
        elif option == 4:
            while nbr_2 == 0:
                print("Erreur: Division par zéro n'est pas permise.")
                nbr_2 = verify_number(input("Entrer le deuxième nombre: "))
                return
            resultat = nbr_1 / nbr_2
        

        
        # file = open("data.txt", "a")
        # file.write(f"{nbr_1} {'+' if option == 1 else '-' if option == 2 else '*' if option == 3 else '/'} {nbr_2} = {resultat}\n")
        # file.close()

        with open("data.txt", "a") as file:
            file.write(f"{nbr_1} {'+' if option == 1 else '-' if option == 2 else '*' if option == 3 else '/'} {nbr_2} = {resultat}\n")

        print("Le résultat est: ", resultat)
        choix = input("Voulez-vous continuer? (O/N) [N] >>> ")
        if choix.upper() != "O":
            continuer = False


if __name__ == "__main__":
    main()
