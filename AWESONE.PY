# a121_catch_a_turtle.py
#-----import statements-----
import turtle 
import random as rand
#-----game configuration----
turtle_color = "pink"
turtle_shape = "circle"
turtle_size = 2
score = 0
Font_setup = ("Arial", 20, "normal")
timer = 30
counter_interval = 1000   #1000 represents 1 second
timer_up = False
#-----initialize turtle-----
turtle.Turtle()
turtle.shape(turtle_shape)
turtle.shapesize(turtle_size)
turtle.fillcolor(turtle_color)
score_writer =  turtle.Turtle()
score_writer.hideturtle()
score_writer.pu()
score_writer.goto(-170,180)
counter =  turtle.Turtle()
counter.goto(250,180)


#-----game functions--------
def update_score_for_turtle(x,y):
  global score
  score += 1
  score_writer.clear()
  score_writer.write(score,font=Font_setup)

def change_position():     
    new_xpos = rand.randint(1, 400)
    new_ypos = rand.randint(1, 400)
    turtle.goto(new_xpos,new_ypos)
def turtle_clicked(x,y): 
  if timer_up == False:
    change_position()
    update_score_for_turtle(x,y)
  else:
    turtle.hideturtle()


  

def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("YOU SUCK KID", font=Font_setup)
    timer_up = True
  else:
    counter.write("Timer: " + str(timer), font=Font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval)



#-----events----------------
turtle.onclick(turtle_clicked)
wn = turtle.Screen()
wn.ontimer(countdown, counter_interval) 
wn.mainloop()
