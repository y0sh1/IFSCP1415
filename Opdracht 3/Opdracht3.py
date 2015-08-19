import os
from pip._vendor.distlib.compat import raw_input

Opdracht = 3


def welcome():
    print("Welkom in Opdracht " + str(Opdracht))
    print("Op het moment bevind u zich in: " + os.getcwd() + "\n")


def validatepath(path):
    print("hier valideren we iets")


def isdir(path):
    print("hier kijken we of een map er echt is")


def isfile(path):
    print("Hier kijken we of een bestand er echt wel is")


def main():
    welcome()
    filename = raw_input('Enter a file name: ')
    print("Bedankt, we gaan nu uw antwoord valideren")

main()
