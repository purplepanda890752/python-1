import turtle
a = turtle.Screen()
a.bgcolor("light,blue")
a.title("Turtle")
pena=turtle.Turtle()
size = 0
while True:
    for i in range(4):
    pena.fd(size+1)
    pena.left(90)
    size = size - 5
    size = size + 1