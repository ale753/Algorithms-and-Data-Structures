import tkinter
import time
import random
import math
import ModuleHeapsort
import ModuleMergesort
import ModuleInsertionCountSort
from tkinter.scrolledtext import ScrolledText
import matplotlib.pyplot as plt


leng = 0
A = []
A1 = []

def writefile (a, title) :
    f = open(title+'.txt','w')
    f.write(title+' : '+str(a))
    f.close()


def algorithmcommand(algtype) :
    global A
    algname = ''
    try :
        leng = len(A)
    except ValueError :
        leng = 0

    if (len(A) <= 0) :
        t.insert(tkinter.END, "Inserire dimensione valida per il vettore " + '\n')

    else :



        if algtype == 2 :

            #caso counting sort
            A = []

            t.insert(tkinter.END, "Vettore non valido per Counting-Sort. Generazione automatica nuovo vettore :" + '\n')
            for i in range(leng) :


                A.insert(i, random.randint(0, int(leng/2 - 1)))



        t.insert(tkinter.END, "VETTORE DI PARTENZA :" + '\n')

        if (leng > 50) :
            B = A[:50]
            t.insert(tkinter.END, B)
            t.insert(tkinter.END, '\n' + "...e altri %s elementi" %(len(A) - len(B)))
        else :
            t.insert(tkinter.END, A )

        t.insert(tkinter.END, '\n')


        writefile(A, 'Vettore random generato')

        t.insert(tkinter.END, "Salvato su file di testo" + '\n')

        t.insert(tkinter.END, "Ordinamento vettore in corso..." + '\n')

        if algtype == 0 :

            start_time = time.time()
            ModuleHeapsort.HeapSort(A)
            time1 = time.time() - start_time
            t.insert(tkinter.END, "TEMPO : %s SECONDI." %time1 + '\n')
            algname = "HEAP-SORT"

        elif algtype == 1 :


            start_time = time.time()
            ModuleMergesort.MergeSort(A, 0, (len(A)-1))
            time1 = time.time() - start_time
            t.insert(tkinter.END, "TEMPO : %s SECONDI." %time1 + '\n')
            algname = "MERGE-SORT"
        elif algtype == 2:

            start_time = time.time()
            A = ModuleInsertionCountSort.counting_sort(A, int(leng/2 - 1)+1)
            time1 = time.time() - start_time
            t.insert(tkinter.END, "TEMPO : %s SECONDI." %time1 + '\n')
            #da finire
            algname = "COUNTING-SORT"
        elif algtype == 3:

            start_time = time.time()
            ModuleInsertionCountSort.insertion_sort(A)
            time1 = time.time() - start_time
            t.insert(tkinter.END, "TEMPO : %s SECONDI." %time1 + '\n')
            algname = "INSERTION-SORT"
        t.insert(tkinter.END, "VETTORE ORDINATO CON %s : " %algname + '\n', 'alert')


        if (leng > 50) :
            B = A[:50]
            t.insert(tkinter.END, B)
            t.insert(tkinter.END, '\n' + "...e altri %s elementi" %(len(A) - len(B)))
        else :
            t.insert(tkinter.END, A )


        t.insert(tkinter.END, '\n')

        writefile(A, 'Vettore ordinato')
        t.insert(tkinter.END, "Salvato su file di testo" + '\n')



        t.insert(tkinter.END, "_______________________________________________" + '\n' , 'endline')


        A.clear()
        for i in range (leng) :
            A.insert(i, A1[i])


def generavettore() :
    global A
    global A1
    leng = int(E1.get())
    t.insert(tkinter.END, "Dimensione memorizzata " + '\n')
    t.insert(tkinter.END, "Genero vettore di partenza... " + '\n')
    A = []
    for i in range(leng) :
        A.insert(i, random.randint(0, int(leng/2 - 1)))

    t.insert(tkinter.END, "VETTORE GENERATO :" + '\n')

    if (leng > 50) :
        B = A[:50]
        t.insert(tkinter.END, B)
        t.insert(tkinter.END, '\n' + "...e altri %s elementi" %(len(A) - len(B)))
    else :
        t.insert(tkinter.END, A )

    t.insert(tkinter.END, '\n')


    #salva il vettore per future operazioni
    A1.clear()
    for i in range (leng) :
        A1.insert(i, A[i])

    t.insert(tkinter.END, "_______________________________________________" + '\n' , 'endline')

