"""
Screen Color Picker

An eyedropper for your whole screen. Click "Pick", then click anywhere on
your display -- even outside this window -- and it grabs the exact pixel
color under your cursor, with a running history you can copy from.
"""

import customtkinter as ctk
from pynput import mouse
import pyautogui

ctk.set_appearance_mode("dark")

BG = "#0c0c0e"
PANEL = "#191919"
ACCENT = "#9ad1ff"


class ColorPickerApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Screen Color Picker")
        self.geometry("420x560")
        self.configure(fg_color=BG)
        self.attributes("-topmost", True)

        self.swatch = ctk.CTkFrame(self, fg_color="#333333", corner_radius=14, height=140)
        self.swatch.pack(fill="x", padx=20, pady=(20, 10))
        self.swatch.pack_propagate(False)

        self.value_var = ctk.StringVar(value="Pick a color to see its values")
        ctk.CTkLabel(self.swatch, textvariable=self.value_var, justify="left",
                     font=ctk.CTkFont(size=14)).pack(expand=True)