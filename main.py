import random
import math


# calcule le pgcd
def pgcd(a, b):
    if b == 0:  # si on compare a et rien
        return a
    else:
        r = a % b  # r = a mod b
        return pgcd(b, r)


# calcule si le nombre est premier ou pas
def estpremier(n):
    nombre = int(n)
    i = 2
    while i < nombre and nombre % i != 0:
        i = i + 1
    if i == nombre:  # si on arrive a i = nombre
        return True
    else:  # sinon si on arrive a nombre % i == 0
        return False


# calcule p et q
def getPAndQ():
    p = random.randint(1, 100)  # entier aléatoire entre 1 et 100
    q = random.randint(1, 100)  # entier aléatoire entre 1 et 100
    while not estpremier(p):  # tant que p n'est pas premier
        p = random.randint(1, 100)  # on retire p aléatoirement
    while not estpremier(q):  # tant que p n'est pas premier
        q = random.randint(1, 100)  # on retire q aléatoirement
    return p, q


# permet de calculer d
def algoEuclidien(e, phiN):
    r, u, v, r1, u1, v1 = e, 1, 0, phiN, 0, 1
    while r1:  # tant que r1 != 0
        q = r // r1
        r, r1 = r1, r - q * r1  # r prend la valeur de r1,
        u, u1 = u1, u - q * u1  # u prend la valeur de u1
        v, v1 = v1, v - q * v1  # v prend la valeur de v1
    return u % phiN


# crypte un chiffre
def chiffrement(chiffre, e, n):
    C = pow(chiffre, e, n)  # -> pow(chiffre,e)%n
    return C


# decrypte un chiffre
def dechiffrement(chiffrement, d, n):
    M = pow(chiffrement, d, n)  # -> pow(chiffre,d)%n
    return M


# permet de factoriser un chiffre
def factorisation(n):
    p = n - 2
    while n % p != 0:
        p = p - 2  # saut de 2 en 2 pour aller plus vite
    q = int(n / p)  # comme n = p*q -> q = n/p
    return p, q


# crypter et decrypter un chiffre avec p,q,e genere aleatoirement
def crypterDecrypterChiffre():
    p, q = getPAndQ()  # calcule de p et q
    while p == q:
        print(p, 'et', q, 'sont les memes... On recommence !')
        p, q = getPAndQ()  # on relance s'ils sont les memes
    n = p * q  # calcule de n
    phiN = (p - 1) * (q - 1)  # calcule de phi(n)
    e = random.randint(2, phiN - 1)  # on choisit un e aléatoirement entre 2 et phi(n)-1
    while pgcd(e, phiN) != 1:
        e = random.randint(2, phiN - 1)
    d = algoEuclidien(e, phiN)  # on choisit d alétoirement entre e et phi(n)
    ############## zone d'affichage ##############
    print('p =', p, '/ q =', q, '/ n =', n, '/ phiN =', phiN)
    print('Kp:(', e, ';', n, ')')
    print('Kpr:(', d, ';', n, ')')
    choix = str(input("Voulez-vous entrer un chiffre (y/n)? "))
    if choix == 'y':  # si on veut entrer un chiffre
        aChiffrer = int(input("Entrez un chiffre : "))  # si on veut entrer le chiffre a crypter et decrypter
        while aChiffrer >= n:  # tant que le chiffre est superieur ou egale a n
            print('Entrez un chiffre inférieur à', n)
            aChiffrer = int(input("Entrez un chiffre : "))
    elif choix == 'n':  # si on ne veut pas
        choix = str(input("Voulez-vous générer un chiffre (y/n) ? "))
        if choix == 'y':  # si on veut generer un nombre
            aChiffrer = random.randint(0, n - 1)  # on choisit un chiffre aléatoirement entre 0 et n-1
        else:  # sinon
            print('Au revoir !')
            return
    else:  # si autre chose est rentré
        print('Je n\'ai pas compris votre demande !')
        print('Au revoir !')
        return
    choix = str(input('Crypter et décrypter le chiffre (y/n) ? '))
    if choix == 'y':
        cCrypter = chiffrement(aChiffrer, e, n)  # on crypte le chiffre
        print(aChiffrer, 'chiffré donne ', cCrypter)  # on affiche le chiffre crypte
        cDecrypter = dechiffrement(cCrypter, d, n)  # on decrypte le chiffre crypte
        print(cCrypter, 'déchiffré donne ', cDecrypter)  # on affiche le chiffre decrypte
    elif choix == 'n':
        choix = str(input('Crypter le chiffre (y/n) ? '))
        if choix == 'y':  # si on veut crypter le chiffre
            cCrypter = chiffrement(aChiffrer, e, n)  # on crypte le chiffre
            print(aChiffrer, 'chiffré donne ', cCrypter)  # on affiche le chiffre crypte
        elif choix == 'n':  # si on ne veut pas le crypter
            choix = str(input('Decrypter le chiffre (y/n) ? '))
            if choix == 'y':  # si on veut dechiffrer le chiffre
                cDecrypter = dechiffrement(aChiffrer, d, n)  # on decrypte le chiffre crypte
                print(aChiffrer, 'déchiffré donne ', cDecrypter)  # on affiche le chiffre decrypte
            else:  # sinon
                print('Annulation...')
                print('Au revoir !')
                return
        else:
            print('Annulation...')
            print('Au revoir !')
    else:
        print('Annulation...')
        print('Au revoir !')


