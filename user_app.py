
import csv
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto import Random

banner =  '''
  _____              __                                 
 / ___/_____ _____  / /____  ___  ___  __ _  ___ _______
/ /__/ __/ // / _ \/ __/ _ \/ _ \/ _ \/  ' \/ -_) __(_-<
\___/_/  \_, / .__/\__/\___/_//_/\___/_/_/_/\__/_/ /___/
        /___/_/                                         

A online marketplace for services backed by blockchain!\n\n '''
     

def generate_key(user_name):
    rnd = Random.new().read
    #print(type)
    #print(rnd)
    keyPair = RSA.generate(1024, rnd )
    pubKey = keyPair.publickey()

    keyPairPEM = keyPair.exportKey().decode()
    pubKeyPEM = pubKey.exportKey().decode()

    priv_name = 'priv_'+ user_name +'.pem'
    pub_name = 'pub_'+ user_name +'.pem'
    with open(priv_name, 'a') as pr:
        pr.write(keyPairPEM)

    with open(pub_name, 'a') as pu:
        pu.write(pubKeyPEM)

    print("\nPrivate and Public keys are generated and stored" )
    return priv_name, pub_name


def login():
    username_entered = input("Enter your username:")

    with open('names.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        found = False
        for row in csv_reader:


            if row != []:

                if username_entered == row[0]:
                    found = True
                    print("\nUser already exists. Logged in...\n")
                    start(username_entered, row[1], row[2])

        if found == False:
            register(username_entered)

def register(user_name):

    priv, pub = generate_key(user_name)
    with open('names.csv', mode='a') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',') 
        csv_writer.writerow([user_name, priv, pub])

    pass

            
def start(user_name, priv, pub):
    priv_name = 'priv_'+ user_name +'.pem'
    pub_name = 'pub_'+ user_name +'.pem'
    priv_key = RSA.import_key(open(priv_name, 'r').read())
    pub_key = RSA.import_key(open(pub_name , 'r').read())

    print("Private and public keys are loaded successfully!\n\n")


    #print(type(priv_key))
    #print(type(pub_key))
    #print(type(pub_key))
 




def main():

    print(banner)

    login()
    
    input("Press ENTER to exit.") #Stops program from exiting




if __name__ == "__main__":
    main()
