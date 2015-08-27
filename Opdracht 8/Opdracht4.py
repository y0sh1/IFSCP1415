import mimetypes
import os
from pip._vendor.distlib.compat import raw_input


opdracht = 4

def scandir(dir):
    contents = os.listdir(dir)
    print("Er staan " + str(len(contents)) + " items in " + dir)
    for item in contents:
        if identifypdf(item) == True:
            print(item + str(mimetypes.guess_type(item)[0]))
        elif identifyoffice(item) == True:
            print(item + str(mimetypes.guess_type(item)[0]))


def welcome():
    print("Welkom bij opdracht " + str(opdracht))
    print("Op het moment bevind u zich in: " + os.getcwd() + "\n")
    antwoord = raw_input("Welke map wilt u onderzoeken? ")
    print("U heeft ingevoerd: " + antwoord + ". De map zal nu aangeroepen worden.")
    scandir(antwoord)


def identifypdf(file):
    if mimetypes.guess_type(file)[0] == "application/pdf":
        return True


def identifyoffice(file):
    filetypes = ['application/msword',\
                 'application/x-msexcel']

    for type in filetypes:
        if mimetypes.guess_type(file)[0] == type:
            return True
