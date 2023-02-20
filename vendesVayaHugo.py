#HUGO VAYA SIMEON

#DECLAREM ELS VECTORS

noms = []
preus = []
qVenudes = []

#CREEM EL BUCLE PRINCIPAL I A CONTINUACIO EL MENU QUE ENS TE QUE MOSTRAR

while True:

    print(' 1. Introduir un article nou')
    print(' 2. Fer una venda')
    print(' 3. Mostrar informació')
    print(' 4. Esborrar un article')
    print(' 5. Esborrar tots els articles')
    print(' 6. Eixir')

    opcio = int(input('Dis-me la opció que vols realitzar: '))

    #CREEM EL SEGON BUCLE QUE SERA EL ENCARREGAT DE EXECUTAR LES OPCIONS

    while opcio>6 or opcio<1:

        opcio = int(input('Dis-me una opcio correcta: '))

    #LA OPCIO 1 AFEGIRA UN ARTICLE

    if opcio == 1:

        article = input("Dis-me el nom del article que vols afegir: ")
        noms.append(article)

        valor = float(input('Preu del article: '))
        preus.append(valor)

        qVenudes.append(0)

    #LA OPCIO 2 FARA UNA VENTA

    if opcio == 2:

        nomProducte = input("Dis-me el nom del article que vols vendre: ")

        if nomProducte in noms:

            index = noms.index(nomProducte)

            quantitatVenuda = int(input('Dis-me la quantitat venuda: '))

            qVenudes[index] += quantitatVenuda

        else:

            print("Error")

    #LA OPCIO 3 ENS MOSTRARA LA INFORMACIO RECOLLIDA

    if opcio == 3:

        print("NOM".ljust(10)[:10], "QUANT".rjust(10)[:10], "PREU".rjust(10)[:10], "IMPORT".rjust(10)[:10])

        importTotal = 0

        for i in range(len(noms)):

            n = noms[i]
            p = preus[i]
            q = qVenudes[i]

            imp = int(q) * float(p)
            
            importTotal += imp

            print(str(n)[:10].ljust(10, ' '), str(q)[:10].rjust(10, ' '), str(p)[:10].rjust(10, ' '), str(imp)[:10].rjust(10, ' '))
        
        print("")
        print("TOTAL:"[:10].rjust(32, ' '), str(importTotal)[:10].rjust(10, ' '))
        print("")

    #LA OPCIO 4 ESBORRARA UN ARTICLE I TOTES LES SEVES CARACTERISTIQUES

    if opcio == 4:

        articleEsborrar = input("Dis-me el article que vols esborrar: ")

        if articleEsborrar in noms:

            index = noms.index(articleEsborrar)

            noms.pop(index)
            preus.pop(index)
            qVenudes.pop(index)

            print("Article esborrat")

        else:

            print("Article no trobat")
    
    #LA OPCIO 5 ESBORRARA TOTS ELS ARTICLES I TOTES LES CARACTERISTIQUES

    if opcio == 5:

        noms.clear()
        preus.clear()
        qVenudes.clear()

    #LA OPCIO 6 ENS DONARA LA OPORTUNITAT DE FINALITZAR EL PROGRAMA

    if opcio == 6:

        respuesta = input("Segur (s/n)? ")

        if respuesta == "s":

            break