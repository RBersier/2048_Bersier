"""
Module : MA-20
Titre : Jeu 2048
Autheur : Ryan Bersier
Date de dernière modification : 04.04.23
Version : 1.0
"""

# import des différentes bibliothèque
from tkinter import *
from tkinter import messagebox
import tkinter.font
import random

# definitiom des variable
nb_move = 0
temp_col = []
nb_score = 0
file = open("data.txt")
nb_highscore = int(file.read())
file.close()
w = 0

# definition des puissances de 2
power2 = [2 ** 1, 2 ** 2, 2 ** 3, 2 ** 4,
          2 ** 5, 2 ** 6, 2 ** 7, 2 ** 8,
          2 ** 9, 2 ** 10, 2 ** 11, 2 ** 12,
          2 ** 13, 2 ** 14, 2 ** 15, 2 ** 16,
          2 ** 17]

# dictionnaire des couleurs pour les puissances de 2
colors = {2 ** 1: "#FF9999", 2 ** 2: "#FF7777", 2 ** 3: "#FF5555", 2 ** 4: "#FF0000",
          2 ** 5: "#99FF99", 2 ** 6: "#77FF77", 2 ** 7: "#55FF55", 2 ** 8: "#00FF00",
          2 ** 9: "#9999FF", 2 ** 10: "#7777FF", 2 ** 11: "#5555FF", 2 ** 12: "#0000FF",
          2 ** 13: "#00FFFF", 2 ** 14: "#FF00FF", 2 ** 15: "#FFFF00", 2 ** 16: "#FFFFFF",
          2 ** 17: "#000000"}

# contenu de la grille du 2048
table2 = [["", "", "", ""],
          ["", "", "", ""],
          ["", "", "", ""],
          ["", "", "", ""]]

# définiton du tableau du 2048
labels = [[None, None, None, None],
          [None, None, None, None],
          [None, None, None, None],
          [None, None, None, None]]


# fonction pour les touches et le déplacement des cases
def key_press(event):
    global nb_move

    # gauche
    if event.keysym == "a" or event.keysym == "Left" or event.keysym == "A":
        mix(False, 1)

    # droite
    if event.keysym == "d" or event.keysym == "Right" or event.keysym == "D":
        mix(True, 1)

    # haut
    if event.keysym == "w" or event.keysym == "Up" or event.keysym == "W":
        mix(False, 0)

    # bas
    if event.keysym == "s" or event.keysym == "Down" or event.keysym == "S":
        mix(True, 0)


# check les mouvements disponible pour la grille
def movement_checker():
    for row in range(len(table2)):
        for col in range(len(table2[row])):
            # verifie dans chaque case s'il y en a une vide
            if table2[row][col] == "":
                return True
            # verfie après mixage en ligne
            if row < 4 - 1 and table2[row][col] == table2[row + 1][col]:
                return True
            # verifie après mixage en colonne
            if col < 4 - 1 and table2[row][col] == table2[row][col + 1]:
                return True
    return False


# Cette fonction mélange les cases d'une grille de jeu 2048
def mix(rev, id):
    global nb_score, nb_move
    # prev_positions_value stocke la valeur actuelle de 'table2', avant tout mélange, pour détecter un changement ultérieur.
    prev_positions_value = [row[:] for row in table2]
    # Pour chaque colonne ou ligne du tableau, on parcourt les objets et les colonnes/lignes en fonction de 'id'
    for col in range(len(table2)):
        for obj in range(len(table2[col])):
            # Si id est 0, on travaille avec des colonnes.
            if id == 0:
                # On ajoute l'élément à la liste temporaire s'il est différent de 0.
                if table2[obj][col] != 0:
                    temp_col.append(table2[obj][col])
            # Si id est différent de 0, on travaille avec des lignes.
            else:
                # On ajoute l'élément à la liste temporaire s'il est différent de 0.
                if table2[col][obj] != 0:
                    temp_col.append(table2[col][obj])
        # On enlève les éléments vides de la liste temporaire.
        while "" in temp_col:
            temp_col.remove("")
        # On fusionne les éléments identiques qui sont côte à côte dans la liste temporaire.
        for obj in range(len(temp_col) - 1):
            if temp_col[obj] == temp_col[obj + 1]:
                temp_col[obj] += temp_col[obj + 1]
                # On met à jour le score en ajoutant la valeur fusionnée.
                nb_score += temp_col[obj]
                temp_col[obj + 1] = ""
        # On enlève les éléments vides de la liste temporaire.
        while "" in temp_col:
            temp_col.remove("")
        # On ajoute des éléments vides à la liste temporaire jusqu'à ce qu'elle atteigne une longueur de 4.
        while len(temp_col) < 4:
            if rev:
                # Si 'rev' est vrai, on ajoute l'élément vide au début de la liste.
                temp_col.insert(0, "")
            else:
                # Sinon, on ajoute l'élément vide à la fin de la liste.
                temp_col.append("")
        # On ajoute les éléments de la liste temporaire à la colonne ou à la ligne correspondante dans 'table2'.
        for obj in range(len(table2[col])):
            if id == 0:
                table2[obj][col] = temp_col[obj]
            else:
                table2[col][obj] = temp_col[obj]
         # On vide la liste temporaire pour la prochaine colonne ou ligne.
        temp_col.clear()
    # Si le tableau 'table2' a changé, cela signifie qu'un mouvement a été effectué.
    if table2 != prev_positions_value:
        # On incrémente le nombre de mouvements effectués.
        nb_move += 1
        random_nb()
    refresh()
    win_game()
    lose_game()


