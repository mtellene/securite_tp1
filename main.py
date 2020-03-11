import random
import math


# calcule le pgcd
def pgcd(a, b):
    if b == 0:
        return a
    else:
        r = a % b
        return pgcd(b, r)


# calcule si le nombre est premier ou pas
def estpremier(n):
    nombre = int(n)
    i = 2
    while i < nombre and nombre % i != 0:
        i = i + 1
    if i == nombre:
        return True
    else:
        return False


# calcule p et q
def getPAndQ():
    p = random.randint(1, 100)
    q = random.randint(1, 100)
    estpremier(p)
    while not estpremier(p):
        p = random.randint(1, 100)
    while not estpremier(q):
        q = random.randint(1, 100)
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
    C = pow(chiffre, e) % n
    return C


# decrypte un chiffre
def dechiffrement(chiffrement, d, n):
    M = pow(chiffrement, d) % n
    return M


# permet de factoriser un chiffre
def factorisation(n):
    F = []
    if n == 1:
        return F
    # recherche de tous les facteurs 2 s'il y en a
    while n >= 2:
        x, r = divmod(n, 2)
        if r != 0:
            break
        F.append(2)
        n = x
    # recherche des facteurs 1er >2
    i = 3
    rn = math.sqrt(n) + 1
    while i <= n:
        if i > rn:
            F.append(n)
            break
        x, r = divmod(n, i)
        if r == 0:
            F.append(i)
            n = x
            rn = math.sqrt(n) + 1
        else:
            i += 2
    return F


# crypte et decrypt un chiffre avec p,q,e genere aleatoirement
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
    aChiffrer = int(input("Entrez un chiffre à crypter : "))  # si on veut entrer le chiffre a crypter et decrypter
    # aChiffrer = random.randint(0, n - 1)  # on choisit un chiffre aléatoirement entre 0 et n-1
    while aChiffrer >= n:  # tant que le chiffre est superieur ou egale a n
        print('Entrez une valeur inférieur à', n)
        aChiffrer = int(input("Entrez un chiffre à crypter : "))
    cCrypter = chiffrement(aChiffrer, e, n)  # on crypte le chiffre
    print(aChiffrer, 'chiffré :', cCrypter)  # on affiche le chiffre crypte
    cDecrypter = dechiffrement(cCrypter, d, n)  # on decrypte le chiffre crypte
    print(cCrypter, 'déchiffré :', cDecrypter)  # on affiche le chiffre decrypte


# decrypte un message trouver p,q,d sachant e,n,
def decryptMessageAvecKp(e, n, message):
    L = []  # creation d'une liste ou
    p, q = factorisation(n)
    phiN = (p - 1) * (q - 1)
    d = algoEuclidien(e, phiN)
    print('p =', p, 'q =', q, 'phiN :', phiN, 'd =', d)
    for i in range(len(message)):
        cDecrypter = dechiffrement(message[i], d, n)
        L.append(cDecrypter)
    print(L)


def main():
    print('1 -> crypter et décrypter un chiffre avec p, q et e généré aléatoirement')
    print('2 -> décrypter un chiffre avec la clé publique')
    choix = int(input('Choix : '))
    if choix == 1:
        crypterDecrypterChiffre()
    elif choix == 2:
        e = int(input('Entrez e : '))
        n = int(input('Entrez n : '))
        # message = [9197, 6284, 12836, 8709, 4584, 10239, 11553, 4584, 7008, 12523, 9862, 356, 5356, 1159, 10280, 12523, 7506, 6311]
        # findMessageTTKp(e, n, message)
        message2 = [671828605, 407505023, 288441355, 679172842, 180261802]
        decryptMessageAvecKp(e, n, message2)


if __name__ == "__main__":
    main()
