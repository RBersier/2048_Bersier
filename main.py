"""
Module : MA-20
Titre : Jeu 2048
Autheur : Ryan Bersier
Date de dernière modification : 17.03.23
Version : 0.2
"""

#import de tkinter
from tkinter import *
import tkinter.font

#definitiom des variable
nb_move = 0
temp_col = []
nb_score = 0
file = open("data.txt")
nb_highscore = int(file.read())
file.close()

#definition des puissance de 2
power2 = [2 ** 1, 2 ** 2, 2 ** 3, 2 ** 4,
          2 ** 5, 2 ** 6, 2 ** 7, 2 ** 8,
          2 ** 9, 2 ** 10, 2 ** 11, 2 ** 12,
          2 ** 13, 2 ** 14, 2 ** 15, 2 ** 16,
          2 ** 17]

#dictionnaire des couleur pour les puissance de 2
colors = {2 ** 1 : "#FF9999", 2 ** 2 : "#FF7777", 2 ** 3 : "#FF5555", 2 ** 4 : "#FF0000",
          2 ** 5 : "#99FF99", 2 ** 6 : "#77FF77", 2 ** 7 : "#55FF55", 2 ** 8 : "#00FF00",
          2 ** 9 : "#9999FF", 2 ** 10 : "#7777FF", 2 ** 11 : "#5555FF", 2 ** 12 : "#0000FF",
          2 ** 13 : "#00FFFF", 2 ** 14 : "#FF00FF", 2 ** 15 : "#FFFF00", 2 ** 16 : "#FFFFFF",
          2 ** 17 : "#000000"}

#contenu de la grille du 2048
table2 = [[power2[0], power2[0], power2[1], power2[2]],
          [power2[6], power2[5], power2[4], power2[3]],
          [power2[7], power2[8], power2[9], power2[10]],
          [power2[14], power2[13], power2[12], power2[11]]]

#définiton du tableau du 2048
labels = [[None, None, None, None],
          [None, None, None, None],
          [None, None, None, None],
          [None, None, None, None]]

#fonction pour les touche et le déplacement des case
def key_press(event):
    global nb_move

#gauche
    if event.keysym == "a" or event.keysym == "Left" or event.keysym == "A":
        mix(False, 1)
        refresh()

#droite
    if event.keysym == "d" or event.keysym == "Right" or event.keysym == "D":
        mix(True, 1)
        refresh()

#haut
    if event.keysym == "w" or event.keysym == "Up" or event.keysym == "W":
        mix(False, 0)
        refresh()
#bas
    if event.keysym == "s" or event.keysym == "Down" or event.keysym == "S":
        mix(True, 0)
        refresh()

#fonction sur l'addition des puissance de 2 et supression du vide
def mix(rev, id):
    global nb_score, nb_move
    for col in range(len(table2)):
        for obj in range(len(table2[col])):
            if id == 0:
                if table2[obj][col] != 0:
                    temp_col.append(table2[obj][col])
            else:
                if table2[col][obj] != 0:
                    temp_col.append(table2[col][obj])
        while "" in temp_col:
            temp_col.remove("")
        for obj in range(len(temp_col) - 1):
            if temp_col[obj] == temp_col[obj + 1]:
                temp_col[obj] += temp_col[obj + 1]
                nb_score += temp_col[obj]
                temp_col[obj + 1] = ""
        while "" in temp_col:
            temp_col.remove("")
        while len(temp_col) < 4:
            if rev:
                temp_col.insert(0, "")
            else:
                temp_col.append("")
        for obj in range(len(table2[col])):
            if id == 0:
                table2[obj][col] = temp_col[obj]
            else:
                table2[col][obj] = temp_col[obj]
        temp_col.clear()
    nb_move += 1
def highscore():
    global nb_highscore
    #gestion du highscore
    if nb_score > nb_highscore:
        file = open("data.txt", "w")
        file.write(f"{nb_score}")
        file.close()

    #definition du highscore
    file = open("data.txt")
    nb_highscore = int(file.read())
    file.close()
def graphics():
    #frame de la grille
    frame1 = Frame(win, bg="grey")
    frame1.grid(row=5, column=10)

    #frame du titre
    frame2 = Frame(win, bg="grey")
    frame2.grid(row= 1, column= 10)
    labels2048 = Label(frame2, text="2048", font=("Helvetica", 48), bg="grey", fg="white")
    labels2048.grid(row= 1, column= 10)

    #frame des statistique
    frame3 = Frame(win, bg="grey")
    frame3.grid(row= 2, column= 10)

    #labels des statistique
    highscore = Label(frame3, text=f"highscore : {nb_highscore}", font=("Helvetica", 12), bg="grey", fg="white")
    highscore.grid(row= 1, column= 1)
    score = Label(frame3, text=f"score : {nb_score}", font=("Helvetica", 12), bg="grey", fg="white")
    score.grid(row= 1, column= 5, padx= 50)
    movements = Label(frame3, text=f"movements : {nb_move}", font=("Helvetica", 12), bg="grey", fg="white")
    movements.grid(row= 1, column= 10)

    #frame du bouton reset
    frame4 = Frame(win, bg="grey")
    frame4.grid(row= 10, column= 10)

    #bouton pour reset
    reset = Button(frame4, text="Restart", font=("Helvetica", 12), bg="grey", fg="white")
    reset.grid(row= 10, column= 10, pady=10)

#définition de la fenetre et ces paramètre
if __name__ == '__main__':
    # window creation :
    win = Tk()
    win.geometry("475x600")
    win.title('2048')
    win.configure(bg="grey")

#definition des paramêtre du tableau et ajout des couleur en fonction de la case
    def refresh():
        global nb_highscore
        #frame de la grille
        frame1 = Frame(win, bg="grey")
        frame1.grid(row=5, column=10)
        for line in range(len(table2)):
            for col in range(len(table2[line])):
                labels[line][col] = tkinter.Label(frame1, text=table2[line][col], width=6, height=3, borderwidth=1, relief="solid", font=("Arial", 24), bg="lightgray")
                labels[line][col].grid(row=line + 5, column=col)

                #defini les couleur
                try:
                    labels[line][col].config(bg=colors[table2[line][col]])
                    if colors[table2[line][col]] == colors[2 ** 17]:
                        labels[line][col].config(fg="white")
                except:
                    labels[line][col].config(bg="lightgray")

        #gère la partie du highscore
        highscore()

        #gère la partie graphique du logiciel
        graphics()

#permet la détection d'appuie de touche
    win.bind('<Key>', key_press)

#dernier mise à jour de la grile avant affichage
    refresh()
    graphics()

#affichage de la fenêtre
    win.mainloop()
