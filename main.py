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
        for line in range(len(table2)):
            table2[line] = Mix(table2[line], False, 0)
        refrech()
        nb += 1
        print(f"vous avez {nb} mouvements")

#droite
    if event.keysym == "d" or event.keysym == "Right" or event.keysym == "D":
        for line in range(len(table2)):
            table2[line] = Mix(table2[line], True, 0)
        refrech()
        nb += 1
        print(f"vous avez {nb} mouvements")

#haut
    if event.keysym == "w" or event.keysym == "Up" or event.keysym == "W":
        for line in range(len(table2)):
            for col in range(len(table2[line])):
                table2[line][col] = Mix(table2[line][col], False, 1)
        refrech()
        nb += 1
        print(f"vous avez {nb} mouvements")
#bas
    if event.keysym == "s" or event.keysym == "Down" or event.keysym == "S":
        for line in range(len(table2)):
            for col in range(len(table2[line])):
                table2[line][col] = Mix(table2[line][col], True, 1)
        refrech()
        nb += 1
        print(f"vous avez {nb} mouvements")

#fonction sur l'addition des puissance de 2 et supression du vide
def Mix(list, rev, id):

#tassage de gauche
        if "" in list:
            list.remove("")
        for obj in range(len(list) - 1):
            if list[obj] == list[obj + 1]:
                list[obj] += list[obj + 1]
                list[obj + 1] = ""

#tassege du haut
                """
            for row in range(len(list) - 1):
                if list[obj][row] != 0:
                    list[row][obj] += list[row + 1][obj]
                    list[row][obj] = ""
                    """
        #permet de retirer le vide
        while "" in list:
            list.remove("")

#tassage droite
        while len(list) < 4:
            if rev:
                list.insert(0, "")
            else:
                list.append("")

        return list

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
