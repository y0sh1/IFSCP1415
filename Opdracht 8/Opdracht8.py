import Opdracht2
import Opdracht3
import Opdracht4
import Opdracht5
import Opdracht6
import Opdracht7

Opdracht = 8

def welcome():
    print("Dit is opdracht " + str(Opdracht) + ".\n")
    ans = menu()
    if(ans == "1"):
        print("hello world")
    elif(ans == "2"):
        Opdracht2.welcome()
    elif(ans == "3"):
        Opdracht3.main()
    elif(ans == "4"):
        Opdracht4.welcome()
    elif(ans == "5"):
        Opdracht5.welcome()
    elif(ans == "6"):
        Opdracht6.welcome()
    elif(ans == "7"):
        Opdracht7.welcome()
    welcome()

def menu():
    print("Hoofdmenu\n" +
        25 * "-" + "\n" +
        "1. Hello World\n"
        "2. Uitleg Python\n"
        "3. Bestandsverkenner\n"
        "4. Bestandszoeker\n"
        "5. GPS zoeker\n"
        "6. Encryptie/Decryptie\n"
        "7. Twitter API\n")
    ans = raw_input("Wat wilt u doen? ")
    return ans


welcome()