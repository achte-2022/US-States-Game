# Importing Libraries
import turtle
import pandas as pd
import time

# Constants
IMAGE_FILE = "blank_states_img.gif"
STATES_FILE = "states.csv"
STATE_COORDS_FILE = "state_coords.csv"

states_dict = {"state": [], "x": [], "y": []}


def get_state_coords(x, y):
    states_dict["x"].append(x)
    states_dict["y"].append(y)
    return


# Object Setup
window = turtle.Screen()
window.title("Get State Coordinates")
window.addshape(IMAGE_FILE)
window.tracer(0)

turtle.shape(IMAGE_FILE)
window.update()

states_series = pd.read_csv(STATES_FILE)
states_list = states_series["state"].to_list()
num_states = len(states_list)
states_dict["state"] = states_list

window.onscreenclick(get_state_coords)

for state in states_list:
    window.update()
    window.title(f"Click {state}")
    time.sleep(5)

print(states_dict)
states_df = pd.DataFrame(states_dict)
states_df.to_csv(STATE_COORDS_FILE)
turtle.mainloop()
