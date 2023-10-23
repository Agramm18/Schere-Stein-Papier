import random

Schere_Stein_Papier = ['Schere', 'Stein', 'Papier']
def Spiel():

    Eingabe_Player = input("Geben sie Schere, Stein oder Papier ein: ")

    Eingabe_Pc = random.choice(Schere_Stein_Papier)

    if Eingabe_Player == 'Schere' and  Eingabe_Pc == 'Stein':
        print(f"Der Spieler hatt {Eingabe_Player} eingegeben")
        print(f"Der PC hatt {Eingabe_Pc} eingegeben")
        print ("Der PC hat gewonnen")
        return

    if Eingabe_Player == 'Schere' and  Eingabe_Pc == 'Papier':
        print(f"Der Spieler hatt {Eingabe_Player} eingegeben")
        print(f"Der PC hatt {Eingabe_Pc} eingegeben")
        print ("Der Player hat gewonnen")
        return

    if Eingabe_Player == 'Schere' and  Eingabe_Pc == 'Schere':
        print(f"Der Spieler hatt {Eingabe_Player} eingegeben")
        print(f"Der PC hatt {Eingabe_Pc} eingegeben")
        print ("Es ist unentschieden spiele eine neue runde")
        return

    if Eingabe_Player == 'Papier' and  Eingabe_Pc == 'Schere':
        print(f"Der Spieler hatt {Eingabe_Player} eingegeben")
        print(f"Der PC hatt {Eingabe_Pc} eingegeben")
        print ("Der PC hat gewonnen")
        return

    if Eingabe_Player == 'Papier' and  Eingabe_Pc == 'Stein':
        print(f"Der Spieler hatt {Eingabe_Player} eingegeben")
        print(f"Der PC hatt {Eingabe_Pc} eingegeben")
        print ("Der Player hat gewonnen")
        return

    if Eingabe_Player == 'Papier' and  Eingabe_Pc == 'Papier':
        print(f"Der Spieler hatt {Eingabe_Player} eingegeben")
        print(f"Der PC hatt {Eingabe_Pc} eingegeben")
        print ("ES ist unentschieden spiele eine neue runde")
        return

    if Eingabe_Player == 'Stein' and  Eingabe_Pc == 'Schere':
        print(f"Der Spieler hatt {Eingabe_Player} eingegeben")
        print(f"Der PC hatt {Eingabe_Pc} eingegeben")
        print ("Der Player hat gewonnen")
        return

    if Eingabe_Player == 'Stein' and  Eingabe_Pc == 'Papier':
        print(f"Der Spieler hatt {Eingabe_Player} eingegeben")
        print(f"Der PC hatt {Eingabe_Pc} eingegeben")
        print ("Der PC hat gewonnen")
        return

    if Eingabe_Player == 'Stein' and  Eingabe_Pc == 'Stein':
        print(f"Der Spieler hatt {Eingabe_Player} eingegeben")
        print(f"Der PC hatt {Eingabe_Pc} eingegeben")
        print ("Es ist unentschieden spiele eine neue runde")
        return


Spiel()