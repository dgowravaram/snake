import turtle
import time

delay = 0.1

#set up screen
wn = turtle.Screen()
wn.title("Snake")
wn.bgcolor("black")
wn.setup(width=600,height=600)
wn.tracer(0) # turns off screen updates

# snake head
head = turtle.Turtle()
head.speed(0) #fastest animation speed
head.shape("square")
head.color("red")
head.penup()
head.goto(0,0)
head.direction="stop"

def go_up():
    head.direction = "up"

def go_down():
    head.direction = "down"

def go_left():
    head.direction = "left"

def go_right():
    head.direction = "right"

def move():
    if head.direction=="up":
        y = head.ycor()
        head.sety(y+20)
    if head.direction=="down":
        y = head.ycor()
        head.sety(y-20)
    if head.direction=="left":
        x = head.xcor()
        head.setx(x-20)
    if head.direction=="right":
        x = head.xcor()
        head.setx(x+20)

# keyboard bindings
wn.listen() # tell window to listen for keyboard presses
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")


# main game loop
while True:
    wn.update()
    move()
    time.sleep(delay)



wn.mainloop() # keep the window open