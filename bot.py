f = open("vs_202206.txt","r") 

while True:
    line = f.readline()
    lineCopy = line
    numeroCambiare = ""
    lineMod = ""
    numero = ""
    numeroNuovo = ""

    if not line:
        print("end")


    #Prende numero da copiare
    i = 0
    j = 0
    while(i < 19):
        if(line[j] == '"'):
            i+=1
        j+=1


    while(j < (len(line) - 2)):
        numeroCambiare += line[j]
        #print(line[j], end="")
        j+=1

    print ('\n')
    #Scrive prima parte della stringa
    x = 0
    y = 0

    while(x < 7):
        lineMod = lineMod + lineCopy[y]

        if(lineCopy[y] == '"'):
            x+=1

        y += 1
    

    #Ottenimento numero
    x = 0
    while(True):
        
        if(lineCopy[y] == '"'):
            break

        numero += lineCopy[y]

        y += 1

    

    #Ottenimento numero nuovo
    h = 0
    a = 1

    lenLine = len(numero)
    if(numeroCambiare not in numero):
        #numeroNuovo += '00'
        numeroNuovo += numeroCambiare
        lenN = len(numeroCambiare)

        while(a < lenN):
            try:
                numeroNuovo += numero[ lenLine + a]
            except:
                print("errore")   

            a += 1
    else:
        numeroNuovo = numero
    #print(numeroCambiare)

    #Fine stringa
    lineMod += numeroNuovo

    b = len(lineMod)
    c = 0
    z = 1


    while(c < 13):
        lineMod = lineMod + lineCopy[b]
        
        if (lineMod[b] == '"'):
            c += 1
        b += 1

    #print (lineMod)

    with open("new.txt", "a") as text_file:
        text_file.write(lineMod)
        text_file.write("\n")

    print("riga fatta")
