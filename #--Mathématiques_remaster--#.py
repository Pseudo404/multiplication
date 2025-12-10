import random
win = 0
print("règle une bonne réponse donne 1 point 1 mauvaise t'en n'enlève 1 si ta 20 point ta gaggner ! si t'accept écris 'oui'")
rule = input("")
if str(rule) == "oui":
    print("GO TRAVAILLE !!!")
    while win != 20:
        a = random.randint(2, 9)
        b = random.randint(2, 9)
        print("combien fait ? " + str(a) + "x" + str(b))
        rep = input("")
        ret = a*b
        if int(rep) == int(ret):
            print("+1 bonne réponse")
            win += 1
        if int(rep) < int(ret):
            print("-1 mauvaise réponse")
            win -= 1
        if int(rep) > int(ret):
            print("-1 mauvaise réponse")
            win -= 1
    if win == 20:
        print("Bien joué, tu as réussi")