def inseriscivett() :
    global A
    global A1
    # A = list(map(int, E2.get())) # convertire a int
    A2 = E2.get()



    A = stringtointarray(A2)
    t.insert(tkinter.END, "Vettore inserito : " + '\n')
    t.insert(tkinter.END, A)
    t.insert(tkinter.END, '\n')
    t.insert(tkinter.END, "_______________________________________________" + '\n' , 'endline')

    print(A)
    A1.clear()
    for i in range (len(A)) :

        A1.insert(i, A[i])
    print(A1)

def leggifile():
    global A
    global A1

    ftypes = [('Text Files', '.txt')]
    dlg = tkinter.filedialog.Open(filetypes = ftypes)
    fl = dlg.show()

    try :
        if fl != '':
            with open(fl, 'r') as myfile:
                data=myfile.read().replace('\n', ' ')
                myfile.close()

            A = stringtointarray(data)

            t.insert(tkinter.END, "Vettore inserito : " + '\n')
            t.insert(tkinter.END, A)
            t.insert(tkinter.END, '\n')
            t.insert(tkinter.END, "_______________________________________________" + '\n' , 'endline')

            A1.clear()
            for i in range (len(A)) :
                A1.insert(i, A[i])
    except ValueError :
        t.insert(tkinter.END, "Errore nella lettura del file. Verificare che il formato sia corretto oppure che vi siano in input solo numeri interi" + '\n')
        t.insert(tkinter.END, "_______________________________________________" + '\n' , 'endline')


def stringtointarray(A2) :
    count = 0
    g = 0
    seq = 0
    A3 = []
    #conversione stringa acquisita a numeri interi
    for g in range (len(A2)) :
        if A2[g] == " " :
            seq = 0;
        else :
            seq = seq + 1
            if(seq >= 2) :
                temp = math.floor(math.log10(int(A2[g])))
                A3[-1] = (A3[-1]*10**(1+temp)+int(A2[g]))
            else :
                A3.append(int(A2[g]))
    return A3



def ClearWindow() :
    t.delete('1.0', tkinter.END)



#inizio main

mainWindow = tkinter.Tk()

mainWindow.title("Algoritmi e Strutture Dati")
mainWindow.geometry('840x480')
mainWindow.iconbitmap('fedii.ico')


rightFrame = tkinter.Frame(mainWindow)
rightFrame.pack(side='right', anchor='n', expand=True)

leftFrame = tkinter.Frame(mainWindow)
leftFrame.pack(side = 'left', anchor = 'n', expand = True)


# t = tkinter.Text(mainWindow)
t = ScrolledText(mainWindow, borderwidth=3, relief="sunken")

t.tag_config('alert', background="yellow", foreground="red")
t.tag_config('endline', foreground = "red")
t.pack()



button1 = tkinter.Button(rightFrame, command=lambda : algorithmcommand(0),  text="Heapsort")
button2 = tkinter.Button(rightFrame, command=lambda : algorithmcommand(1), text="MergeSort")
button4 = tkinter.Button(rightFrame, command=lambda : algorithmcommand(2), text="CountingSort")
button5 = tkinter.Button(rightFrame, command=lambda : algorithmcommand(3), text= "InsertionSort")
button3 = tkinter.Button(rightFrame, command=ClearWindow, text="ClearWindow", fg = 'red')

button1.pack(side='top')
button2.pack(side='top')
button4.pack(side='top')
button5.pack(side='top')
button3.pack(side='top')

label1 = tkinter.Label( leftFrame, text="Dimensione Vettore")

E1 = tkinter.Entry(leftFrame, bd =5)
E2 = tkinter.Entry(leftFrame, bd = 5)

genera = tkinter.Button(leftFrame, text ="Genera", command = generavettore)
inserisci = tkinter.Button(leftFrame, text = "Inserisci", command = inseriscivett)
leggi = tkinter.Button(leftFrame, text = "Apri", command = leggifile)

#w = tkinter.Label(mainWindow, text="red", bg="red", fg="white")
# w.pack(padx=5, pady=10, side="left")
label2 = tkinter.Label (leftFrame, text = "Inserimento manuale")
label3 = tkinter.Label(leftFrame, text = "Leggi da file")


r = 0



label1.pack(side = 'top')

E1.pack(side = 'top')

genera.pack(side = 'top')

label2.pack(side = 'top')

E2.pack(side = 'top')

inserisci.pack(side = 'top')

label3.pack(side = 'top')

leggi.pack(side = 'top')

mainWindow.mainloop()







