visited_block = []
hah = 0

from turtle import Turtle, Screen
import  turtle as t
t.colormode(255)
turtle = Turtle()
screen = Screen()
screen.tracer(0)




def nqueens(n):
    board = [-1] * n  # initialize the board with no queens
    solutions = []  # initialize the list of solutions
    solve_nqueens(n, 0, board, solutions)  # start solving the problem
    return solutions

def solve_nqueens(n, row, board, solutions):
    if row == n:  # base case: all queens have been placed on the board
        solutions.append(board.copy())  # add the solution to the list of solutions
    else:
        for i in range(n):  # try all possible columns for the current row
            if is_valid(row, i, board):  # check if the current position is valid
                board[row] = i  # place the queen on the board
                solve_nqueens(n, row + 1, board, solutions)  # recursively solve for the next row
                board[row] = -1  # backtrack: remove the queen from the board

def is_valid(row, col, board):
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True







###############         UI          ######################
Queens =  int(screen.textinput(title="N Queens", prompt="Enter the number of Queens: "))


ans = nqueens(Queens)


n = len(ans[1])

ggrid_w = []
ggrid_b = []
queens = []

if n ==4:
    screen.setup(n*130, n*130)
else:
    screen.setup(n*100,n*100)

screen.bgcolor((189,154,122))


def grid(n, col, g_c):
    screen.update()

    for i in range(int((n*n)/2)):
        turtle = Turtle()
        turtle.penup()
        turtle.speed("fastest")
        turtle.shape("square")
        turtle.color(col)
        turtle.shapesize(3.4)
        g_c.append(turtle)



grid(n, "black",ggrid_b)
grid(n, "white",ggrid_w)



# ggrid_b[3].goto(80,80)
def posi_():
    screen.update()

    w_turn = 0  # false
    l = len(ggrid_w) -1
    m = len(ggrid_b) -1

    for i in range(n):
        for j in range(n):
            if (i+j)%2==0:
                ggrid_w[m].goto(70*(j-2)-70,70*(i-2)-60)
                m-=1

            else:
                ggrid_b[l].goto(70*(j-2)-70,70*(i-2)-60)
                l-=1
def queenposi(node):
    for i in range(len(node)):
        j = node[i]
        queens[i].speed("fastest")
        queens[i].up()
        queens[i].forward(0)
        queens[i].goto((70*(j-2)-70),70*(i-2)-60)
        # queens[i].goto(380,380)

tt = Turtle()
tt.shape()
tt.shape("square")
tt.color("white")
tt.shapesize(3.4)
tt.goto(70*(0-2)-70,70*(0-2)-60)


posi_()
screen.tracer(1)

for i in range(n):
    turtle = Turtle()
    screen.addshape(f"queen-64.gif")
    turtle.shape(f"queen-64.gif")
    queens.append(turtle)







for i in range(len(ans)-1):
    queenposi(ans[i])


screen.exitonclick()


