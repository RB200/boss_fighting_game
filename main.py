from tkinter import *
from PIL import ImageTk
from PIL import Image
import random

levels = [0,0,0]
upg_menu_opened = False
window = Tk()
money = 10000
def open_upgrade_menu():
    global upg_menu_opened
    global upg_menu
    global stat_1_text
    if not upg_menu_opened:
        upg_menu = Frame(window,width=400,height=400,bg="#ff9782")
        upg_menu.pack()
        upg_menu.place(relx=0.1,rely=0.1)

        close_button = Button(upg_menu,width=10,bg="#69bbff",text="Close menu",command=close_upgrade_menu)
        close_button.place(anchor="center",relx=0.5,rely=0.9)

        stat_1_container = Frame(upg_menu,width=150,height=150,bg="#d46757")
        stat_1_container.pack()
        stat_1_container.place(relx=0.1,rely=0.1)

        txt = StringVar()
        txt.set(str(levels[0]))

        stat_1_text = Label(stat_1_container,text=f"{levels[0]}",bg="#d46757")
        stat_1_text.pack()
        stat_1_text.place(anchor="center",relx=0.5,rely=0.2)
        stat_1 = Button(stat_1_container,width=16,bg="#69bbff",text="Upgrade Stat 1",command=lambda: upg_wrapper(stat_1_text,1))

        stat_1.place(anchor="center",relx=0.5,rely=0.6) 
        upg_menu_opened = True
    else:
        pass

def close_upgrade_menu():
    global upg_menu_opened
    global upg_menu
    upg_menu.destroy()
    upg_menu_opened = False

def upg_wrapper(txt,level):
    global stat_1_text
    upgrade(level)

    stat_1_text.update_idletasks()
    stat_1_text.configure(text=str(levels[level-1]))

    
def upgrade(level):
    if level > 0:
        levels[level-1] += 1
    
    print(levels[level-1])
    
    #global money
    #if money - cost_to_upgrade(levels[level-1]) >= 0: 
    #    levels[level-1] += 1
    #    money -= cost_to_upgrade(levels[level-1]) 
    #    print(money)     
    #else:
    #    print("Not enough money")

#def cost_to_upgrade(level):
#    return level * 1.25
#
#while True:
#    response = input("upgrade? :")
#    if response == "1":
#        upgrade(int(response))

def open_inventory():
    pass

def main():

    window.title("Boss Fighting Game")
    window.geometry("500x500")


    img = ImageTk.PhotoImage(Image.open("./images/image.png"))

    frame = Frame(window, width=400, height=400)
    frame.pack()
    frame.place(anchor='center', relx=0.5, rely=0.5)

    label = Label(frame, image = img)
    label.pack()

    upg_button = Button(window,text="Upgrades",command=open_upgrade_menu,width=10,bg="#69bbff")
    upg_button.pack()
    upg_button.place(anchor="center",relx=0.5,rely=0.95)

    inv_button = Button(window,text="Inventory",command=open_inventory,width=10,bg="#69bbff")
    inv_button.pack()
    inv_button.place(anchor="center",relx=0.3,rely=0.95)
    window.mainloop()


main()
