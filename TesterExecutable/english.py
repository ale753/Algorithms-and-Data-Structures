import os
import tkinter
import time
import random
from tkinter.scrolledtext import ScrolledText
import matplotlib.pyplot as plt
import numpy as np
import _thread
import threading

#variabili globali necessarie
leng = 0
A = [] # Vettore su cui vengono effettuate le operazioni di Sort
A1 = [] # Vettore di supporto
lock = 0 #Unico semaforo per la sincronizzazione dei Thread
k = 0 # valore k
font = 'calibri'
algorithms = ["HeapSort", "MergeSort", "CountingSort", "InsertionSort"]


# scrivere questo su moduli separati
def counting_sort(A, k) :

    B = [None]*(len(A))
    C = []

    for i in range (0, k+1) :
        C.insert(i, 0)

    for j in range (0, len(A)) :
        C[A[j]] = C[A[j]] + 1


    for j in range (1, k+1) :
        C[j] = C[j] + C[j-1]

    for j in range (len(A)-1, -1, -1) :
        B[C[A[j]]-1] = A[j]
        C[A[j]] = C[A[j]]-1

    return B


def insertion_sort(A) :

    for j in range (1, len(A)) :
        key = A[j]
        i = j - 1

        while(i >= 0  and A[i] > key) :
            A[i + 1] = A[i]
            i = i - 1

        A[i + 1] = key


def Merge(A, p, q, r) :

    n1 = q-p+1
    n2 = r-q

    L = []
    R = []

    for i in range (0, n1) :
        L.insert(i, A[p+i])

    for j in range (0, n2) :
        R.insert(j, A[q+j+1])

    i=0
    j=0
    k=p

    while (i < n1 and j < n2) :

        if (L[i] <= R[j]):
            A[k] = L[i]
            i=i+1

        else :
            A[k] = R[j]
            j=j+1

        k=k+1

    while (i< n1):
        A[k] = L[i]
        i=i+1
        k=k+1

    while (j < n2):
        A[k] = R[j]
        j=j+1
        k=k+1



def MergeSort(A, p, r) :
    if p < r :
        q = int((p+r)/2)
        MergeSort(A, p, q)
        MergeSort(A, q+1, r)
        Merge(A, p, q, r)


def left(i):

    return 2*i;

def right(i) :
    return ((2*i) + 1)

def swap( A, x, y ) :
    tmp = A[x]
    A[x] = A[y]
    A[y] = tmp


def MaxHeapify(A, i, heapsize) :

    l = left(i)
    r = right(i)
    largest = i;

    if(l <= heapsize and A[l] > A[i]) :
        largest = l;

    if(r <= heapsize and A[r] > A[largest]) :
        largest = r;

    if(largest != i ) :
        swap(A, i, largest)
        MaxHeapify(A, largest, heapsize)


def BuildMaxHeap(A) :
    heapsize=len(A)-1
    leastParent = int(len(A)/2)
    for i in range (leastParent , -1, -1 ):
        MaxHeapify(A, i,heapsize)


def HeapSort(A) :

    BuildMaxHeap(A)
    heapsize=len(A)-1
    for i in range (heapsize, 0, -1) :
        swap(A,0,i)
        heapsize = heapsize - 1
        MaxHeapify(A, 0, heapsize)


def Partition(A, p, r) :
    x = A[r]
    i = p - 1
    for j in range(p, r ) :
        if A[j] <= x :
            i = i + 1
            swap(A, i, j)
    swap(A,i + 1, r )
    return (i + 1)






# scrivere questo su moduli separati

#Funzione di scrittura su file
def writefile (a, title) :
    f = open(title+'.txt','w')
    j = 0
    for i in range (len(a)) :
        j = a[i]
        f.write(' ')
        f.write(str(j))

    f.close()


def GetAlgorithm() :
    global A
    global k
    switcher = {

        algorithms[0] : (HeapSort, (A,) ), #Tupla di un singolo elemento, importante
        algorithms[1] : (MergeSort, (A, 0, len(A) - 1) ),
        algorithms[2] : (counting_sort ,(A, k) ),
        algorithms[3] : (insertion_sort, (A,) ),


    }
    return switcher

