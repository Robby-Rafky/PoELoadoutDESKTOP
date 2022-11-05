import tkinter as tk
from tkinter import messagebox, ttk
from urllib.request import urlopen
import base64
import json

# COLOURS---------------------------------------------
import pandas as pd

WHITE = "#ffffff"
BLACK = "#919191"
GREY = "#505050"
L_GREY = "#919191"
BLUE = "#6790b8"
D_BLUE = "#0f1a24"

COLOUR_UNIQUE_TEXT = "#af6018"
COLOUR_FOIL_TEXT = "#82ad6a"
COLOUR_NORMAL_TEXT = "#c8c8c8"
COLOUR_OTHER_TEXT = "#aa9e76"

COLOUR_UNIQUE_BG = "#441c0b"
COLOUR_FOIL_BG = "#344247"
COLOUR_NORMAL_BG = "#313130"
COLOUR_OTHER_BG = "#423e2d"


# ----------------------------------------------------
def on_app_close():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        config_file.close()
        base_window.destroy()


def change_data_set():
    data_view["columns"] = list(df.columns)

    for column, text in zip(data_view["columns"], ["Chaos", "Exalted", "Divine"]):
        data_view.column(column, anchor="w")
        data_view.heading(column, text=text)

    for index, row in df.iterrows():
        data_view.insert("", 0, text=str(index), values=list(row))


def get_image_from_url(url):
    image_byt = urlopen(url).read()
    image_b64 = base64.encodebytes(image_byt)
    return tk.PhotoImage(data=image_b64)


def change_variant(x):
    selected_item = data_view.item(data_view.focus())["text"]
    selected_variant = variant_view.item(variant_view.focus())["text"]
    display_selected_data(variant_data[selected_item][selected_variant], selected_item)


def change_name_colour(rarity):
    if rarity == 9:
        item_name_label["bg"] = COLOUR_FOIL_BG
        item_name_label["fg"] = COLOUR_FOIL_TEXT
    elif rarity == 3:
        item_name_label["bg"] = COLOUR_UNIQUE_BG
        item_name_label["fg"] = COLOUR_UNIQUE_TEXT
    elif rarity != 5:
        item_name_label["bg"] = COLOUR_NORMAL_BG
        item_name_label["fg"] = COLOUR_NORMAL_TEXT
    else:
        item_name_label["bg"] = COLOUR_OTHER_BG
        item_name_label["fg"] = COLOUR_OTHER_TEXT


def display_selected_data(variant, variant_name):
    change_name_colour(variant["rarity"])
    variant_image = get_image_from_url(variant["icon"])
    item_image.configure(image=variant_image)
    item_image.image = variant_image

    item_name_label.place(height=50, width=440, x=230, y=30, anchor="center")
    item_image.place(x=230, y=150, anchor="center")

    item_name_text.set(variant_name)


def selected_additional_info(x):
    selected_item = data_view.item(data_view.focus())["text"]
    if selected_item != "":
        variant_item = list(variant_data[selected_item])[-1]

        variant_view.delete(*variant_view.get_children())
        var_df = pd.DataFrame.from_dict(variant_data[selected_item])
        var_df = var_df.transpose().sort_values(by=["chaosValue"])
        var_df = var_df.drop(["icon", "rarity"], axis=1)
        variant_view["columns"] = list(var_df.columns)

        variant_view.column("#0", minwidth=160, width=160, stretch=False)
        for column, text, size in zip(variant_view["columns"], ["Chaos", "Exalted", "Divine"], [100, 100, 100]):
            variant_view.column(column, minwidth=size, width=size, anchor="w", stretch=False)
            variant_view.heading(column, text=text)

        for index, row in var_df.iterrows():
            variant_view.insert("", 0, text=str(index), values=list(row))
        variant_view.place(relheight=1, relwidth=1)

        display_selected_data(variant_data[selected_item][variant_item], selected_item)


# ----------------------------------------------------
config_file = open("userInterface/configUI.json", "r+")
ui_config = json.load(config_file)

variant_file = open("dataHandling/TrimmedData/trimmedVariants.json", "r+")
variant_data = json.load(variant_file)

base_window = tk.Tk()

base_window.geometry(f'{ui_config["settings"]["width"]}x{ui_config["settings"]["height"]}')
base_window.resizable(False, False)
base_window.title("PoE Loadout Desktop")
base_window["bg"] = D_BLUE

base_window.wm_protocol("WM_DELETE_WINDOW", on_app_close)

item_name_text = tk.StringVar()

item_data_frame = tk.LabelFrame(base_window)
item_search_frame = tk.LabelFrame(base_window, text="Search")
dataset_select_frame = tk.LabelFrame(base_window)
additional_data_frame = tk.LabelFrame(base_window)
variant_data_frame = tk.LabelFrame(base_window)
general_frame = tk.LabelFrame(base_window)

item_name_label = tk.Label(additional_data_frame, textvariable=item_name_text,
                           bg=D_BLUE, font="MSSansSerif 18 bold")
item_image = tk.Label(additional_data_frame, bg=D_BLUE)

item_data_frame.place(height=600, width=1400, y=90, x=20)
item_search_frame.place(height=50, width=1400, y=20, x=20)
dataset_select_frame.place(height=350, width=1400, y=710, x=20)
additional_data_frame.place(height=300, width=460, y=90, x=1440)
variant_data_frame.place(height=300, width=460, y=390, x=1440)
general_frame.place(height=350, width=460, y=710, x=1440)

item_data_frame["bg"], item_data_frame["fg"] = D_BLUE, WHITE
item_search_frame["bg"], item_search_frame["fg"] = D_BLUE, WHITE
dataset_select_frame["bg"], dataset_select_frame["fg"] = D_BLUE, WHITE
additional_data_frame["bg"], additional_data_frame["fg"] = D_BLUE, WHITE
variant_data_frame["bg"], variant_data_frame["fg"] = D_BLUE, WHITE
general_frame["bg"], general_frame["fg"] = D_BLUE, WHITE

style = ttk.Style()
style.theme_use("alt")
style.configure("Treeview", background=D_BLUE, foreground=WHITE, fieldbackground=D_BLUE)
style.configure("Treeview.Heading", background=D_BLUE, foreground=WHITE)

data_view = ttk.Treeview(item_data_frame)
data_view.place(relheight=1, relwidth=1)

variant_view = ttk.Treeview(variant_data_frame)

data_view_scroll_y = tk.Scrollbar(item_data_frame, orient="vertical", command=data_view.yview)
data_view.configure(yscrollcommand=data_view_scroll_y.set)
data_view_scroll_y.pack(side="right", fill="y")

df = pd.read_json("dataHandling/TrimmedData/trimmedItems.json")
df = df.transpose().sort_values(by=["chaosValue"])

change_data_set()
data_view.bind("<ButtonRelease-1>", selected_additional_info)
variant_view.bind("<ButtonRelease-1>", change_variant)



