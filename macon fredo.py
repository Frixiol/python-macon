from tkinter import *  # on importe tous la bibliothèque Tk
import math

fen = Tk()  # création d’une fenêtre Tk
fen.title("Calepinage")
fen.geometry("700x400")
fen.configure(bg='#D8D5E4')


# insérer les widgets et les appels de fonction

def error():
    labelEr = Label(fen, text="Error", bg='#D8D5E4')
    labelEr.pack()
    labelEr.place(relheight=0.2, relwidth=0.4, relx=0.2, rely=0.5)


def calcul():
    longP = inputlongP.get()
    largP = inputlargP.get()
    longgT = inputlonggT.get()
    larggT = inputlarggT.get()
    rad = var.get()
    squareM = (int(longP) * int(largP))/10000
    if rad == 1:
        longT = largT = 20
        colle = round(6 * squareM,1)
    elif rad == 2:
        longT = largT = 30
        colle = round(8 * squareM,1)
    elif rad == 3:
        longT = 20
        largT = 40
        colle = round(8 * squareM,1)
    elif rad == 4:
        longT = int(longgT)
        largT = int(larggT)
        colle = round(8*squareM,1)
        
    else:
        error()
    
    nbTuilelong = math.ceil(int(longP)/longT)
    nbTuilelarg = math.ceil(int(largP)/largT)
    nbTuile = nbTuilelong*nbTuilelarg
    
    paquets=1/(squareM/100)
    
    ouver(longP, largP, squareM, nbTuile,colle,paquets)
    # insérer votre code


def ouver(longP, largP, squareM, nbTuile,colle, paquets):
    labelShowLong1 = Label(fen, text="Longueur:", bg='#D8D5E4')
    labelShowLong1.pack()
    labelShowLong1.place(relx=0.1, rely=0.5)
    labelShowLong2 = Label(fen, text=(longP,"cm"), bg='#D8D5E4')
    labelShowLong2.pack()
    labelShowLong2.place(relx=0.22, rely=0.5)

    labelShowLarg1 = Label(fen, text="largeur:", bg='#D8D5E4')
    labelShowLarg1.pack()
    labelShowLarg1.place(relx=0.1, rely=0.55)
    labelShowLarg2 = Label(fen, text=(largP,"cm"), bg='#D8D5E4')
    labelShowLarg2.pack()
    labelShowLarg2.place(relx=0.22, rely=0.55)

    labelShowsquare1 = Label(fen, text="Surface:", bg='#D8D5E4')
    labelShowsquare1.pack()
    labelShowsquare1.place(relx=0.1, rely=0.6)
    labelShowsquare2 = Label(fen, text=(squareM,"m²"), bg='#D8D5E4')
    labelShowsquare2.pack()
    labelShowsquare2.place(relx=0.22, rely=0.6)

    labelShowsquare1 = Label(fen, text="Tuiles:", bg='#D8D5E4')
    labelShowsquare1.pack()
    labelShowsquare1.place(relx=0.1, rely=0.65)
    labelShowsquare2 = Label(fen, text=nbTuile, bg='#D8D5E4')
    labelShowsquare2.pack()
    labelShowsquare2.place(relx=0.22, rely=0.65)

    labelShowsquare1 = Label(fen, text="Kg de colle:", bg='#D8D5E4')
    labelShowsquare1.pack()
    labelShowsquare1.place(relx=0.1, rely=0.7)
    labelShowsquare2 = Label(fen, text=colle, bg='#D8D5E4')
    labelShowsquare2.pack()
    labelShowsquare2.place(relx=0.23, rely=0.7)

    labelShowsquare1 = Label(fen, text="nbr de paquets de carreaux:", bg='#D8D5E4')
    labelShowsquare1.pack()
    labelShowsquare1.place(relx=0.1, rely=0.7)
    labelShowsquare2 = Label(fen, text=paquets, bg='#D8D5E4')
    labelShowsquare2.pack()
    labelShowsquare2.place(relx=0.23, rely=0.75)

    calepinage()


def calepinage () :
 fen2 = Tk()  # création d’une fenêtre Tk
 fen2.title("affiche")
 fen2.geometry("600x400")
 
 longP = inputlongP.get()
 largP = inputlargP.get()


 canvas = Canvas(fen2, width= int(largP), height=int(longP), background='yellow')
 
 ligne1 = canvas.create_line(75, 0, 75, 120) # l'affectation dans une variable n'est pas obligatoire
 
 ligne2 = canvas.create_line(0, 60, 150, 60) # seulement si on a besoin de modifier l'élément
 
 txt = canvas.create_text(75, 60, text="Calepinage", font="Arial 16 italic", fill="Red")
 canvas.place(x=10,y=70)
 
 
 
 
 
 
 
 
 fen2.mainloop()




# ----programme principal----

labeltxt = Label(fen, text="Tailles careaux", bg='#D8D5E4')
labeltxt.pack()
labeltxt.place(relheight=0.1, relwidth=0.2, relx=0.68, rely=0.05)

var = IntVar()

bouton1 = Radiobutton(fen, text="20x20 cm", variable=var, value=1, bg='#D8D5E4')
bouton1.pack()
bouton1.place(relx=0.7, rely=0.15)

bouton2 = Radiobutton(fen, text="30x30 cm", variable=var, value=2, bg='#D8D5E4')
bouton2.pack()
bouton2.place(relx=0.7, rely=0.20)

bouton3 = Radiobutton(fen, text="20x40 cm", variable=var, value=3, bg='#D8D5E4')
bouton3.pack()
bouton3.place(relx=0.7, rely=0.25)

bouton4 = Radiobutton(fen, text="Personaliser", variable=var, value=4, bg='#D8D5E4')
bouton4.pack()
bouton4.place(relx=0.7, rely=0.30)



inputlongP = Entry(fen)
inputlongP.pack()
inputlongP.place(relheight=0.06, relwidth=0.1, relx=0.2, rely=0.1)

inputlargP = Entry(fen)
inputlargP.pack()
inputlargP.place(relheight=0.06, relwidth=0.1, relx=0.2, rely=0.2)

inputlonggT = Entry(fen)
inputlonggT.pack()
inputlonggT.place(relheight=0.06, relwidth=0.1, relx=0.65, rely=0.35)

inputlarggT = Entry(fen)
inputlarggT.pack()
inputlarggT.place(relheight=0.06, relwidth=0.05, relx=0.85, rely=0.35)

labeltxt1 = Label(fen, text="Longueur:", bg='#D8D5E4')
labeltxt1.pack()
labeltxt1.place(relheight=0.06, relwidth=0.1, relx=0.09, rely=0.1)

labeltxt2 = Label(fen, text="Largeur:", bg='#D8D5E4')
labeltxt2.pack()
labeltxt2.place(relheight=0.06, relwidth=0.1, relx=0.09, rely=0.2)

labeltxt3 = Label(fen, text="X", bg='#D8D5E4')
labeltxt3.pack()
labeltxt3.place(relheight=0.06, relwidth=0.1, relx=0.72, rely=0.35)

boutonL = Button(fen, text="Calculer", command=calcul)
boutonL.pack()
boutonL.place(relheight=0.1, relwidth=0.2, relx=0.1, rely=0.3)



canvas = Canvas(fen, height=5, background='white')
canvas.place(relx=0.05, rely=0.45, relwidth=0.9)

fen.mainloop()
