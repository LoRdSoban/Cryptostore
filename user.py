import csv
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii
from Crypto import Random





banner =  '''
  _____              __                                 
 / ___/_____ _____  / /____  ___  ___  __ _  ___ _______
/ /__/ __/ // / _ \/ __/ _ \/ _ \/ _ \/  ' \/ -_) __(_-<
\___/_/  \_, / .__/\__/\___/_//_/\___/_/_/_/\__/_/ /___/
        /___/_/                                         

A online marketplace for services backed by bloackchain '''
     

def generate_key():
    rnd = Random.new().read
    print(type)
    print(rnd)
    keyPair = RSA.generate(1024, rnd )
    pubKey = keyPair.publickey()

    pubKeyPEM = pubKey.exportKey()
    keyPairPEM = keyPair.exportKey()
    print()
    print(type(keyPair))
    print()
    print(type(pubKey))

    return keyPairPEM.decode('ascii'), pubKeyPEM.decode('ascii')
    #print(f"Public key:  (n={hex(pubKey.n)}, e={hex(pubKey.e)})")
    #pubKeyPEM = pubKey.exportKey()
    #print(pubKeyPEM.decode('ascii'))
    
    #print(f"Private key: (n={hex(pubKey.n)}, d={hex(keyPair.d)})")
    #privKeyPEM = keyPair.exportKey()
    #print(privKeyPEM.decode('ascii'))
    
    #encryption
    #msg = b'A message for encryption'
    #encryptor = PKCS1_OAEP.new(pubKey)
    #encrypted = encryptor.encrypt(msg)
    #print("Encrypted:", binascii.hexlify(encrypted))

    #print()


    #decryptor = PKCS1_OAEP.new(keyPair)
    #decrypted = decryptor.decrypt(encrypted)
    #print(decrypted.decode("utf-8"))


def login():
    username_entered = input("Enter your username:")
    with open('names.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        found = False
        for row in csv_reader:
            if row != []:
                if username_entered == row[0]:
                    found = True
                    start(username_entered, row[1], row[2])

        if found == False:
            register(username_entered)

def register(user_name):

    priv, pub = generate_key()
    with open('names.csv', mode='a') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',') 
        csv_writer.writerow([user_name, priv, pub])

    pass

            
def start(user_name, priv, pub):
        #encryption
    #msg = b'A message for encryption'
    #encryptor = PKCS1_OAEP.new(pub)
    #encrypted = encryptor.encrypt(msg)
    #print("Encrypted:", binascii.hexlify(encrypted))
    keyPair = RSA
    keyPairPEM = priv.encode('ascii')
    keyPair = keyPairPEM.importKey()
    print()
    print(type(keyPair))
    print()
    #print(type(pubKey))

    #return keyPairPEM.decode('ascii'), pubKeyPEM.decode('ascii')

    print(type(priv))
    print()
    print(type(pub))
    print()


    #decryptor = PKCS1_OAEP.new(priv)
    #decrypted = decryptor.decrypt(encrypted)
    #print(decrypted.decode("utf-8"))
    



def main():
    print(banner)

    login()





if __name__ == "__main__":
    main()