# decrypte un message trouver p,q,d sachant e,n,
def decryptMessageAvecKp(e, n, message):
    L = []  # creation d'une liste ou
    p, q = factorisation(n)  # on calcule p et q avec n
    print('p =', p, 'q =', q)
    phiN = (p - 1) * (q - 1)  # calcule de phi(n)
    d = algoEuclidien(e, phiN)  # calcule de d
    for i in range(len(message)):
        cDecrypter = dechiffrement(message[i], d, n)  # on decrypte le chiffre a l'indice i
        L.append(cDecrypter)  # on ajoute la valeur decrypte a la liste
    print(L)


# retourne un alphabet
def getAlphabet():
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                'V', 'W', 'X', 'Y', 'Z', ' ', '.', '?', '€', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    return alphabet


# calcule le nombre de tuple et N
def getNbOfTheTupleAndNewN(k, N, n):
    tuple = k  # tuple quand on cryptera notre message
    tmp = pow(N, tuple) - 1
    while tmp < n:
        tuple = tuple + 1
        tmp = pow(N, tuple) - 1
    return tuple


# mettre le message (chaine de caractere) sous forme de liste en séparant par bloc
def fromMessageToList(message, k):
    liste = []
    if (len(
            message) / k) * 2 % 2 != 0:  # obligé de mettre *2 -> si k=2 et len(mess)=6 -> divion=3 -> 3%2 !=0 => rajout d'un A
        longueur = int(len(message) / k) + 1
    else:
        longueur = int(len(message) / k)
    for i in range(0, longueur):
        liste.append([])  # liste où le message sera segmenter en paquet
        for j in range(i * k, i * k + k):  # on fait des pas de k, car paquet de taille k
            if j >= len(message):  # si on est a la fin du mot
                liste[i].append('A')  # on met A
                break
            liste[i].append(message[j])  # on ajoute le caractere
    return liste


# recuperer les valeurs de chaque lettre du message
def getValuesOfLetters(liste):
    alphabet = getAlphabet()  # on recupere l'alphabet
    listeValeur = []  # liste où il y aura la valeur de chaque lettre
    for i in range(len(liste)):
        listeValeur.append([])
        for j in range(len(liste[i])):
            lettre = liste[i][j]  # on recupere la lettre
            for k in range(len(alphabet)):
                if alphabet[
                    k] == lettre:  # on compare la lettre a l'alphabet, tant qu'on a pas trouver la lettre -> i++
                    listeValeur[i].append(k)  # on recupere l'indice de la lettre et on considere que c'est la valeur
    return listeValeur


# converti les paquets en chiffre pret a etre crypter
def paquetToInt(listeValeur, N):
    paquetToInt = []  # liste où il y aura les paquets sont forme de int
    for i in range(len(listeValeur)):
        crypter = 0
        exposant = len(listeValeur[0]) - 1  # longueur du paquet -1
        for j in range(len(listeValeur[i])):
            if exposant == 0:  # pow(N,0)
                crypter = crypter + listeValeur[i][j]
                break
            crypter = listeValeur[i][j] * pow(N, exposant)
            exposant = exposant - 1
        paquetToInt.append(crypter)
    return paquetToInt


# permet de crypter les chiffres (paquets convertis)
def cryptPaquet(listPaquetInt, e, n):
    paquetCrypte = []  # liste où il y aura les paquets cryptés
    for i in range(len(listPaquetInt)):
        paquet = pow(listPaquetInt[i], e, n)  # -> pow(liste,e)%n
        paquetCrypte.append(paquet)
    return paquetCrypte


# calcule les tuples en fonction des paquets cryptés
def makeTuple(paquetCrypte, tuple, N):
    listOfTuple = []  # liste où il y aura les tuples des messages cryptés
    for i in range(len(paquetCrypte)):
        listOfTuple.append([])
        val = paquetCrypte[i]  # on donne la valeur du paquet crypté que l'on doit mettre en tuple
        tmp = tuple - 1  # pour l'exposant
        for j in range(tuple):
            test = pow(N, tmp)
            if test > val:
                listOfTuple[i].append(0)
            else:
                c = int(val / test)  # on prend la partie eniter de val/test (val = c*test)
                listOfTuple[i].append(c)
                val = val - c * pow(N, tmp)
            tmp = tmp - 1
    return listOfTuple


