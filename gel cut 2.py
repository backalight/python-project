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
f = 6466  # feuille Lee filter
r = 92964  # rouleau Lee filter
v = 0  # valeur pour avancement dans list RefGel


for x in range(n):
    print (("pour ", RefGel[v]))

    Par = eval(input("combien de PAR64 et ou 2k "))
    Par = 625 * Par  # calcul surface totale gel pour PAR

    Pc1k = eval(input("combien de PC 1k et ou decoupe 2K"))
    Pc1k = 462.25 * Pc1k  # calcul surface totale gel pour format PC

    Dec = eval(input("combien de decoupes 1K"))
    Dec = 342.25 * Dec  # calcul surface totale gel pour format  dec

    Cyc = eval(input("combien de cycliodes"))
    Cyc = 1118 * Cyc  # calcul surface totale gel pour cycliode Adb

    Fresnel = eval(input("combien de fresnels 5k"))
    Fresnel = 1600 * Fresnel  # calcul surface totale gel pour fresnel

    ############################################################################

    h = 0  # nombre de rouleaux
    b = 0  # nombre de feuilles
    a = 0  # quantite
    t = Par + Pc1k + Dec + Cyc + Fresnel  # superficie gel
    if t < 6466:
        b = b + 1
        print(("il faut 1 feuille de ", RefGel[v]))
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

    print(("POUR", RefGel[v], "Il faut:"\n"" ToTalrouleau[v], "rouleaux ,"\n"," ToTalfeuille[v]," "feuilles"))
    v = v + 1