# fonction de calcul du highscore
def highscore():
    global nb_highscore
    # verifie si le score est supèrieur au highscore
    if nb_score > nb_highscore:
        # ouvre le fichier data contenant le highscore et enregistre le nouveau score
        file = open("data.txt", "w")
        file.write(f"{nb_score}")
        file.close()

    # definition du highscore
    file = open("data.txt")
    nb_highscore = int(file.read())
    file.close()


# actualise les diférente stat présente sur la partie graphique pendant la partie
def refresh_graphics():
    global score_label, highscore_label, movements_label, nb_score, nb_move, nb_highscore

    score_label.config(text=f"score : {nb_score}")
    movements_label.config(text=f"movements : {nb_move}")
    highscore_label.config(text=f"highscore : {nb_highscore}")


# gère l'appariton de 2 et de 4
def random_nb():
    # definition d'une variable pour que si aucune case n'est disponible qu'il ne tente pas d'en regenerer des 2 ou 4
    i = 0
    if movement_checker():
        # definition d'une variable pour avoir 10% de chance qu'un 4 se gènère
        x = random.randint(0, 9)
        while True:
            # choisie une case aléatoire parmis les 16
            y = random.randint(0, 3)
            z = random.randint(0, 3)
            # verifie qu'il y est une case vide sur la grille
            for line in range(len(table2)):
                for col in range(len(table2[line])):
                    if table2[line][col] == "":
                        i += 1
            # si pas de case casse la boucle
            if i == 0:
                break
            else:
                # verifie que la case séléctionner est vide
                if table2[y][z] == "":
                    # ajout de 4
                    if x == 0:
                        table2[y][z] = power2[1]
                        break
                    # ajout de 2
                    else:
                        table2[y][z] = power2[0]
                        break
    refresh()


# pour les démmarage
def start_game():
    # si la grille est vide génére 2 nombre sur la grille
    if table2 == [["", "", "", ""], ["", "", "", ""], ["", "", "", ""], ["", "", "", ""]]:
        random_nb()
        random_nb()


# gère le restart du jeu
def reset_game(window=None):
    global nb_score, table2, nb_move, frame3, score_label, movements_label
    # redéfinission des variable stat à 0 (sauf highscore)
    nb_score = 0
    nb_move = 0
    # vide la variable contenant la grille et la rédéfini avec rien dedans
    table2.clear()
    table2 = [["", "", "", ""],
              ["", "", "", ""],
              ["", "", "", ""],
              ["", "", "", ""]]
    refresh()
    # pour la partie gagner detruit la fenêtre parallèle pour si le joueur choisie de recommencer une partie
    if window != None:
        win_win_game.destroy()
    score_label.config(text=f"score : {nb_score}")
    movements_label.config(text=f"movements : {nb_move}")

    start_game()


