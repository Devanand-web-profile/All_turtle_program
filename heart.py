import turtle
pen= turtle.Turtle()
screen=pen.getscreen()
def curve():
    for i in range (200):
        pen.right(1)
        pen.forward(1)

def heart():
    pen.fillcolor("black")
    pen.begin_fill()
    
    pen.left(140)
    pen.forward(113)
    
    curve()
    pen.left(120)
    
    curve()
    
    pen.forward(112)
    pen.end_fill()

def text():
    pen.up()
    pen.setpos(-55,50)
    pen.down()
    pen.color("red")
    pen.write("Hello heart ! ",font=("algerian",20,"bold"))   
heart()
text()
screen.exitonclick()