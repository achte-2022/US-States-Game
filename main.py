# Importing Libraries
import turtle
import pandas as pd


# Constants
IMAGE_FILE = "blank_states_img.gif"
STATE_COORDS_FILE = "state_coords.csv"
STATES_TO_LEARN_FILE = "states_to_learn.csv"


def print_state(x, y, state):
    state_turtle = turtle.Turtle()
    state_turtle.penup()
    state_turtle.hideturtle()
    state_turtle.goto(x=x, y=y)
    state_turtle.write(state)
    return


# Object Setup
window = turtle.Screen()
window.title("US States Game")
window.addshape(IMAGE_FILE)
window.tracer(0)

turtle.shape(IMAGE_FILE)
window.update()

states_df = pd.read_csv(STATE_COORDS_FILE)
states_list = states_df["state"].to_list()
num_states = len(states_list)

is_game_on = True

correct_guesses = {"state": []}

while len(correct_guesses["state"]) < num_states:
    if len(correct_guesses["state"]) == 0:
        user_answer = window.textinput(
            title="Guess a US state's name.", prompt="Enter your answer: "
        ).title()
    else:
        user_answer = window.textinput(
            title=f"{len(correct_guesses['state'])}/{num_states} States Correct",
            prompt="Enter your answer: ",
        ).title()

    if user_answer == "Exit":
        break

    if (user_answer not in correct_guesses) and (user_answer in states_list):
        correct_guesses["state"].append(user_answer)
        current_state = states_df[states_df["state"] == user_answer]
        x_cor = int(current_state["x"])
        y_cor = int(current_state["y"])
        print_state(x_cor, y_cor, user_answer)
        window.update()


states_to_learn_list = [
    state for state in states_list if state not in correct_guesses["state"]
]

states_to_learn_df = pd.DataFrame(states_to_learn_list, columns=["state"])
print(states_to_learn_df)
states_to_learn_df.to_csv(STATES_TO_LEARN_FILE)
