import turtle

def add(x,y):
    print("I will add the numbers %d and %d" % (x,y))
    return x + y;

sum = add(8,5)
print('=', sum)


turtle.color('orange')

def back(len):
    turtle.penup()
    turtle.backward(len)
    turtle.pendown()

size= 100
#repeat 3 times for shape
def triangle(size):
    for i in range(3):
        turtle.forward(size)
        turtle.right(120)
def square(size):
    for i in range(4):
        turtle.forward(size)
        turtle.right(90)        
def hex(size):
    for i in range(5):
        turtle.forward(size)
        turtle.right(32)
triangle(100)
back(75)
square(150)
back(150)
hex(100)
