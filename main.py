#import upgrader
from tkinter import *
from PIL import ImageTk
from PIL import Image
levels = [0,0,0]

window = Tk()
money = 10000
def open_upgrade_menu():
    upg_menu = Frame(window,width=400,height=400,bg="red")
    upg_menu.pack()
    upg_menu.place(relx=0.1,rely=0.1)

    close_button = Button(upg_menu,width=10,bg="blue",command=upg_menu.destroy)
    close_button.pack()
    close_button.place(anchor="center",relx=0.5,rely=0.9)
def main():

    window.title("Boss Fighting Game")
    window.geometry("500x500")


    img = ImageTk.PhotoImage(Image.open("./images/image.png"))

    frame = Frame(window, width=400, height=400)
    frame.pack()
    frame.place(anchor='center', relx=0.5, rely=0.5)

    label = Label(frame, image = img)
    label.pack()

    button = Button(window,text="Upgrades",command=open_upgrade_menu,width=10)
    button.pack()
    button.place(anchor="center",relx=0.5,rely=0.9)

    window.mainloop()


main()
"""
import pygame



pygame.init()

screen = pygame.display.set_mode((500,500))

pygame.display.set_caption("Boss Fighting Game")

running = True
while running:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False
    screen.blit(pygame.image.load("./images/image14.png"),(250,250))
    pygame.display.flip()  

"""