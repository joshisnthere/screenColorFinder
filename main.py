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

        self.pick_btn = ctk.CTkButton(self, text="Pick a color", fg_color="#2a2a30",
                                       command=self._start_picking)
        self.pick_btn.pack(pady=10)

        ctk.CTkLabel(self, text="History", text_color="#8a8a8a").pack(anchor="w", padx=24, pady=(10, 4))
        self.history_box = ctk.CTkTextbox(self, fg_color=PANEL, height=260, width=380)
        self.history_box.pack(padx=20)
        self.history_box.configure(state="disabled")

        self._listener = None

    def _start_picking(self):
        self.pick_btn.configure(text="Click anywhere on screen...", state="disabled")
        self._listener = mouse.Listener(on_click=self._on_click)
        self._listener.start()

    def _on_click(self, x, y, button, pressed):
        if not pressed:
            return
        r, g, b = pyautogui.pixel(int(x), int(y))
        hex_code = f"#{r:02x}{g:02x}{b:02x}"

        self.after(0, self._show_result, hex_code, r, g, b)
        return False  # stop listener after one click

    def _show_result(self, hex_code, r, g, b):
        self.swatch.configure(fg_color=hex_code)
        self.value_var.set(f"{hex_code.upper()}\nRGB {r}, {g}, {b}")

        self.history_box.configure(state="normal")
        self.history_box.insert("end", f"{hex_code.upper()}   RGB({r}, {g}, {b})\n")
        self.history_box.see("end")
        self.history_box.configure(state="disabled")