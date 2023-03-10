# Example from JCY January 2023
# adapted by Frédérique Andolfatto January 2023

from tkinter import *
import tkinter.font
nb = 0
power2 = [2 ** 1, 2 ** 2, 2 ** 3, 2 ** 4,
          2 ** 5, 2 ** 6, 2 ** 7, 2 ** 8,
          2 ** 9, 2 ** 10, 2 ** 11, 2 ** 12,
          2 ** 13, 2 ** 14, 2 ** 15, 2 ** 16,
          2 ** 17]
colors = {2 ** 1 : "#FF9999", 2 ** 2 : "#FF7777", 2 ** 3 : "#FF5555", 2 ** 4 : "#FF0000",
          2 ** 5 : "#99FF99", 2 ** 6 : "#77FF77", 2 ** 7 : "#55FF55", 2 ** 8 : "#00FF00",
          2 ** 9 : "#9999FF", 2 ** 10 : "#7777FF", 2 ** 11 : "#5555FF", 2 ** 12 : "#0000FF",
          2 ** 13 : "#00FFFF", 2 ** 14 : "#FF00FF", 2 ** 15 : "#FFFF00", 2 ** 16 : "#FFFFFF",
          2 ** 17 : "#000000"}
table2 = [[power2[0], power2[0], power2[1], power2[2]],
          [power2[4], power2[4], power2[5], power2[6]],
          [power2[8], power2[8], power2[9], power2[10]],
          [power2[12], power2[12], power2[13], power2[14]]]
labels = [[None, None, None, None],
          [None, None, None, None],
          [None, None, None, None],
          [None, None, None, None]]

def key_press(event):
    global nb
    if event.keysym == "a" or event.keysym == "Left" or event.keysym == "A":
        for line in range(len(table2)):
            table2[line] = Mix(table2[line], False, 0)
        refrech()
        nb += 1
        print(f"vous avez {nb} mouvements")
    if event.keysym == "d" or event.keysym == "Right" or event.keysym == "D":
        for line in range(len(table2)):
            table2[line] = Mix(table2[line], True, 0)
        refrech()
        nb += 1
        print(f"vous avez {nb} mouvements")
    if event.keysym == "w" or event.keysym == "Up" or event.keysym == "W":
        for line in range(len(table2)):
            for col in range(len(table2[line])):
                table2[line][col] = Mix(table2[line][col], False, 1)
        refrech()
        nb += 1
        print(f"vous avez {nb} mouvements")


def Mix(list, rev, id):
        if "" in list:
            list.remove("")
        for obj in range(len(list) - 1):
            """
             for row in range(len(list[obj]) - 1):
                if list[obj][row] != 0:
                    list[row][obj] += list[row + 1][obj]
                    list[row][obj] = ""
                if list[obj][row] == 0: 
            """
            if list[obj] == list[obj + 1]:
                list[obj] += list[obj + 1]
                list[obj + 1] = ""
        while "" in list:
            list.remove("")
        while len(list) < 4:
            if rev:
                list.insert(0, "")
            else:
                list.append("")

        return list

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # window creation :
    win = Tk()
    win.geometry("500x500")
    win.title('2048')
    win.configure(bg="grey")

    # label creation, we set them with = and then we set them inside the window with .grid(row,column)
    def refrech():
        for line in range(len(table2)):
            for col in range(len(table2[line])):
                # creation of each label without placing it
                labels[line][col] = tkinter.Label(text=table2[line][col], width=6, height=3, borderwidth=1, relief="solid",
                                                  font=("Arial", 24), bg="lightgray")
                # we set the label in the windows with a virtual grid
                labels[line][col].grid(row=line, column=col)

                try:
                    labels[line][col].config(bg=colors[table2[line][col]])
                    if colors[table2[line][col]] == colors[2 ** 17]:
                        labels[line][col].config(fg="white")
                except:
                    labels[line][col].config(bg="lightgray")

    win.bind('<Key>', key_press)
    refrech()
    win.mainloop()
