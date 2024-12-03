def trierListe(fichier = "./data.txt"):
    fic = open(fichier, 'r', encoding="utf-8")
    colonne1 = []
    colonne2 = []
    res = 0
    for ligne in fic:
        print(ligne.split(" "))
        colonne1.append(int(ligne.split(" ")[0]))
        colonne2.append(int(ligne.split(" ")[3][:-1]))
    colonne1.sort()
    colonne2.sort()
    for i in range(len(colonne1)):
        if colonne1[i] > colonne2[i]:
            res += colonne1[i] - colonne2[i]
        else:
            res += colonne2[i] - colonne1[i]
    print(res)

# trierListe()


def creerDict(fichier = "./test.txt"):
    fic = open(fichier, 'r', encoding="utf-8")
    dico = dict()
    for ligne in fic:
        if int(ligne.split(" ")[3][:-1]) not in dico.keys():
            dico[int(ligne.split(" ")[3][:-1])] = 0
        dico[int(ligne.split(" ")[3][:-1])] += 1
    return dico

def calc(fichier = "./data.txt"):
    dico = creerDict(fichier)
    fic = open(fichier, 'r', encoding="utf-8")
    res = 0
    for ligne in fic:
        if int(ligne.split(" ")[0]) in dico.keys():
            res += int(ligne.split(" ")[0]) * dico[int(ligne.split(" ")[0])]
    print(res)

calc()