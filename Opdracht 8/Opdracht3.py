import os
from pip._vendor.distlib.compat import raw_input

Opdracht = 3


def welcome():
    print("Welkom in Opdracht " + str(Opdracht))
    print("Op het moment bevind u zich in: " + os.getcwd() + "\n")


def isdir(path):
    if os.path.isdir(path):
        return True
    else:
        return False


def isfile(path):
    if os.path.isfile(path):
        return True
    else:
        return False


def main():
    welcome()
    path = raw_input("Voer het pad of bestand in dat u wilt onderzoeken: ")
    print("Bedankt, we gaan nu uw antwoord valideren")
    if isdir(path):
        print("Dit is een map")
        print("De inhoud van de map is als volgt: ")
        for sub in os.listdir(path):
            print(sub)
    elif isfile(path):
        print("Dit is een bestand")
    else:
        print("Wat is dit?!")