
import turtle
t= turtle.Turtle()
s=int(input("Enter the Length of Square :"))
col="blue"

t.fillcolor(col)
t.begin_fill()
for _ in range(4):
    t.forward(s)
    t.right(144)

t.end_fill()