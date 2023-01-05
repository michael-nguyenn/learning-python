# SOLUTION FOR REEBORG'S WORLD HURDLE 4

def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()


while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()

# move forward
# when we first hit the wall wall_in_front() is true
# then we can turn right_left()
# if we at the wall then wall_on_right() is true
# while wall_on_right() is true
# we move()
# once we're at the top wall_on_right() becomes false
# we then turn_right()
# if front_is_clear()
# then we move()
# once we hit the ground, front_is_clear() becomes false
# we then. turn left() to return to original position
