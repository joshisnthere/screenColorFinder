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