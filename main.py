"""
Module : MA-20
Titre : Jeu 2048
Autheur : Ryan Bersier
Date de dernière modification : 10.03.23
"""

#import de tkinter
from tkinter import *
import tkinter.font

#definitiom des variable
nb = 0
temp_col = []

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
          [power2[4], power2[4], power2[5], power2[6]],
          [power2[8], power2[8], power2[9], power2[10]],
          ["", "", "", ""]]

#définiton du tableau du 2048
labels = [[None, None, None, None],
          [None, None, None, None],
          [None, None, None, None],
          [None, None, None, None]]

#fonction pour les touche et le déplacement des case
def key_press(event):
    global nb

#gauche
    if event.keysym == "a" or event.keysym == "Left" or event.keysym == "A":
        Mix(False, 1)
        refrech()
        nb += 1
        print(f"vous avez {nb} mouvements")

#droite
    if event.keysym == "d" or event.keysym == "Right" or event.keysym == "D":
        Mix(True, 1)
        refrech()
        nb += 1
        print(f"vous avez {nb} mouvements")

#haut
    if event.keysym == "w" or event.keysym == "Up" or event.keysym == "W":
        Mix(False, 0)
        refrech()
        nb += 1
        print(f"vous avez {nb} mouvements")
#bas
    if event.keysym == "s" or event.keysym == "Down" or event.keysym == "S":
        Mix(True, 0)
        refrech()
        nb += 1
        print(f"vous avez {nb} mouvements")

#fonction sur l'addition des puissance de 2 et supression du vide
def Mix(rev, id):
    for col in range(len(table2)):
        for obj in range(len(table2[col])):
            if id == 0:
                if table2[obj][col] != 0:
                    temp_col.append(table2[obj][col])
            else:
                if table2[col][obj] != 0:
                    temp_col.append(table2[col][obj])
        if "" in temp_col:
            temp_col.remove("")
        for obj in range(len(temp_col) - 1 ):
            if temp_col[obj] == temp_col[obj + 1]:
                temp_col[obj] += temp_col[obj + 1]
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

#définition de la fenetre et ces paramètre
if __name__ == '__main__':
    # window creation :
    win = Tk()
    win.geometry("500x500")
    win.title('2048')
    win.configure(bg="grey")

#definition des paramêtre du tableau et ajout des couleur en fonction de la case
    def refrech():
        for line in range(len(table2)):
            for col in range(len(table2[line])):
                labels[line][col] = tkinter.Label(text=table2[line][col], width=6, height=3, borderwidth=1, relief="solid", font=("Arial", 24), bg="lightgray")
                labels[line][col].grid(row=line, column=col)
                #defini les couleur
                try:
                    labels[line][col].config(bg=colors[table2[line][col]])
                    if colors[table2[line][col]] == colors[2 ** 17]:
                        labels[line][col].config(fg="white")
                except:
                    labels[line][col].config(bg="lightgray")
#permet la détection d'appuie de touche
    win.bind('<Key>', key_press)
#dernier mise à jour de la grile avant affichage
    refrech()
#affichage de la fenêtre
    win.mainloop()
