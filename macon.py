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
#insérer les widgets et les appels de fonction

def info() :
  long=input()
  larg=input()



def calcul() :
    surface=(long*larg)
    
    ouver()
    #insérer votre code
    
def ouver() :
    fen2=Tk() #création d’une fenêtre Tk
    fen2.title("affiche")
    fen2.geometry("1000x800")
    label = Label(fen, text="surface=...", bg="yellow")
    label.place(x=10,y=10)
  
    fen2.mainloop()

#----programme principal----
bouton1 = Button(fen,text = "20x20",command=calcul)
bouton1.pack()
bouton1.place(relheight=0.1, relwidth=0.2,relx=0.1, rely=0.05)

bouton2 = Button(fen,text = "30x30",command=calcul)
bouton2.pack()
bouton2.place(relheight=0.1, relwidth=0.2,relx=0.4, rely=0.05)

bouton3 = Button(fen,text = "20x40",command=calcul)
bouton3.pack()
bouton3.place(relheight=0.1, relwidth=0.2,relx=0.7, rely=0.05)

fen.mainloop() 
