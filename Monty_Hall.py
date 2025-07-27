import random

def monty_hall_simulation(durchläufe=1000, wechseln=True):
    siege = 0

    for _ in range(durchläufe):
        türen = ["Ziege", "Ziege", "Auto"]
        random.shuffle(türen)

        wahl = random.randint(0, 2)

        monty_optionen = [i for i in range(3) if i != wahl and türen[i] == "Ziege"]
        monty_öffnet = random.choice(monty_optionen)

        if wechseln:
            finale_wahl = [i for i in range(3) if i != wahl and i != monty_öffnet][0]
        else:
            finale_wahl = wahl

        if türen[finale_wahl] == "Auto":
            siege += 1

    return siege / durchläufe

wechsel_quote = monty_hall_simulation(wechseln=True)
bleib_quote = monty_hall_simulation(wechseln=False)

print("Gewinnrate MIT Wechseln:", wechsel_quote)
print("Gewinnrate OHNE Wechseln:", bleib_quote)