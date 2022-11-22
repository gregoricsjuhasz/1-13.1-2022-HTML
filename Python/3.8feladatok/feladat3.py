import turtle
ablak = turtle.Screen()
ablak.bgcolor("#90EE90")
Pista = turtle.Pen()
Pista.shape("turtle")
Pista.color("blue")
Pista.stamp
move=30
for i in range(12):
    Pista.penup()
    Pista.forward(50)
    Pista.pendown()
    Pista.forward(25)
    Pista.penup()
    Pista.forward(15)
    Pista.stamp()
    Pista.home()
    Pista.right(move)
    move = move + 30
