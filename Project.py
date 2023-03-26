'''from tkinter import *

def click():
    list.append(entry.get())
    label.config(text = entry.get())

window = Tk()
window.title('MyProj')
window.geometry('600x400')

label=Label(
    window,
    text = 'Это работает',
    bg = 'cyan',
    font={'consolas', 15},
    underline=2,
    height = 2,
    width = 10
    )
label.pack()

entry = Entry()
entry.pack()

button = Button(
    window,
    text = 'Click'
    background = 'pink'
    font={'consolas', 15},
    height = 2,
    wigth = 10,
    activebackground = 'yellow2',
    command= click
)
button.pack

window.mainloop()






def plus(a, b):
    res = a + b
    return res


s = plus(54, 57)

print(s)'''



'''from tkinter import *

def change():
    canvas.itemconfig(square, fill='blue')
    canvas.config(bg='green')

root=Tk()


canvas=Canvas(root, width=400, height=300, bg='white')
canvas.pack()


square = canvas.create_rectangle(15, 15, 190, 110)


Button(text = 'Click', command = change).pack()

root.mainloop()'''






'''from tkinter import *

def house():
    canvas.itemconfig(square, fill = 'red')
 
def up():
    canvas.itemconfig(triegle, fill = 'yellow')

def sun():
    canvas.itemconfig(sun, fill='blue')

root=Tk()

canvas = Canvas(root, width=400, height=600, bg='white')
canvas.pack()

square = canvas.create_rectangle(80, 260, 320, 500, fill='red', outline='red')

triegle = canvas.create_polygon(80, 260, 200, 140, 320, 260, fill='grey', outline='grey')

sun = canvas.create_oval(350, 0, 400, 50, fill='yellow', outline='yellow')

Button(text='Дом', command=house).pack
Button(text = 'Крыша', command=up).pack
Button(text = 'Солнце', command = sun).pack

root.mainloop()'''



'''from tkinter import*
from random import*


def fight():
    canvas.delete('all')
    figure = randint(0, 2)

    x = randint(0, 400)
    y = randint(0, 400)
    a = randint(0, 400)
    b = randint(0, 400)

    color = ['blue', 'red', 'yellow', 'orange', 'pink', 'purple']

    if figure == 0:
        square=canvas.create_rectangle(x, y, a, b, fill = choice(color))
    elif figure == 1:
        oval=canvas.create_oval(x, y, a, b, fill = choice(color))
    elif figure == 2:
        polygon=canvas.create_polygon(x, y, a, b, x, b, fill = choice(color))

root = Tk()

canvas=Canvas(root, width=400, height=400, bg = "white")
canvas.pack()

Button(text='Нажать', command = fight).pack()


root.mainloop()'''






'''from tkinter import *
from random import *


a = []

def change():
    for i in range(N):
        a.append([randint(50, 350), randint(50, 350)])
    for i in range(N):
        if i != N - 1:
            canvas.create_line(a[i][0], a[i][1], a[i+1][0], a[1+i][1])

root=Tk()
root.title("Хуйня")

canvas=Canvas(root, width=400, height = 600, bg='white')
canvas.pack()

N = Entry()
N.pack()

b = Button(text = 'Ввод', command=change)
b.pack()


root.mainloop()'''







'''from tkinter import *

window = Tk()
window.geometry('600x400')
window.resizable(True, False)

button = Button(
    text = 'click',
    bg = 'yellow'
)
button.place(
    relx = 0.5,
    rely = 0.5,
    anchor=CENTER,
    width = 80,
    height = 50
)

window.mainloop()'''



'''s = '31798713'

print(s[0:-1:1])'''







'''import csv

lines = {
    ['Alexander Melnikov', '31', 'm'],
    ['Mihail Tolstoy', '28', 'm'],
}

with open('data.csv', 'w', newline='') as f:
    crs = csv.writer(f)
    crs.writerows(lines)

with open('data.csv', 'r') as f:
    crs = csv.reader(f)
    for i in crs:
        print(i)'''




