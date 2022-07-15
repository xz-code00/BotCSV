from re import S


FILE_CSV_INPUT = "vs_20220714_NON-CONTABILE.txt"
FILE_CSV_OUTPUT = "new.txt"


#Apertura del file csv
f = open(FILE_CSV_INPUT,"r") 

with open(FILE_CSV_OUTPUT, "a") as text_file:
    text_file.write("data,ora,cli,numero,area geografica,durata,importo,nng,vis_cli,prefix")
    text_file.write("\n")

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
    a = 0

    lenLine = len(numero)

    if(numero[1] != '0'):
        numeroNuovo += "0039"
        leN = len(numeroCambiare)
        
        while(a < lenLine):
            try:
                numeroNuovo += numero[a]
            except:
                print("In esecuzione")   

            a += 1

    else:
        numeroNuovo += numero


#Viene generata la parte finale della stringa e accodata
    lineMod += numeroNuovo

    s = 0
    l = 0
    while(s < 11):
        if(lineCopy[l] == '"'):
            s += 1
        l += 1
    
    c = 0

    while(c < 17):
        try:
            lineMod = lineMod + lineCopy[s]
        
            if (lineMod[s] == '"'):
                c += 1
            s += 1
        except:
            c += 1


#Viene inserita la nuova stringa nel file
    with open(FILE_CSV_OUTPUT, "a") as text_file:
        text_file.write(lineMod)
    

    print("Riga generata con successo")
