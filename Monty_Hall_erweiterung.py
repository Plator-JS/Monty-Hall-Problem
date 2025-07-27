import random

def monty_hall_game():
    türen = ["Ziege", "Ziege", "Auto"]
    random.shuffle(türen)

    print("Willkommen beim Monty-Hall-Spiel!")
    print("Hinter einer Tür ist ein Auto, hinter den anderen Ziegen.")
    print("Welche Tür wählst du? (0, 1 oder 2)")
    wahl = int(input("Deine Wahl: "))

    monty_optionen = [i for i in range(3) if i != wahl and türen[i] == "Ziege"]
    monty_öffnet = random.choice(monty_optionen)

    print(f"Monty öffnet Tür {monty_öffnet} – dahinter ist eine Ziege.")

    wechseln = input("Willst du wechseln? (ja/nein): ").lower() == "ja"

    if wechseln:
        finale_wahl = [i for i in range(3) if i != wahl and i != monty_öffnet][0]
    else:
        finale_wahl = wahl

    print(f"Du wählst Tür {finale_wahl}.")
    print(f"Hinter der Tür ist: {türen[finale_wahl]}")

    if türen[finale_wahl] == "Auto":
        print("Glückwunsch! Du hast das Auto gewonnen!")
    else:
        print("Leider nur eine Ziege. Versuch's nochmal!")

monty_hall_game()