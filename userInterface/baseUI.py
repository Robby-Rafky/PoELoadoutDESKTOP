import tkinter as tk
from tkinter import messagebox, ttk
import json

# COLOURS---------------------------------------------
import pandas as pd

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


item_data_frame = tk.LabelFrame(base_window, text="Item Data")
item_search_frame = tk.LabelFrame(base_window, text="Search")
dataset_select_frame = tk.LabelFrame(base_window, text="Data Sets")
additional_data_frame = tk.LabelFrame(base_window, text="More Data")
general_frame = tk.LabelFrame(base_window, text="General")

item_data_frame.place(height=600, width=1400, y=90, x=20)
item_search_frame.place(height=50, width=1400, y=20, x=20)
dataset_select_frame.place(height=350, width=1400, y=710, x=20)
additional_data_frame.place(height=600, width=460, y=90, x=1440)
general_frame.place(height=350, width=460, y=710, x=1440)

item_data_frame["bg"], item_data_frame["fg"] = D_BLUE, WHITE
item_search_frame["bg"], item_search_frame["fg"] = D_BLUE, WHITE
dataset_select_frame["bg"], dataset_select_frame["fg"] = D_BLUE, WHITE
additional_data_frame["bg"], additional_data_frame["fg"] = D_BLUE, WHITE
general_frame["bg"], general_frame["fg"] = D_BLUE, WHITE

# ---test---
test_text = tk.StringVar()
label = tk.Label(additional_data_frame, textvariable=test_text)
# ----------

data_view = ttk.Treeview(item_data_frame)
data_view.place(relheight=1, relwidth=1)

data_view_scroll_y = tk.Scrollbar(item_data_frame, orient="vertical", command=data_view.yview)
data_view.configure(yscrollcommand=data_view_scroll_y)
data_view_scroll_y.pack(side="right", fill="y")

df = pd.read_json("dataHandling/TrimmedData/trimmedItems.json")
df = df.transpose().sort_values(by=["chaosValue"])
data_view["columns"] = list(df.columns)

# TODO - put into function for repeated uses
for column in data_view["columns"]:
    data_view.column(column, anchor="w")
    data_view.heading(column, text=column)

for index, row in df.iterrows():
    data_view.insert("", 0, text=str(index), values=list(row))

# TODO - fix this into a real function pulling data from trimmed variants
def selected_additional_info(x):
    curItem = data_view.item(data_view.focus())
    print(curItem)

    test_text.set(curItem["text"])


data_view.bind("<ButtonRelease-1>", selected_additional_info)
label.pack()


