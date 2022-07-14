FILE_CSV_INPUT = "c.txt"
FILE_CSV_OUTPUT = "new.txt"


#Apertura del file csv
f = open(FILE_CSV_INPUT,"r") 


#Ciclo eseguito per ogni riga
while True:
    line = f.readline()
    lineCopy = line
    numeroCambiare = ""
    lineMod = ""
    numero = ""
    numeroNuovo = ""

    if not line:
        print("end")
        exit()


#Prelievo del numero da sostiture dalla cella "prefix"
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


#Generazione e scrittura della parte antecedente della stringa
    x = 0
    y = 0

    while(x < 7):
        lineMod = lineMod + lineCopy[y]

        if(lineCopy[y] == '"'):
            x+=1

        y += 1
    

#Viene estratto per essere comparato il numero da modificare
    x = 0
    while(True):
        
        if(lineCopy[y] == '"'):
            break

        numero += lineCopy[y]

        y += 1

    

#Generazione e se necessario sostituzione della nuova numerazione
    a = 1

    lenLine = len(numero)
    if(numeroCambiare not in numero):
        if (numero[0] == '0' and numero[1] == '0'):
            numeroNuovo += '00'
        numeroNuovo += numeroCambiare
        lenN = len(numeroCambiare)

        while(a < lenN):
            try:
                numeroNuovo += numero[ lenLine + a]
            except:
                print("In esecuzione")   

            a += 1
    else:
        numeroNuovo = numero
    #print(numeroCambiare)



#Viene generata la parte finale della stringa e accodata
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


#Viene inserita la nuova stringa nel file
    with open(FILE_CSV_OUTPUT, "a") as text_file:
        text_file.write(lineMod)
        text_file.write("\n")

    print("Riga generata con successo")