# permet de crypter un texte (pour l'instant txt en dur dans la fonction)
def crypteText(e, n, message):
    alphabet = getAlphabet()
    N = len(alphabet)  # nombre de caracteres auxquels on a droit
    k = int(math.log(n, N))  # k min est le nombre de tuple
    tuple = getNbOfTheTupleAndNewN(k, N, n)
    print('message =', message)
    liste = fromMessageToList(message, k)  # liste avec le message séparé en bloc
    listeValeur = getValuesOfLetters(liste)  # liste avec les valeurs
    listPaquetInt = paquetToInt(listeValeur, N)  # liste avec les paquets converti en chiffre
    paquetCrypte = cryptPaquet(listPaquetInt, e, n)  # liste avec les paquets cryptés
    listOfTuple = makeTuple(paquetCrypte, tuple, N)
    for i in range(len(liste)):
        print(liste[i], '=>', listPaquetInt[i], '=>', paquetCrypte[i], '=>', listOfTuple[i])
    print('----------------------------------')
    return N, listOfTuple, tuple, k


# converti le tuple en un chiffre (C)
def fromTupleToSingleInt(listOfTuple, choix, tuple, N):
    tupleToDecrypt = listOfTuple[choix - 1]
    tmp = tuple - 1
    val = 0
    for i in range(len(tupleToDecrypt)):
        val = val + tupleToDecrypt[i] * pow(N, tmp)  # tuple[i]*N^tmp
        tmp = tmp - 1
    return val


# converti le message crypter en la somme des valeurs de chaque lettre
def decryptIntToLettersValues(n, e, val):
    p, q = factorisation(n)
    phiN = (p - 1) * (q - 1)
    d = algoEuclidien(e, phiN)
    cDecrypt = dechiffrement(val, d, n)
    return cDecrypt


# décompose la somme des valeurs en tuples avec les valeurs de chaque lettre
def getLettersValues(k, cDecrypt, N):
    singleTuple = []
    exposant = k - 1  # longueur du paquet -1
    tmp = cDecrypt
    while exposant >= 0:
        if exposant == 0:
            singleTuple.append(cDecrypt)
            break
        test = pow(N, exposant)
        if test > cDecrypt:
            singleTuple.append(0)
            break
        tmp = int(tmp / test)
        singleTuple.append(tmp)
        cDecrypt = cDecrypt - tmp * test
        exposant = exposant - 1
    return singleTuple


# permet d'avoir les lettres grace au tuple
def getLetter(singleTuple):
    listOfLetters = []
    for i in range(len(singleTuple)):
        alphabet = getAlphabet()
        aChercher = singleTuple[i]
        listOfLetters.append(alphabet[aChercher])
    return listOfLetters


# permet de decrypter un tuple (from int to string)
def decrypteText(listOfTuple, tuple, N, e, n, k):
    print(listOfTuple)
    choix = int(input('Entrez le tuple à décoder : '))  # tuple a decrypter
    while choix < 1 or choix > len(listOfTuple):
        print('Entrez un chiffre entre 1 et', len(listOfTuple), '!')
        choix = int(input('Entrez le tuple à décoder : '))
    print(listOfTuple[choix - 1])
    val = fromTupleToSingleInt(listOfTuple, choix, tuple, N)  # val = message crypte
    cDecrypt = decryptIntToLettersValues(n, e,
                                         val)  # cDecrypt = somme des valeurs des lettres a partir du message crypte
    singleTuple = getLettersValues(k, cDecrypt,
                                   N)  # liste où il y aura le tuple des correspondant a la valeur de chaque lettre
    listOfLetters = getLetter(singleTuple)
    print(val, '=>', cDecrypt, '=>', singleTuple, '=>', listOfLetters)


def main():
    print('1 -> crypter et/ou décrypter un chiffre (p, q et e généré aléatoirement)')
    print('2 -> décrypter une liste de chiffre avec la clé publique')
    print('3 -> crypter un texte avec la clé publique')
    choix = int(input('Choix : '))
    if choix == 1:
        crypterDecrypterChiffre()
    elif choix == 2:
        e = int(input('Entrez e : '))
        n = int(input('Entrez n : '))
        message = [9197, 6284, 12836, 8709, 4584, 10239, 11553, 4584, 7008, 12523, 9862, 356, 5356, 1159, 10280, 12523,
                   7506, 6311]
        decryptMessageAvecKp(e, n, message)
        # message2 = [671828605, 407505023, 288441355, 679172842, 180261802]
        # decryptMessageAvecKp(e, n, message2)
    elif choix == 3:
        # pour test e=3 et n=2047
        e = int(input('Entrez e : '))
        n = int(input('Entrez n : '))
        message = str(input('Entrez le message à crypter : '))
        message = message.upper()
        N, listOfTuple, tuple, k = crypteText(e, n, message)
        decrypteText(listOfTuple, tuple, N, e, n, k)


if __name__ == "__main__":
    main()
