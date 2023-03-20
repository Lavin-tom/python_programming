import turtle

def fractal_tree(t, branch_len, angle, depth):
    if depth == 0:
        return
    t.forward(branch_len)
    t.right(angle)
    fractal_tree(t, branch_len * 0.7, angle, depth - 1)
    t.left(angle * 2)
    fractal_tree(t, branch_len * 0.7, angle, depth - 1)
    t.right(angle)
    t.backward(branch_len)

# initialize turtle
t = turtle.Turtle()
t.speed('fastest')

# set starting position and angle
t.left(90)
t.penup()
t.backward(200)
t.pendown()

# draw fractal tree
depth = 8
branch_len = 120
angle = 20
fractal_tree(t, branch_len, angle, depth)

# hide turtle
t.hideturtle()
