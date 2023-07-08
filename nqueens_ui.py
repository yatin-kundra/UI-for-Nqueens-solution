from turtle import Turtle, Screen
import  turtle as t
t.colormode(255)
turtle = Turtle()
screen = Screen()
screen.tracer(0)

node = [7, 3, 0, 2, 5, 1, 6, 4]

n = len(node)

ggrid_w = []
ggrid_b = []
queens = []

screen.setup(n*100,n*100)

screen.bgcolor((189,154,122))


def grid(n, col, g_c):
    screen.update()

    for i in range(int((n*n)/2)):
        turtle = Turtle()
        turtle.penup()
        turtle.shape("square")
        turtle.color(col)
        turtle.shapesize(3.4)
        g_c.append(turtle)



grid(n, "black",ggrid_b)
grid(n, "white",ggrid_w)



# ggrid_b[3].goto(80,80)
def posi_(node):
    screen.update()

    w_turn = 0  # false
    l = len(ggrid_w) -1
    print(l)
    m = len(ggrid_b) -1
    print(m)
    for i in range(n):
        for j in range(n):
            if (i+j)%2==0:
                ggrid_w[m].goto(70*(j-2)-90,70*(i-2)-60)
                m-=1

            else:
                ggrid_b[l].goto(70*(j-2)-90,70*(i-2)-60)
                l-=1
def queenposi(node):
    for i in range(len(node)):
        j = node[i]
        queens[i].up()
        queens[i].forward(0)
        queens[i].goto((70*(j-2)-90),70*(i-2)-60)
        # queens[i].goto(380,380)


posi_(node)
screen.tracer(1)

for i in range(n):
    turtle = Turtle()
    screen.addshape(f"queen-64.gif")
    turtle.shape(f"queen-64.gif")
    queens.append(turtle)


queenposi(node)


screen.exitonclick()
