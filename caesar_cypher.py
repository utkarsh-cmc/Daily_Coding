#author - utkarsh
#caesar cypher is a simple cypher where the alphabet in the input string is changed or replace with the n(given key) no. of next alphabet.
import string

def caesar_cypher(usertext,key):

    alphabet=string.ascii_lowercase                 
    shifted=alphabet[key:] + alphabet[:key]

    table=str.maketrans(alphabet,shifted)

    encrypt=usertext.translate(table)
    print(encrypt)

userInputs = input("enter the text: ")
key = int(input("enter the shift key: "))
usertext=userInputs.lower()

caesar_cypher(usertext,key)