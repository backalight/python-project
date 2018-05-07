#Little project to count how many roll or/and sheet of color filter you need for your gig
#petit projet pour compter le nombre de rouleaux et/ou feuilles de gels necessaires pour un spectacle.
# entree nombre et ref gel
RefGel = []
ToTalfeuille = []
ToTalrouleau = []
n = eval(input("combien de ref?"))
for x in range(n):
    z = eval(input("l pour lee:"))
    RefGel.append(z)
f = 6466  # feuille Lee filter // lee filter sheet area
r = 92964  # rouleau Lee filter // lee filter roll area
v = 0  # valeur pour avancement dans list RefGel // value for index in RefGel list


for x in range(n):
    print ("pour ", RefGel[v])

    Par = eval(input("combien de PAR64 et ou 2k "))
    Par = 625 * Par  # calcul surface totale gel pour PAR // color frame area calculator for Par can

    Pc1k = eval(input("combien de PC 1k et ou decoupe 2K"))
    Pc1k = 462.25 * Pc1k  # calcul surface totale gel pour format PC // color frame area calculator for PC 2K

    Dec = eval(input("combien de decoupes 1K"))
    Dec = 342.25 * Dec  # calcul surface totale gel pour format  dec //  color frame area calculator for profile RJ 1k

    Cyc = eval(input("combien de cycliodes"))
    Cyc = 1118 * Cyc  # calcul surface totale gel pour cycliode Adb //  color frame area calculator for ADB cyc

    Fresnel = eval(input("combien de fresnels 5k"))
    Fresnel = 1600 * Fresnel  # calcul surface totale gel pour fresnel //  color frame area calculator for Fresnel 5K

    ############################################################################

    h = 0  # nombre de rouleaux // number of roll
    b = 0  # nombre de feuilles // number of sheet
    a = 0  # quantite
    t = Par + Pc1k + Dec + Cyc + Fresnel  # superficie gel // total area colorframe needed
    if t < 6466:
        b = b + 1
        print("il faut 1 feuille de ", RefGel[v])
    else:
        a = t // r
        h = h + a
        a = t - h * r
        a = t // f
        b = b + a
        a = t - f * b
    if 0 < a < f:
        b = b + 1
    while b >= 14:
        h = h + 1
        b = b - 14
    b = str(b)
    h = str(h)
    ToTalfeuille.append(b)
    ToTalrouleau.append(h)
    v += 1

################################################################################

# recap totale
print("##Recapitulatif##")
v = 0
for x in range(n):

    print("POUR", RefGel[v], "Il faut:", ToTalrouleau[v], "rouleaux, ", ToTalfeuille[v], "feuilles")
    v = v + 1
