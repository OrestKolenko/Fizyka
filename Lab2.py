from tkinter import *
from turtle import *
import math, random




def draw_grid():
    #X line
    up() 
    goto(-200, 0)
    down()
    forward(400)
    #X arrow
    begin_fill()
    right(90)
    forward(3)
    left(120)
    forward(6)
    left(120)
    forward(6)
    left(120)
    forward(3)
    end_fill()
    #T text
    up()
    goto(203, 6)
    down()
    write('t')
    #Y line
    up()
    goto(-200, -200)
    down()
    left(180)
    forward(400)
    #Y arrow
    begin_fill()
    right(90)
    forward(3)
    left(120)
    forward(6)
    left(120)
    forward(6)
    left(120)
    forward(3)
    end_fill()
    #U text
    up()
    goto(-202, 210)
    down()
    write('U')



def initiation():
    B_Label.grid(row=0, column=0)
    B_Entry.grid(row=0, column=1)

    S_Label.grid(row=1, column=0)
    S_Entry.grid(row=1, column=1)

    w_Label.grid(row=2, column=0)
    w_Entry.grid(row=2, column=1)

    submit_Button.grid(row=3, column=0, columnspan=2)

    draw_grid()



def submit():
    B = float(B_Entry.get())
    S = float(S_Entry.get())
    w = float(w_Entry.get())
    draw(B, S, w)



def draw(B, S, w):
    global colors, count, T_init, B_init, S_init, w_init
    T = 2*math.pi/w
    if count == 1:
        T_init = T
        B_init = B
        S_init = S
        w_init = w
    #Color of the wave
    picked_color = random.choice(colors)
    colors.remove(picked_color)
    pencolor(picked_color)
    #Sinusoidal wave
    height= 100*(B*S*w)/(B_init*S_init*w_init)
    num_of_curves = 6*(T_init/T) 
    up()
    goto(-200, 0)
    down()
    for x in range(-200, 200):
        y = height * math.sin((x * math.pi) / (400/num_of_curves))  
        goto(x, y)
    #BSw text
    up()
    goto(-280, height-5)
    down()
    write(f'BSw = {round(B*S*w, 5)}')
    #BSw dotted line
    up()
    goto(-200, height)
    i=0
    while i <= 40:
        i+=1
        down()
        goto(i*10-200, height)
        i+=1
        up()
        goto(i*10-200, height)
    #-BSw text
    up()
    goto(-280, -height-5)
    down()
    write(f'-BSw = {round(-B*S*w, 5)}')
    #-BSw dotted line
    up()
    goto(-200, -height)
    i=0
    while i <= 40:
        i+=1
        down()
        goto(i*10-200, -height)
        i+=1
        up()
        goto(i*10-200, -height)
    count -= 2
    #T dotted line
    up()
    goto(-200+(400/num_of_curves), -200)
    i = 0
    while i<40:
        i+=1
        down()
        goto(-200+(400/num_of_curves), -200+i*10)
        i+=1
        up()
        goto(-200+(400/num_of_curves), -200+i*10)
    #T text 
    up()
    goto(-200+(400/num_of_curves), 205)
    down()
    write(f"T = {round(T, 2)}")

colors = ['red', 'blue', 'green']
count=1

window = Tk()

init_Button = Button(text="Start", font=("Arial", 15), command=initiation)
init_Button.grid(row=3, column=0, columnspan=2)

B_Label = Label(text="Input B:", font=("Arial", 15))
B_Entry = Entry(text="B_Entry", font=("Arial", 15))


S_Label = Label(text="Input S:", font=("Arial", 15))
S_Entry = Entry(text="S_Entry", font=("Arial", 15))

w_Label = Label(text="Input w:", font=("Arial", 15))
w_Entry = Entry(text="w_entry", font=("Arial", 15))

submit_Button = Button(text="Submit", command=submit, font=("Arial", 15))





window.mainloop()