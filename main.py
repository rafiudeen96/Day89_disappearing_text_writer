import time
from tkinter import *
from random import *
from time import *

beginning_text = ""

i = 5
timer = 0

loop = None


def func_random_prompt_generator():
    prompt_generator_window = Tk()
    prompt_generator_window.title("Dangerous Prompt Generator")
    prompt_generator_window.geometry("900x500")

    # ------------------------------------Welcoming Label-----------------------------------------------------#
    greeting_kind_label = Label(text="The Most Dangerous Random Prompt Generator", font=("Arial", 25, "bold"),
                                fg="black")
    greeting_kind_label.place(x=100, y=100)

    # -------------------------------------Function Random prompt------------------------------------------------#

    def func_random_text():

        global beginning_text

        text_list = ["She decided to go to her father's grave, to ask his advice",
                     "He was terrified of small spaces and she knew",
                     "They had to work together, so they would need to"]

        beginning_text = choice(text_list)

        beginning_text_label = Label(text=beginning_text, font=("Arial", 15, "bold"), fg="black", anchor="center")
        beginning_text_label.place(x=100, y=150)

    # ------------------------------------------------Calling the function Random text at beginning--------------------#

    func_random_text()

    # ----------------------------------------------------- Generate Random prompt ------------------------------------#
    random_text_generator_button = Button(text="Generate Prompt", command=func_random_text)
    random_text_generator_button.place(x=100, y=220)

    # ---------------------------------------------------Function Dangerous Text Editor----------------------------#

    def func_dangerous_text_editor():
        global beginning_text
        text_editor_window = Tk()
        text_editor_window.title("Dangerous Text Editor")
        text_editor_window.geometry("900x500")

        countdown_label = Label(text_editor_window, text="")

        def func_countdown(keypress=None):
            global i, timer, loop
            timer_one_sec = 1000
            if i >= -1:
                countdown_label.config(text=i)
                countdown_label.place(x=20, y=5)
                i -= 1
                if keypress:
                    timer += 1000
                    print("keypress")
                print(f"Timer: {timer}")
                loop = text_editor_window.after(timer, func_countdown)
            else:
                text_editor_window.destroy()

        def func_start_countdown(event):
            global i
            i = 5
            key_press = True
            func_countdown(key_press)

        text_editor_window.bind("<KeyPress>", func_start_countdown)

        editor_textbox = Text(text_editor_window)
        editor_textbox.place(x=100, y=100)
        editor_textbox.insert(INSERT, beginning_text)

        text_editor_window.mainloop()

    # --------------------------------------------- Open the text Editor ----------------------------------------------#

    start_writing_button = Button(text="Start Writing", command=func_dangerous_text_editor)
    start_writing_button.place(x=300, y=220)

    prompt_generator_window.mainloop()


func_random_prompt_generator()
