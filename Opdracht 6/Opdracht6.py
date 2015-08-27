from Crypto.Cipher import AES
import binascii

Opdracht = 6
key = 'mysecretpassword'
plaintext = 'Secret Message A'
ciphertext = binascii.unhexlify('e8da47acc08bc751745ef8fbff44e107')

def welcome():
    print("Welkom bij opdracht " + str(Opdracht))
    key = raw_input("Wat is de sleutel? (16 of 32 karakters)")
    keuze = raw_input("Wat wil je doen, 1 voor coderen, 2 voor de decoderen: ")
    try:
        if(keuze == "1"):
            plain = raw_input("Wat is de plaintext? (16 of 32 karakters)")
            print(encrypt(plain, key))
        elif(keuze == "2"):
            cipher = raw_input("Wat is de cipthertext?")
            print(decrypt(cipher, key))
        else:
            print("Geen goede keuze :(")
    except:
        print("Er ging iets fout. Waarschijnlijk heeft dit te maken met de ingevoerde tekst")


def encrypt(plain, key):
    encobj = AES.new(key, AES.MODE_ECB)
    ciphertext = encobj.encrypt(plain)
    # Resulting ciphertext in hex
    return ciphertext.encode('hex')

def decrypt(ciphertext, key):
    decobj = AES.new(key, AES.MODE_ECB)
    plaintext = decobj.decrypt(ciphertext.decode('hex'))
    # Resulting plaintext
    return plaintext

welcome()