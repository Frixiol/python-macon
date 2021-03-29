a = "20x20"
b = "30x30"  # cm
c = "20x40"
d = 6  # kg de colle  /m²   pour a
f = 8  # idem               pour b et c
# x=input()  #type de carreaux
# z=input()  #taille du local  en m²

# nbrcarreaux=(z/(x/10000))


from tkinter import *  # on importe tous la bibliothèque Tk
import math

fen = Tk()  # création d’une fenêtre Tk
fen.title("fenetre")
fen.geometry("500x400")
fen.configure(bg='#D8D5E4')


# insérer les widgets et les appels de fonction

def error():
    labelEr = Label(fen, text="Error", bg='#D8D5E4')
    labelEr.pack()
    labelEr.place(relheight=0.2, relwidth=0.4, relx=0.2, rely=0.5)


def calcul():
    longP = inputlongP.get()
    largP = inputlargP.get()
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
    else:
        error()

    nbTuilelong = math.ceil(int(longP)/longT)
    nbTuilelarg = math.ceil(int(largP)/largT)

    nbTuile = nbTuilelong*nbTuilelarg


    if int(longP) > int(largP):
        canwidth = 500
        canheight = canwidth/(int(longP)/int(largP))
    elif int(longP) < int(largP):
        canheight = 500
        canwidth = canheight/(int(largP)/int(longP))
    else:
        canwidth=500
        canheight=canwidth

    squar_placex = canwidth/nbTuilelong
    squar_placey = canheight/nbTuilelarg

    ouver(longP,largP,longT,largT,squareM,nbTuile,colle,nbTuilelong,nbTuilelarg,canwidth,canheight,squar_placex,squar_placey)
    # insérer votre code


def ouver(longP,largP,longT,largT,squareM,nbTuile,colle,nbTuilelong,nbTuilelarg,canwidth,canheight,squar_placex,squar_placey):
    labelShowLong1 = Label(fen, text="Longueur:", bg='#D8D5E4')
    labelShowLong1.pack()
    labelShowLong1.place(relx=0.1, rely=0.5)
    labelShowLong2 = Label(fen, text=longP, bg='#D8D5E4')
    labelShowLong2.pack()
    labelShowLong2.place(relx=0.22, rely=0.5)

    labelShowLarg1 = Label(fen, text="largeur:", bg='#D8D5E4')
    labelShowLarg1.pack()
    labelShowLarg1.place(relx=0.1, rely=0.55)
    labelShowLarg2 = Label(fen, text=largP, bg='#D8D5E4')
    labelShowLarg2.pack()
    labelShowLarg2.place(relx=0.22, rely=0.55)

    labelShowsquare1 = Label(fen, text="m²:", bg='#D8D5E4')
    labelShowsquare1.pack()
    labelShowsquare1.place(relx=0.1, rely=0.6)
    labelShowsquare2 = Label(fen, text=squareM, bg='#D8D5E4')
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

    fen2 = Tk()  # création d’une fenêtre Tk
    fen2.title("affiche")
    fen2.geometry("600x600")
    fen2.configure(bg='#D8D5E4')
    DrawCanvas = Canvas(fen2,width=canwidth,height=canheight,bg='grey',borderwidth=0,highlightthickness=0)
    DrawCanvas.place(x=50,y=50)

    for i in range(nbTuilelarg):
        
        if i % 2==0:
            oddeven = 1
        else:
            oddeven = 2

        for y in range(nbTuilelong):
	
            if oddeven == 1:				
                if y % 2==0:
                    pattern = 'white'
                else:
                    pattern = 'black'
			
            if oddeven == 2:	
                if y % 2==0:
                    pattern = 'black'
                else:
                    pattern = 'white'
			
            squar = DrawCanvas.create_rectangle(squar_placex*y,squar_placey*i,(squar_placex*y)+squar_placex,(squar_placey*i)+squar_placey,fill=pattern)
    
    restecutx=squar_placex-((int(longP)/longT-math.floor(int(longP)/longT))*squar_placex)
    if restecutx == squar_placex:
        restecutx = 0	
		
    restecuty=squar_placey-((int(largP)/largT-math.floor(int(largP)/largT))*squar_placey)
    if restecuty == squar_placey:
        restecuty = 0	
 
    squarcut = Canvas(fen2,width=squar_placex,height=canheight,bg='#D8D5E4',borderwidth=0,highlightthickness=0)
    squarcut.place(x=50+canwidth-restecutx/2,y=50)
    squarcut = Canvas(fen2,width=squar_placex,height=canheight,bg='#D8D5E4',borderwidth=0,highlightthickness=0)
    squarcut.place(x=50-squar_placex+restecutx/2,y=50)
    squarcut = Canvas(fen2,width=canwidth,height=squar_placey,bg='#D8D5E4',borderwidth=0,highlightthickness=0)
    squarcut.place(x=50,y=50+canheight-restecuty/2)
    squarcut = Canvas(fen2,width=canwidth,height=squar_placey,bg='#D8D5E4',borderwidth=0,highlightthickness=0)
    squarcut.place(x=50,y=50-squar_placey+restecuty/2)
    print(squar_placex)
    print(squar_placey)
    print(50+canwidth-restecutx/2)
    
	
	
    fen2.mainloop()


# ----programme principal----

labeltxt = Label(fen, text="Tiles Size", bg='#D8D5E4')
labeltxt.pack()
labeltxt.place(relheight=0.1, relwidth=0.2, relx=0.68, rely=0.05)

var = IntVar()

bouton1 = Radiobutton(fen, text="20x20", variable=var, value=1, bg='#D8D5E4')
bouton1.pack()
bouton1.place(relx=0.7, rely=0.15)

bouton2 = Radiobutton(fen, text="30x30", variable=var, value=2, bg='#D8D5E4')
bouton2.pack()
bouton2.place(relx=0.7, rely=0.20)

bouton3 = Radiobutton(fen, text="20x40", variable=var, value=3, bg='#D8D5E4')
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
inputlonggT.place(relheight=0.06, relwidth=0.05, relx=0.7, rely=0.36)

inputlarggT = Entry(fen)
inputlarggT.pack()
inputlarggT.place(relheight=0.06, relwidth=0.05, relx=0.8, rely=0.36)

labeltxt1 = Label(fen, text="longueur:", bg='#D8D5E4')
labeltxt1.pack()
labeltxt1.place(relheight=0.06, relwidth=0.1, relx=0.09, rely=0.1)

labeltxt2 = Label(fen, text="largeur:", bg='#D8D5E4')
labeltxt2.pack()
labeltxt2.place(relheight=0.06, relwidth=0.1, relx=0.09, rely=0.2)

labeltxt3 = Label(fen, text="X", bg='#D8D5E4')
labeltxt3.pack()
labeltxt3.place(relheight=0.06, relwidth=0.05, relx=0.75, rely=0.36)

boutonL = Button(fen, text="Launch", command=calcul)
boutonL.pack()
boutonL.place(relheight=0.1, relwidth=0.2, relx=0.1, rely=0.3)

canvas = Canvas(fen, height=5, background='white')
canvas.place(relx=0.05, rely=0.45, relwidth=0.9)

fen.mainloop()