#La funzione prende in ingresso algtype, scelto in base al bottone cliccato sul men�. Vedere codice dell'interfaccia grafica
def algorithmcommand(algorithm_name) :
    global lock
    global A
    global k

    lock.acquire()
    leng = len(A)

    if algorithm_name == "CountingSort" :
        #caso counting sort
        A.clear()
        t.insert(tkinter.END, "Generating new array for CountingSort" + '\n')
        k = int(leng/2 - 1)
        for i in range(leng) :
            A.insert(i, random.randint(0,k))


    #DISPLAY VETTORE DI PARTENZA
    t.insert(tkinter.END, "Input array :" + '\n' + "{}".format( A[:50] ), font)
    if (leng > 50) : #Nel caso in cui il vettore superi una certa lunghezza, ne si fa il display a video solo di una parte
        t.insert(tkinter.END, '\n' + "...and other %s" %(len(A) - 50), font)


    t.insert(tkinter.END, '\n' + "Sorting array..." + '\n', font)

    Algorithm = GetAlgorithm()[algorithm_name]
    arguments = list(Algorithm[1])

    start_time = time.time()
    B = Algorithm[0] (*arguments)
    time1 = time.time() - start_time
    if(B) :
        A = B[:]
    t.insert(tkinter.END, "TIME : %s SECONDS." %time1 + '\n', font)


    t.insert(tkinter.END, "Array sorted with %s :" %algorithm_name + '\n' + "{}".format( A[:50] ), font)

    if (leng > 50) : #Nel caso in cui il vettore superi una certa lunghezza, ne si fa il display a video solo di una parte
        t.insert(tkinter.END, '\n' + "...and other %s" %(len(A) - 50), font)



    if (leng < 10000) :

        writefile(A, 'Vettore ordinato')
        t.insert(tkinter.END, '\n' + "Saved on .txt file" + '\n', font)


    #Siccome A � stato sostituito col suo corrispettivo ordinato, A1 � la copia precedente di A non ordinato.
    #Si resetta A in modo da poter di nuovo effettuare operazioni sul precedente vettore non ordinato.
    A = A1[:]
    displayline()
    lock.release()


#Funzione che genera un vettore casuale dato una determinata dimensione
def generavettore(dim) :
    global A
    global A1
    A.clear()
    for i in range(dim) :
        A.insert(i, random.randint(0, dim))


    t.insert(tkinter.END, "Generated array :" + '\n' + "{}".format(A[:50]), font)
    if (dim > 50) :
        t.insert(tkinter.END, '\n' + "...and other %s" %(len(A) - 50) + '\n', font)
    #salva il vettore per future operazioni

    savedata(A)
    displayline()


#Funzione che consente di inserire un vettore da tastiera
def inseriscivett() :
    global A
    global A1
    # A = list(map(int, E2.get())) # convertire a int
    try :
        if  not (bool(E2.get().strip())  ) : # se � vuota
            raise ValueError


        #E2 prende il valore in formato "string" presente nella Entry numero 2.
        #La Entry 2 sta a sinistra nell'interfaccia grafica, sotto il pulsante "Genera Vettore" (Riferirsi al codice dell'interfaccia grafica)
        A = stringtoarray(E2.get())

        t.insert(tkinter.END, "Input array : " + '\n' + "{}".format(A), font)
        savedata(A)
        displayline()


    except ValueError :
        t.insert(tkinter.END, "Error. Insert valid parameters" + '\n', 'alert')

#Lettura del vettore da file di testo
def leggifile():
    global A
    global A1
    ftypes = [('Text Files', '.txt')] # Al momento supporta solo file di tipo txt
    dlg = tkinter.filedialog.Open(filetypes = ftypes)
    fl = dlg.show()

    try :
        if fl != '': #se il nome del file � valido

            with open(fl, 'r') as myfile:
                A = stringtoarray(myfile.read().replace('\n', ' '))

            t.insert(tkinter.END, "Input from file : " + '\n' + "{}".format(A), font )

            savedata(A)
            displayline()
    except :
        t.insert(tkinter.END, "Error while reading file. Format must be (.txt)" + '\n', 'alert')
        displayline()




def stringtoarray(string) :
    array = []
    temp = ""
    alphanumeric = False

    #conversione stringa acquisita a numeri interi
    for char in string :
        if ((char.isalpha()) or (char.isdigit()) ) :
            temp = temp + char
            if(char.isalpha()) :
                alphanumeric = True
        else :
            if (temp is not ""):
                array.append(temp)
            temp = ""

    array.append(temp)

    if(alphanumeric is not True) :
        for i in range (len(array)) :

            if(array[i] == '') :
                array.remove(array[i])
            else :
                array[i] = int(array[i])

    return array


