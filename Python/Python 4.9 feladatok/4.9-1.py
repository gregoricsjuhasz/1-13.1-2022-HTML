import turtle

def negyzetek (t, h):

    for i in range(5):

        t.pendown()
        t.forward(20)
        t.left(90)
        t.forward(20)
        t.left(90)
        t.forward(20)
        t.left(90)
        t.forward(20)
        t.left(90)
        t.penup()
        t.forward(35)
        t.penup()
        


a = turtle.Screen()
a.bgcolor("lightgreen")
a.title("Sanyi találkozik egy függvénnyel")

Sanyi = turtle.Turtle()
Sanyi.pensize(4)
Sanyi.color("pink")
negyzetek (Sanyi, 20)

a.mainloop()  