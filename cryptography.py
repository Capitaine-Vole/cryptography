import random

enter = input("Entrez le text à crypter : ").lower()
key = input("Entrez la clée de chiffrement : ").lower()

while type(key) != int:
    try:
        key = int(key)
    except:
        key = input("Entrez la clée de chiffrement : ").lower()


#alphabetNum = {1:'a', 2:'b', 3:'c', 4:'d', 5:'e', 6:'f', 7:'g', 8:'h', 9:'i', 10:'j', 11:'k', 12:'l', 13:'m', 14:'n', 15:'o', 16:'p', 17:'q', 18:'r', 19:'s', 20:'t', 21:'u', 22:'v', 23:'w', 24:'x', 25:'y', 26:'z'} 
alphabetLetter = {'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5, 'f' : 6, 'g' : 7, 'h' : 8, 'i' : 9, 'j' : 10, 'k' : 11, 'l' : 12, 'm' : 13, 'n' : 14, 'o' : 15, 'p' : 16, 'q' : 17, 'r' : 18, 's' : 19, 't' : 20, 'u' : 21, 'v' : 22, 'w' : 23, 'x' : 24, 'y' : 25, 'z' : 26}

alphabetNum = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def ssplit(word): 
    return [char for char in str(word)]  

def encrypt(char, key):

    keylist = ssplit(key)
    for i in range(len(keylist)):
        keylist[i-1] = int(keylist[i-1])

    print(keylist)

    listt = []

    for o in range(len(char)):
        for i in range(26):
            if char[o] == alphabetNum[i-1]:
                listt.append(i)

    print(listt)

    associated = []

    it = 0

    for i in listt:
        i -= 1
        i += keylist[0]
        if i > 25:
            i = i - (26*(int(i/26)))
        print(i)
        associated.append(alphabetNum[i])

    associatedstr = ""
    for i in associated:
        associatedstr = associatedstr+i

    print(associatedstr)

def unencypt(char, key):

    keylist = ssplit(key)
    for i in range(len(keylist)):
        keylist[i-1] = int(keylist[i-1])

    print(keylist)

    listt = []

    for o in range(len(char)):
        for i in range(26):
            if char[o] == alphabetNum[i-1]:
                listt.append(i)

    print(listt)

    associated = []

    it = 0

    for i in listt:
        i -= 1
        i += keylist[0]
        if i > 25:
            i = i - (26*(int(i/26)))
        print(i)
        associated.append(alphabetNum[i])

    associatedstr = ""
    for i in associated:
        associatedstr = associatedstr+i

    print(associatedstr)

encrypt(enter, key)
