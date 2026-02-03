def verify_number(nbr):
    while True:
        try:
            float(nbr)
            return nbr
        except ValueError:
            nbr = input("Entrée invalide. Veuillez entrer un nombre valide: ")

def main():    
    nbr_1 = verify_number(input("Entrer le premier nombre: "))
    nbr_2 = verify_number(input("Entrer le deuxième nombre: "))

    print("Le résultat de l'addition est: ", float(nbr_1) + float(nbr_2))


if __name__ == "__main__":
    main()
