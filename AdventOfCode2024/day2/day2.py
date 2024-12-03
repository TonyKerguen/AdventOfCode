def countSafeLine(fichier = "./data.txt"):
    fic = open(fichier, 'r', encoding="utf-8")
    res = 0
    for line in fic:
        l = line.split(" ")
        l[-1] = l[-1][:-1]
        if lineIdSafe(l):
            res += 1
    print(res)

def lineIdSafe(l):
    increasing = False
    decreasing = False
    safe = True
    same = False
    for i in range(len(l)-1):
        if int(l[i]) < int(l[i+1]):
            increasing = True
            if (int(l[i+1]) - int(l[i])) > 3:
                return False
        if int(l[i]) > int(l[i+1]):
            decreasing = True
            if (int(l[i]) - int(l[i+1])) > 3:
                return False
        if int(l[i]) == int(l[i+1]):
            same = True
    print(l)
    print((increasing != decreasing) and not same)
    return (increasing != decreasing) and not same

countSafeLine()