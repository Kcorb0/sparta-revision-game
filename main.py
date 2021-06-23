# --Things to add--
# Colour scheme options at the side or bottom (Dark mode etc)
# Image viewer for some answers to show visual aid for topics


import tkinter as tk
from tkinter import ttk
from tkinter.font import Font
from topics import agile, data_consepts, database_design, sql, python


class SpartaQuestionGenerator:
    def __init__(self, root):
        root.title("Sparta Question Generator")
        root.resizable(False, False)
        root.minsize(750, 550)
        root.iconbitmap("assets\logo\logo.ico")

        font_title = Font(
            family="roboto",
            size=20,
            weight="normal",
            slant="roman",
            underline=0,
            overstrike=0,
        )

        font_inp = Font(
            family="roboto",
            size=12,
            weight="normal",
            slant="roman",
            underline=0,
            overstrike=0,
        )

        # Outer frame
        outer_frame = ttk.Frame(root, padding=".2i")
        outer_frame.pack()

        title = ttk.Label(outer_frame, text="Question Generator", font=font_title)
        title.pack()

        # Entry field for user answer
        user_answer = tk.Text(outer_frame, width=100, height=10, font=font_inp)
        user_answer.pack()

        user_answer = ttk.Button(outer_frame, text="Compare Answer")
        user_answer.pack()


root = tk.Tk()
SpartaQuestionGenerator(root)
root.mainloop()
