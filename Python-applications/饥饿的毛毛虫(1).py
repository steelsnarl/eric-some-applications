import turtle as t
import random
import time

t.bgcolor('yellow')
catarpillar = t.Turtle()
catarpillar.shape('square')
catarpillar.color('red')
catarpillar.speed(0)
catarpillar.penup()
catarpillar.hideturtle()
leaf = t.Turtle()
leaf_shape = ((0,0),(14,2),(18,6),(20,20),\
              (6,18),(2,14))
t.register_shape('leaf',leaf_shape)
leaf.shape('leaf')
leaf.color('green')
leaf.penup()
leaf.hideturtle()
leaf.speed(0)
game_started = False
text_turtle = t.Turtle()
text_turtle.write('Press SPACE to start',align='center',\
                  font=('Arial',16,'bold'))
text_turtle.hideturtle()

score_turtle = t.Turtle()
score_turtle.hideturtle()
score_turtle.speed(0)
def outside_window():
    left_wall = -t.window_width() / 2
    right_wall = t.window_width() / 2
    top_wall = t.window_height() / 2
    bottem_wall = -t.window_height() / 2
    (x,y) = catarpillar.pos()
    outside = \
            x < left_wall or \
            x > right_wall or \
            y < bottem_wall or \
            y > top_wall
    return outside
                        

def game_over():
    catarpillar.color('yellow')
    leaf.color('yellow')
    t.penup()
    t.hideturtle()
    t.write('GAME OVER!',align='center',font=('Arial',30,'normal'))
    

def display_score(current_score):
    score_turtle.clear()
    score_turtle.penup()
    x = (t.window_width() / 2) - 50
    y = (t.window_height() / 2) - 50
    score_turtle.setpos(x,y)
    score_turtle.write(str(current_score),align='right',\
                       font=('Arial',40,'bold'))
def place_leaf():
    leaf.hideturtle()
    leaf.setx(random.randint(-200,200))
    leaf.sety(random.randint(-200,200))
    leaf.showturtle()

def start_game():
    global game_started
    if game_started:
        return
    game_started = True

    score = 0
    text_turtle.clear()

    catarpillar_speed = 2
    catarpillar_length = 3
    catarpillar.showturtle()
    display_score(score)
    place_leaf()

    while True:
        catarpillar.forward(catarpillar_speed)
        if catarpillar.distance(leaf) < 20:
            place_leaf()
            catarpillar_length = catarpillar_length + 1
            catarpillar.shapesize(1,catarpillar_length,1)
            catarpillar_speed += 1
            score += 10
            display_score(score)
        if outside_window():
            game_over()
            break

def move_up():
    if ((catarpillar.heading() == 0) or (catarpillar.heading() == 180)):
        catarpillar.setheading(90)

def move_down():
    if ((catarpillar.heading() == 0) or (catarpillar.heading() == 180)):
        catarpillar.setheading(270)   

def move_left():
    if ((catarpillar.heading() == 90) or (catarpillar.heading() == 270)):
        catarpillar.setheading(180)

def move_right():
    if ((catarpillar.heading() == 90) or (catarpillar.heading() == 270)):
        catarpillar.setheading(0)
      
t.onkey(start_game,'space')
time.sleep(1)
while True:
    t.onkey(move_up,'Up')
    t.onkey(move_right,'Right')
    t.onkey(move_down,'Down')
    t.onkey(move_left,'Left')
    t.listen()
    t.mainloop()
t.done()   
    


