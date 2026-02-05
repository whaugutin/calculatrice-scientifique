def verify_number(nbr) -> float:
    while True:
        try:
            return float(nbr)
        except ValueError:
            nbr = input("Entrée invalide. Veuillez entrer un nombre valide: ")