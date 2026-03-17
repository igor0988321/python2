import turtle as t

def moveTurtle(x, y):
    pen.goto(x, y)


pen = t.Pen()
screen = t.Screen()

pen.pensize(10)
pen.color('red')
# pen.forward(100)

screen.onscreenclick(moveTurtle)

t.mainloop()