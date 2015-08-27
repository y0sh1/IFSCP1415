def welcome():
    ans = True
    while ans:
        print("""
        1.Inspringen in Python
        2.Syntax
        3.Imports
        4.In- en Output
        5.Datatypes
        6.Loops en statements
        7.Functies
        8.Exit/Quit
        """)
        ans = raw_input("Waar wil je meer over weten? ")
        if ans == "1":
            print("\n Inspringen in Python is belangrijk voor het uitvoeren van code. Als dit niet correct gedaan wordt kan"
                  "het programma mogelijk niet goed functioneren.")
        elif ans == "2":
            print("\n Syntax is een studievereniging voor de opleiding informatica aan de Hogeschool Leiden.")
        elif ans == "3":
            print(
                "\n Imports is het importeren van code bibliotheken in Python. Gebruik hiervan zorgt er voor dat voor veel"
                "functionaliteit toegevoegd kan worden, zonder het wiel opnieuw uit te vinden.")
        elif ans == "4":
            print(
                "\n Python kan zowel data weergeven, als data opnemen. Deze applicatie is hier een voorbeeld van (het hoofd"
                "menu)")
        elif ans == "5":
            print("\n Python heeft een aantal datatypes: Numbers, String, List, Tuple, Dictionary.")
        elif ans == "6":
            print(
                "\n Binnen Python is het mogelijk om acties uit te voeren, wanneer er voorafgaand randvoorwaarden "
                "zijn gedefineerd. .")
        elif ans == "7":
            print("\n Voor veel gebruikte stukken code is het beter om een functie hiervoor te defineren. "
                  "Hiermee voorkom je dat je veel gebruikte code op meerdere plaatsen volledig uitschrijft.\n "
                  "Functies kunnen input en output hebben, maar dit is niet verplicht.")
        elif ans == "8":
            print("\n Goodbye")
            ans = False
        elif ans != "":
            print("\n Geen valide invoer. Probeer het opnieuw")