#Pulisce la finestra dell'interfaccia grafica da tutti gli output
def ClearWindow() :
    t.delete('1.0', tkinter.END)
#Linea di separazione tra le operazioni
def displayline() :
    t.insert(tkinter.END, "\n" + "-----------------------------------------------" + "\n", 'endline' )
def openexe() :
    try :
        os.startfile("alberi.exe")
    except :
        t.insert(tkinter.END, "Error. alberi.exe not found" + '\n', 'alert')

def savedata(A) :
    global A1
    A1 = A[:]


#Inizializzazione Thread per le operazioni.
#Si � ritenuto necessario utilizzare i thread poich� tkinter (per l'interfaccia grafica) � single Threaded,
#questo pu� comportare che l'interfaccia grafica si blocchi finch� un'operazione non viene eseguita, con conseguenti
#crash ed errori inattesi.

#Da test effettuati, comunque, questo non inficia in alcun modo il tempo di esecuzione degli algoritmi.

#La funzione prende in ingresso i, che � il comando associato al bottone cliccato nell'interfaccia.
#Per ragioni di leggibilit�, il nome del comando "i" � lo stesso nome del bottone nell'interfaccia grafica.

def ThreadInit(i) :
    global A

    #SWITCH sulle operazioni

    if(i == "GeneraVettore" ) :
        #tasto genera vettore
        try :

            leng = int(E1.get())

            threading.Thread(target = generavettore, args = (int(E1.get()), )).start()
            # _thread.start_new_thread( generavettore, ("Thread-1",int(E1.get()) ) )

        except ValueError :

            t.insert(tkinter.END, "Error. Lenght must be an integer greater than or equal to 0" + '\n', 'alert')

    elif (i == "TestaAlgoritmo") :
        #tasto testa algoritmo
        try :

            threading.Thread(target = testalgorithm, args = (variable.get() , int(E3.get()), int(E4.get()), int(E5.get()),variable2.get() )).start()
            # _thread.start_new_thread(testalgorithm,(variable.get() , int(E3.get()), int(E4.get()), int(E5.get()),variable2.get() ))

            t.insert(tkinter.END, "Testing " + variable.get() + " ..." + '\n', font)

        except  ValueError :
            t.insert(tkinter.END, "Error reading input parameters for testing. Try again with valid data" + '\n', 'alert')

    elif ( i == "MostraRisultati") :
        try :

            # Legge i risultati ottenuti dal test e li presenta in forma grafica
            # Li confronta anche con funzioni note nell'analisi degli algoritmi, come NlogN e N
            t2 = np.loadtxt('CampioniTempi.txt', dtype=int)
            d2 = np.loadtxt("CampioniDimensioni.txt", dtype = int)


            plt.grid(color = "b", linestyle = "-", linewidth = 0.1)
            plt.plot(d2 , t2, 'ro')
            plt.plot(d2 , t2, 'r--')
            plt.axis([ 0 ,d2[-1], 0, t2[-1]])
            plt.ylabel('Times')
            plt.xlabel('Input lenght')
            #t1 = np.arange(d2[0], d2[-1], d2[1] - d2[0])
            # t2 = np.arange(1.0, 283, 0.02)
            plt.title("Results")
            plt.figure(1)

            y = np.arange(0, 40000, 1)
            x = np.arange(0, d2[-1], 1)
            plt.plot(x, x, 'y')
            plt.plot(y, y**2, 'g')
            x1 = np.arange(1, d2[-1], 1)
            plt.plot(x1, x1 * np.log2(x1), 'b')

            plt.legend(['Samples', 'Interpolation', 'n', 'n^2', 'n*log2(n)'], loc='best')

            t.insert(tkinter.END, "Input array lenght | Time in microseconds" + '\n' + "{}".format((np.column_stack((d2, t2))) ), font)

            displayline()

            plt.show()

        except OSError :

            t.insert(tkinter.END, "Error. Test results not found" + '\n', 'alert')

    elif (i == "MostraRisultatiAlberi") :
        try :
            t2 = np.loadtxt('TempiAlbero.txt', dtype=int)
            d2 = np.loadtxt("DimensioniAlbero.txt", dtype = int)


            plt.grid(color = "b", linestyle = "-", linewidth = 0.1)
            plt.plot(t2 ,np.log2(d2+1), 'ro')
            plt.plot(t2 , np.log2(d2+1), 'r--')
            plt.axis([ 0 ,d2[-1], 0, 50])
            plt.ylabel('Times')
            plt.xlabel('Tree height ')
            plt.title("Tree results")
            plt.figure(1)

            x1 = np.arange(1, d2[-1], 1)
            plt.plot( x1, np.log2(x1), 'b')

            plt.legend(['Samples', 'Interpolation', 'log2(n)'], loc='best')


            t.insert(tkinter.END, "Tree lenght | Time in microseconds" + '\n' + "{}".format((np.column_stack((d2, t2)))), font)

            displayline()
            plt.show()



        except OSError :

            t.insert(tkinter.END, "Error. Tree test results not found." + '\n', 'alert')

    else :

        try :
            if (len(A) <= 0) :

                raise ValueError("Error. Insert valid input")

            threading.Thread(target = algorithmcommand, args = (i, )).start()

        except ValueError as err:

            t.insert(tkinter.END, err.args[0] + '\n', 'alert')




