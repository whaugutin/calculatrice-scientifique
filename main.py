from functions import verify_number
from ipyllogger import Logger
from ipyllogger import level

logger = Logger()

def main(): 
    
    logger.log("Session Starts", level=level.WARNING)

    continuer = True
    while continuer:
        print("---Operations Mathématiques de Base---")
        print("1. Addition de deux nombres")
        print("2. Soustraction de deux nombres")
        print("3. Multiplication de deux nombres")
        print("4. Division de deux nombres")
        print("0. Quitter")

        option = int(verify_number(input("Choisissez une option >>> ")))

        if option == 0:
            logger.log("Session ends", level=level.WARNING)
            print("Au revoir")
            exit()

        if option not in [1, 2, 3, 4]:
            print("Choix invalide \n")
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
        

        print("Le résultat est: ", resultat)
        choix = input("Voulez-vous continuer? (O/N) [N] >>> ")
        if choix.upper() != "O":
            continuer = False


if __name__ == "__main__":
    main()
