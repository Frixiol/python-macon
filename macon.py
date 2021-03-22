a="20x20"  
b="30x30"       #cm
c="20x40"
d=6  #kg de colle  /m²   pour a 
f=8  #idem               pour b et c 
#x=input()  #type de carreaux 
#z=input()  #taille du local  en m²

#nbrcarreaux=(z/(x/10000))



from tkinter import * # on importe tous la bibliothèque Tk

fen=Tk() #création d’une fenêtre Tk
fen.title("fenetre")
fen.geometry("500x400")
fen.configure(bg='#D8D5E4')
#insérer les widgets et les appels de fonction

def error():
	labelEr = Label(fen,text="Error",bg='#D8D5E4')
	labelEr.pack()
	labelEr.place(relheight=0.2, relwidth=0.4,relx=0.2, rely=0.5)

def calcul() :
    
    longP = inputlongP.get()
    largP = inputlargP.get()
    rad = var.get()
    if rad == 1:
        longT = largT = 0.2
    elif rad == 2:
        longT = largT = 0.3 
    elif rad == 3:
        longT = 0.2
        largT = 0.4
    else:
        error()
		
    ouver()
    #insérer votre code
    
def ouver() :
    fen2=Tk() #création d’une fenêtre Tk
    fen2.title("affiche")
    fen2.geometry("1000x800")
    
    
  
    fen2.mainloop()

#----programme principal----

labeltxt = Label(fen,text="Tiles Size",bg='#D8D5E4')
labeltxt.pack()
labeltxt.place(relheight=0.1, relwidth=0.2,relx=0.68, rely=0.05)

var = IntVar()

bouton1 = Radiobutton(fen,text = "20x20",variable=var, value=1,bg='#D8D5E4')
bouton1.pack()
bouton1.place(relx=0.7, rely=0.15)

bouton2 = Radiobutton(fen,text = "30x30",variable=var, value=2,bg='#D8D5E4')
bouton2.pack()
bouton2.place(relx=0.7, rely=0.25)

bouton3 = Radiobutton(fen,text = "20x40",variable=var, value=3,bg='#D8D5E4')
bouton3.pack()
bouton3.place(relx=0.7, rely=0.35)


inputlongP = Entry(fen)
inputlongP.pack()
inputlongP.place(relheight=0.06, relwidth=0.1,relx=0.2, rely=0.1)

inputlargP = Entry(fen)
inputlargP.pack()
inputlargP.place(relheight=0.06, relwidth=0.1,relx=0.2, rely=0.2)


labeltxt1 = Label(fen,text="longueur:",bg='#D8D5E4')
labeltxt1.pack()
labeltxt1.place(relheight=0.06, relwidth=0.1,relx=0.09, rely=0.1)

labeltxt2 = Label(fen,text="largeur:",bg='#D8D5E4')
labeltxt2.pack()
labeltxt2.place(relheight=0.06, relwidth=0.1,relx=0.09, rely=0.2)

boutonL = Button(fen,text = "Launch",command=calcul)
boutonL.pack()
boutonL.place(relheight=0.1, relwidth=0.2,relx=0.1, rely=0.3)

fen.mainloop() 