#Testing degli algoritmi.
#La funzione prende in ingresso il tipo di algoritmo da testare e in pi� :
# dim - Dimensione iniziale del vettore in input (che viene generato casualmente)
# fattoremoltiplicativo - A ogni iterazione del ciclo for, l'input viene moltiplicato per questo fattore, aumentando la dimensione del prossimo vettore da testare
# numripetizioni - Numero di iterazioni da eseguire
def testalgorithm(algorithm_name, dim , fattoremoltiplicativo, numripetizioni, inputtype) :
    global A
    global k
    lock.acquire()
    #prende da men� a tendina
    times = [] #Tempi di esecuzione
    dims = [] #Dimensioni

    j = dim * fattoremoltiplicativo

    times.insert(0, 0.0)
    dims.insert(0, 0)


    A.clear()
    misura = 0
    for rip in range (numripetizioni) :
        p = 0
        if (inputtype == "Random") :
            for i in range(dim) :
                A.insert(i, random.randint(0, int(dim/2 - 1)))

        elif (inputtype == "Crescente" or inputtype == "Decrescente"):
            for i in range(dim) :
                if(algorithm_name == "CountingSort"):
                    A.insert(i, p)
                    if ((i+1)%3 == 0) :
                        p+=1
                else :
                    A.insert(i, i)
            if(inputtype == "Decrescente") :
                A = A[::-1]

        k = int(len(A)/2 - 1)

        Algorithm = GetAlgorithm()[algorithm_name]
        arguments = list(Algorithm[1])

        start_time = time.time()
        Algorithm[0] (*arguments)
        misura = time.time() - start_time

        times.append(misura*1000000) #microsecondi
        dims.append(dim)
        clock.config(text="Time " + str(misura) + " | Array lenght " + str(dim) + " | Loop   " + str(rip+1))
        dim = dim + j # incremento dimensione per prossima iterazione
        A.clear()


    #Salvataggio su file di testo
    writefile(times, "CampioniTempi")
    writefile(dims, "CampioniDimensioni")

    t.insert(tkinter.END, "Test completed." + '\n', font)
    displayline()
    lock.release()



#inizio main


mainWindow = tkinter.Tk()

mainWindow.title("Smart Tester - Algorithms and Data Structures")
mainWindow.geometry('840x580')
mainWindow.iconbitmap('fedii.ico')



rightFrameS = tkinter.Frame(mainWindow)
rightFrameS.pack(side='right', anchor='n', expand = True)

rightFrame = tkinter.Frame(mainWindow)
rightFrame.pack(side='right', anchor='n', expand=True)

leftFrame = tkinter.Frame(mainWindow)
leftFrame.pack(side = 'left', anchor = 'n', expand = True)

bottomFrame = tkinter.Frame(mainWindow)
bottomFrame.pack(side = 'bottom', anchor = 'n', expand = True)


# t = tkinter.Text(mainWindow)
t = ScrolledText(mainWindow, borderwidth=3, relief="sunken")

#Colore per operazioni eseguite e per la endline
t.tag_config('alert', background="yellow", foreground="red")
t.tag_config('cmd', background="blue", foreground="white")
t.tag_config('calibri', font = "Calibri")
t.tag_config('endline', foreground = "blue")
t.pack()





