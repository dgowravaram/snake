import turtle
import time
import random

delay = 0.1

score = 0


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

# treat
treat = turtle.Turtle()
treat.speed(0) #fastest animation speed
treat.shape("circle")
treat.color("blue")
treat.penup()
treat.goto(0,100)

segments = []

# pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("score: 0", align="center", font=("courier", 24, "normal"))



def go_up():
    if head.direction!="down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction!="right":
        head.direction = "left"

def go_right():
    if head.direction!="left":
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

    # check for a collision with border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction="stop"

        # hide segments
        for segment in segments:
            segment.goto(1000, 1000)

        # clear segments list
        segments.clear()

        # reset score
        score = 0
        pen.clear()
        pen.write("Score: {} ".format(score), align="center", font=("courier", 24, "normal"))

    # move treat to random spot on screen if collision occurs
    if head.distance(treat) < 20:
        x = random.randint(-275, 275)
        y = random.randint(-275, 275)
        treat.goto(x, y)

        # add a segment to the snake
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("orange")
        new_segment.penup()
        segments.append(new_segment)

        # increase the score
        score+=10

        pen.clear()
        pen.write("Score: {} ".format(score), align="center", font=("courier", 24, "normal"))

    # move the end segments first in reverse order
    for index in range(len(segments)-1, 0,-1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

     # move segment to where head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()

    # check for head collision with body segments
    for segment in segments:
        if segment.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction="stop"

            for segment in segments:
                segment.goto(1000,1000)
            segments.clear()



    time.sleep(delay)



wn.mainloop() # keep the window open
