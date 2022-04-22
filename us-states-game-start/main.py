import turtle, pandas

# Set up screen
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

#  Add image to screen
turtle.shape(image)

# Create list of guessed states
guessed_states = []

# Play until all 50 states guessed
while len(guessed_states) < 50:
    # Ask user to guess state and show how many states correct
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?")

    answer = answer_state.title()

    # Take state data from csv file to a list
    data = pandas.read_csv("50_states.csv")
    all_states = data.state.to_list()

    # Upon exit save the states not identified in new csv file
    if answer == "Exit":
        still_to_learn = [state for state in all_states if state not in guessed_states]
        
        missing_states_data = pandas.DataFrame(still_to_learn)
        missing_states_data.to_csv("states_to_learn.csv")

        break
    # Add correct guesses to list of guessed states
    elif answer in all_states and answer not in guessed_states:
        guessed_states.append(answer)
        new_data = data[data.state == answer]
        print(new_data)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(new_data.x), int(new_data.y))
        t.write(answer)

    elif answer in guessed_states:
        pass