#Bottoni parte destra dello schermo

buttons = []

for h in range (len(algorithms)) :
    buttons.insert ( h, tkinter.Button(rightFrame, command=lambda h = h : ThreadInit(algorithms[h]),  text=algorithms[h]) ) #h = h per operazioni su lambda
    buttons[h].pack(side = 'top')


# button1 = tkinter.Button(rightFrame, command=lambda : ThreadInit("HEAP-SORT"),  text="Heapsort")
# button2 = tkinter.Button(rightFrame, command=lambda : ThreadInit("MERGE-SORT"), text="MergeSort")
# button4 = tkinter.Button(rightFrame, command=lambda : ThreadInit("COUNTING-SORT"), text="CountingSort")
# button5 = tkinter.Button(rightFrame, command=lambda : ThreadInit("INSERTION-SORT"), text= "InsertionSort")
button3 = tkinter.Button(rightFrame, command=ClearWindow, text="ClearWindow", fg = 'red')

#Bottoni parte inferiore dello schermo
button6 = tkinter.Button(bottomFrame, command=lambda : ThreadInit("TestaAlgoritmo"),  text="Test Algorithm")
button7 = tkinter.Button(bottomFrame, command=lambda : ThreadInit("MostraRisultati"),  text="Show results")

button8 = tkinter.Button(rightFrame, command= openexe,  text="Open tree subprogram")
button9 = tkinter.Button(rightFrame, command=lambda : ThreadInit("MostraRisultatiAlberi"),  text="Show results (Tree)")
#pack on top bottoni a destra
# button1.pack(side='top')
# button2.pack(side='top')
# button4.pack(side='top')
# button5.pack(side='top')

button3.pack(side='top')

#pack on right bottoni parte inferiore
button7.pack(side = 'right')
button6.pack(side = 'right')


#Label sinistra dello schermo
label1 = tkinter.Label( leftFrame, text="Array lenght")
label2 = tkinter.Label (leftFrame, text = "Manual Input")
label3 = tkinter.Label(leftFrame, text = "Open file")

#Label parte inferiore
label4 = tkinter.Label(bottomFrame, text = ("Initial lenght : \n \n " + " Multiplication factor : \n \n" + "Loops : \n") )

tkinter.Label(rightFrame, text = "\n \n \n").pack()

button8.pack(side = 'top')
button9.pack(side = 'top')

E1 = tkinter.Entry(leftFrame, bd =5)
E2 = tkinter.Entry(leftFrame, bd = 5)
E3 = tkinter.Entry(bottomFrame, bd = 5)
E4 = tkinter.Entry(bottomFrame, bd = 5)
E5 = tkinter.Entry(bottomFrame, bd = 5)

genera = tkinter.Button(leftFrame, text ="Generate", command = lambda : ThreadInit("GeneraVettore"))
inserisci = tkinter.Button(leftFrame, text = "Insert", command = inseriscivett) #Thread non necessari in questi casi
leggi = tkinter.Button(leftFrame, text = "Open", command = leggifile) #Thread non necessari in questi casi

#w = tkinter.Label(mainWindow, text="red", bg="red", fg="white")
# w.pack(padx=5, pady=10, side="left")

lock = _thread.allocate_lock()

#men� a tendina
variable = tkinter.StringVar(bottomFrame)
variable.set(algorithms[0]) # default value

#random crescente e decrescente
variable2 = tkinter.StringVar(bottomFrame)
variable2.set("Random")



clock = tkinter.Label(mainWindow, font=('calibri', 12, 'bold'), bg='white', relief="groove")
clock.pack(fill="both", expand=1)




options = tkinter.OptionMenu(bottomFrame, variable, *algorithms)
options.pack()



inputopt = tkinter.OptionMenu(bottomFrame, variable2, "Random", "Ascending order", "Descending order")
inputopt.pack(side = "top")
#fine men� a tendina

label1.pack(side = 'top')

E1.pack(side = 'top')

genera.pack(side = 'top')

label2.pack(side = 'top')

E2.pack(side = 'top')

inserisci.pack(side = 'top')

label3.pack(side = 'top')

label4.pack(side = 'left')

leggi.pack(side = 'top')

E3.pack()

E4.pack()

E5.pack()

mainWindow.mainloop()
