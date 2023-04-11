import math

def afficher_figures():
    figures = [
        "Triangle",
        "Carré",
        "Rectangle",
        "Losange",
        "Trapèze",
        "Cercle",
    ]
    for i, figure in enumerate(figures):
        print(f"{i + 1}. {figure}")

def calculer_air(figure, **params):
    if figure == "Triangle":
        base, hauteur = params["base"], params["hauteur"]
        return 0.5 * base * hauteur
    elif figure == "Carré":
        cote = params["cote"]
        return cote ** 2
    elif figure == "Rectangle":
        longueur, largeur = params["longueur"], params["largeur"]
        return longueur * largeur
    elif figure == "Losange":
        diagonale1, diagonale2 = params["diagonale1"], params["diagonale2"]
        return 0.5 * diagonale1 * diagonale2
    elif figure == "Trapèze":
        base1, base2, hauteur = params["base1"], params["base2"], params["hauteur"]
        return 0.5 * (base1 + base2) * hauteur
    elif figure == "Cercle":
        rayon = params["rayon"]
        return math.pi * rayon ** 2
    else:
        raise NotImplementedError(f"La formule pour calculer l'aire d'un {figure} n'est pas implémentée.")

def main():
    afficher_figures()
    choix_figure = int(input("Entrez le numéro de la figure plane dont vous voulez calculer l'aire: ")) - 1
    figures = [
        "Triangle",
        "Carré",
        "Rectangle",
        "Losange",
        "Trapèze",
        "Cercle",
    ]
    figure = figures[choix_figure]

    if figure == "Triangle":
        base = float(input("Entrez la base du triangle: "))
        hauteur = float(input("Entrez la hauteur du triangle: "))
        print(f"L'aire du triangle est: {calculer_air(figure, base=base, hauteur=hauteur)}")
    elif figure == "Carré":
        cote = float(input("Entrez la longueur du côté du carré: "))
        print(f"L'aire du carré est: {calculer_air(figure, cote=cote)}")
    elif figure == "Rectangle":
        longueur = float(input("Entrez la longueur du rectangle: "))
        largeur = float(input("Entrez la largeur du rectangle: "))
        print(f"L'aire du rectangle est: {calculer_air(figure, longueur=longueur, largeur=largeur)}")
    elif figure == "Losange":
        diagonale1 = float(input("Entrez la longueur de la première diagonale du losange: "))
        diagonale2 = float(input("Entrez la longueur de la deuxième diagonale du losange: "))
        print(f"L'aire du losange est: {calculer_air(figure, diagonale1=diagonale1, diagonale2=diagonale2)}")
    elif figure == "Trapèze":
        base1 = float(input("Entrez la longueur de la première base du trapèze: "))
        base2 = float(input("Entrez la longueur de la deuxième base du trapèze: "))
        hauteur = float(input("Entrez la hauteur du trapèze: "))
        print(f"L'aire du trapèze est: {calculer_air(figure, base1=base1, base2=base2, hauteur=hauteur)}")
    elif figure == "Cercle":
        rayon = float(input("Entrez le rayon du cercle: "))
        print(f"L'aire du cercle est: {calculer_air(figure, rayon=rayon)}")

if __name__ == "__main__":
    main()
