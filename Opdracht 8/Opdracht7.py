import tweepy
import time
Opdracht = 7

def welcome():
    print("Welkom bij opdracht " + str(Opdracht))
    #insert your Twitter keys here
    consumer_key ='4idYcrgggfjwL5WWGGQqj0z3P'
    consumer_secret='qn2I4ssenNnHCqW7rZ6fxPrLYpec2pQ8FSD8J26li8UjaHU14Q'
    access_token='2522373451-e3RB96JvdU3yy6nlVyYNfn9oyedd1u4ylVUIEKZ'
    access_secret='v6SSBmVlQmoRaUBxv35fejoX3lTLHqIUPdgOrcYF2wtRI'

    auth = tweepy.auth.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth)

    list= open('list.txt','w')

    if(api.verify_credentials):
        print('Succesvol Ingelogt!')

    username = raw_input("Welke gebruiker wil je bekijken? ")
    user = tweepy.Cursor(api.followers, screen_name=username).items()
    print("Het programma zal alle volgers nu ophalen. Dit kan lang duren.")
    while True:
        try:
            u = next(user)
            list.write(u.screen_name +' \n')

        except:
            print ('Timeout :(. Sleep 30 seconds')
            time.sleep(15*2)
            u = next(user)
            list.write(u.screen_name +' \n')
    list.close()


