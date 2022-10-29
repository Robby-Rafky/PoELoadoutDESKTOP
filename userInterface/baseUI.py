import tkinter as tk
from tkinter import messagebox
import json

# COLOURS---------------------------------------------
WHITE = "#ffffff"
BLACK = "#919191"
GREY = "#505050"
L_GREY = "#919191"
BLUE = "#6790b8"
D_BLUE = "#0f1a24"
# ----------------------------------------------------


def on_app_close():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        config_file.close()
        base_window.destroy()


# ----------------------------------------------------


config_file = open("userInterface/configUI.json", "r+")
ui_config = json.load(config_file)

base_window = tk.Tk()

base_window.geometry(f'{ui_config["settings"]["width"]}x{ui_config["settings"]["height"]}')
base_window.resizable(False, False)
base_window.title("PoE Loadout Desktop")
base_window["bg"] = D_BLUE

base_window.wm_protocol("WM_DELETE_WINDOW", on_app_close)
