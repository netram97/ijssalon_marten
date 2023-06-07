# variabeles
prijzen = {'aardbei': 3, 'vanille': 4, 'chocolade': 5}
aanbieding = prijzen['aardbei'] * 0.8
reclame_tekst = f'Vandaag in de aanbieding: aardbei-ijs, 1 liter - slechts €{aanbieding}!'

# Functies
def Gekozen1():
    print()
    print(reclame_tekst)
    print()
    print(frommat)

aanbieding_formatted = '{:.2f}'.format(aanbieding).replace('.', ',')# Ik vind een komma mooier dan een punt voor een bedrag.
reclame_tekst_formatted = f'Vandaag in de aanbieding: aardbei-ijs, 1 liter - slechts €{aanbieding_formatted}!'
def Gekozen2():
    print()
    print(reclame_tekst_formatted)
    print()
    print(frommat)

reclame_tekst_upper = reclame_tekst_formatted.upper()
def Gekozen3():
    print()
    print(reclame_tekst_upper)
    print()
    print(frommat)

reclame_tekst_list = reclame_tekst_upper.split()
def Gekozen4():
    print()
    print(*reclame_tekst_list, sep = ',')
    print()
    print(frommat)

def Gekozen5():
    print()
    for eu in reclame_tekst_list:
        print(eu)
    print()
    print(frommat)
def Gekozen6():
    print()
    for el in reclame_tekst_list:
        print(el.lower())
    print()
    print(frommat)
def Gekozen7():
    print()
    for el in reclame_tekst_list:
        if len(el) > 5:
            print(el.capitalize())
        else:
            print(el.lower())
    print()
    print(frommat)

# Loop
tf = True
frommat = 95*'-'
print(frommat)
while tf == True:
    keuze_menu = f"""1. Reclame tekst\n2. Reclame tekst met 2 decimalen\n3. Reclame tekst in hoofdletters\n4. Reclame tekst in een lijst met hoofdletters\n5. Reclame tekst in een lijst met hoofdletters onder elkaar\n6. Reclame tekst in een lijst met kleine letters onder elkaar\n7. Reclame tekst in een lijst met kleine letters, behalve als het woord langer is dan 5 letters\n8. Stoppen\nMaak een keuze... """
    keuze = input(keuze_menu)
    function_list = [Gekozen1, Gekozen2, Gekozen3, Gekozen4, Gekozen5, Gekozen6, Gekozen7]
    if keuze == '1':
        function_list[0]()
    elif keuze == '2':
        function_list[1]()
    elif keuze == '3':
        function_list[2]()
    elif keuze == '4':
        function_list[3]()
    elif keuze == '5':
        function_list[4]()
    elif keuze == '6':
        function_list[5]()
    elif keuze == '7':
        function_list[6]()
    elif keuze == '8':
        print()
        print('Closing program...')
        tf = False
    else:
        print()
        print('Verkeerde input, probeer het opnieuw.')
        print()
        print(frommat)