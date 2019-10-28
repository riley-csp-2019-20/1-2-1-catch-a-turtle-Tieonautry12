# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random

#-----game configuration----
turtleshape = "square"
turtlesize =  3
turtlecolor = "red"

score = 0

timer = 5
counter_interval = 1000
timer_up = False


#-----initialize turtle-----
clifford = trtl.Turtle(shape=turtleshape)
clifford.color(turtlecolor)
clifford.shapesize(turtlesize)
clifford.speed(300)

john = trtl.Turtle()
john.ht()
john.penup()
john.goto(-370, 270)

font_setup = ("Arial" , 30, "bold")
john.write(score , font=font_setup)

josh = trtl.Turtle()
josh.ht()
josh.penup()
josh.goto(270, 270 )

#-----game functions--------
def clifford_clicked(x,y):
    print("clifford got clicked")
    change_position()
    update_score()


def change_position():
    clifford.penup()
    clifford.ht()
    if not timer_up:
        cliffordx = random.randint(-400,400)
        cliffordy = random.randint(-300,300)
        clifford.goto(cliffordx,cliffordy)
        clifford.st()
    

def update_score():
    global score
    score += 1
    print(score)
    john.clear()
    john.write(score , font=font_setup)

def countdown():
  global timer, timer_up
  josh.clear()
  if timer <= 0:
    josh.write("Time's Up", font=font_setup)
    timer_up = True
  else:
    josh.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    josh.getscreen().ontimer(countdown, counter_interval) 
    


#-----events----------------

wn = trtl.Screen()
wn.bgcolor("yellow")
clifford.onclick(clifford_clicked)
wn.ontimer(countdown, counter_interval) 
wn.mainloop()