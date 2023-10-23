




def Schere_Stein_Papier():

    Rock_Paper_Scissor = "Schere", "Stein", "Papier"

    Spiel = input("Geben sie Schere, Stein oder Papier ein: ")

    if Spiel == "Schere":
        print("Der Computer hat Papier genommen sie haben gewonnen")
        return

    if Spiel == "Stein":
        print("Der Computer hat Schere genommen sie haben gewonnen")
        return

    if Spiel == "Papier":
        print("Der Computer hat Stein genommen sie haben gewonnen")
        return

Schere_Stein_Papier()