# fonction pour gagner la partie
def win_game():
    global w, win_win_game
    # definition de la variable gagné a faux tant que pas de 2048
    won = False
    # verifie sur toutes les cases la présence d'une case 2048 si oui passe la variable gagné à vrai
    for line in range(len(table2)):
        for col in range(len(table2[line])):
            if table2[col][line] == power2[10] and w == 0:
                won = True
    # si gagné créer une fenêtre au-dessus de la prmemière
    if won:
        win_win_game = Toplevel(win)
        win_win_game.geometry("800x150")
        win_win_game.title('gagner')
        win_win_game.configure(bg="grey")

        # frame du texte
        frame5 = Frame(win_win_game, bg="grey")
        frame5.pack()
        labels_win = Label(frame5, text="Congratulations you won!!!", font=("Helvetica", 24), bg="grey", fg="white")
        labels_win.pack()
        labels_ask = Label(frame5,
                           text="Now you have the choice to continue your game to go further than 2048, restart a game or leave the program",
                           font=("Helvetica", 12), bg="grey", fg="white")
        labels_ask.pack()

        # frame des 3 boutons
        frame6 = Frame(win_win_game, bg="grey")
        frame6.pack(pady=30)
        # bouton pour continuer la partie
        continue_win = Button(frame6, text="Continue", font=("Helvetica", 12), bg="grey", fg="white",
                              command=win_win_game.destroy)
        continue_win.pack(side=LEFT)
        # bouton pour recommencer une partie
        reset_win = Button(frame6, text="Restart", font=("Helvetica", 12), bg="grey", fg="white",
                           command=lambda: reset_game(win_win_game))
        reset_win.pack(side=LEFT, padx=50)
        # bouton pour quitter le jeu
        quit_win = Button(frame6, text="Leave", font=("Helvetica", 12), bg="grey", fg="white",
                          command=win_win_game.destroy and win.destroy)
        quit_win.pack(side=LEFT)

        # win que 1 seule fois par partie
        w += 1


# fonction pour la partie perdu
def lose_game():
    # racourci pour la fonction mouvement checker
    mc = movement_checker()
    # verifie si plus aucun mouvement disponible
    if not mc:
        # pose la question au joueur s'il veut rejouer ou quitter le jeu
        answer = messagebox.askquestion("Lose", "You lose, you want to retry for reaching 2048 ?")
        if answer == "yes":
            reset_game()
        elif answer == "no":
            win.destroy()


# définition de la fenêtre et ces paramètres
if __name__ == '__main__':
    # window creation :
    win = Tk()
    win.geometry("475x600")
    win.title('2048')
    win.configure(bg="grey")
    # frame de la grille
    frame1 = Frame(win, bg="grey")
    frame1.grid(row=5, column=10)
    # frame du titre
    frame2 = Frame(win, bg="grey")
    frame2.grid(row=1, column=10)
    labels2048 = Label(frame2, text="2048", font=("Helvetica", 48), bg="grey", fg="white")
    labels2048.grid(row=1, column=10)
    # frame des statistiques
    frame3 = Frame(win, bg="grey")
    frame3.grid(row=2, column=10)
    # labels des statistiques
    highscore_label = Label(frame3, text=f"highscore : {nb_highscore}", font=("Helvetica", 12), bg="grey", fg="white")
    highscore_label.grid(row=1, column=1)
    score_label = Label(frame3, text=f"score : {nb_score}", font=("Helvetica", 12), bg="grey", fg="white")
    score_label.grid(row=1, column=5, padx=50)
    movements_label = Label(frame3, text=f"movements : {nb_move}", font=("Helvetica", 12), bg="grey", fg="white")
    movements_label.grid(row=1, column=10)
    # frame du bouton reset
    frame4 = Frame(win, bg="grey")
    frame4.grid(row=10, column=10)
    # bouton pour reset
    reset = Button(frame4, text="Restart", font=("Helvetica", 12), bg="grey", fg="white", command=reset_game)
    reset.grid(row=10, column=10, pady=10)


    # definition des paramètres du tableau et ajout des couleurs en fonction de la case
    def refresh():
        global nb_highscore
        # frame de la grille
        frame1 = Frame(win, bg="grey")
        frame1.grid(row=5, column=10)
        # ajoute un label dans chaques case
        for line in range(len(table2)):
            for col in range(len(table2[line])):
                labels[line][col] = tkinter.Label(frame1, text=table2[line][col], width=6, height=3, borderwidth=1,
                                                  relief="solid", font=("Arial", 24), bg="lightgray")
                # definition d'un décalage de la grille pour laisser un peu de place à la parti graphique
                labels[line][col].grid(row=line + 5, column=col)

                # défini les couleurs
                try:
                    labels[line][col].config(bg=colors[table2[line][col]])
                    if colors[table2[line][col]] == colors[2 ** 17]:
                        labels[line][col].config(fg="white")
                except:
                    labels[line][col].config(bg="lightgray")

        # gère la partie du highscore
        highscore()

        # gère la partie graphique du logiciel
        refresh_graphics()


    # permet la détection d'appui de touche
    win.bind('<Key>', key_press)
    # dernier mise à jour de la grile avant affichage
    refresh()
    start_game()
    # affichage de la fenêtre
    win.mainloop()
