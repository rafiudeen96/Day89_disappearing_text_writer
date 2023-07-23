import time
from tkinter import *
from random import *
from time import *

beginning_text = ""

i = 5
timer = 0

is_button_pressed = False

loop = None

after=None

beginning_text_label = None


def func_random_prompt_generator():
    prompt_generator_window = Tk()
    prompt_generator_window.title("Dangerous Prompt Generator")
    prompt_generator_window.geometry("900x500")
    prompt_generator_window.configure(bg="white")

    # ------------------------------------Welcoming Label-----------------------------------------------------#
    greeting_kind_label = Label(text="The Most Dangerous Random Prompt Generator", font=("Arial", 25, "bold"),
                                fg="black",bg="white")
    greeting_kind_label.place(x=100, y=100)

    greeting_kind_label.

    # -------------------------------------Function Random prompt------------------------------------------------#

    def func_random_text():

        global beginning_text,beginning_text_label

        text_list = ["She decided to go to her father's grave, to ask his advice",
                     "He was terrified of small spaces and she knew",
                     "They had to work together, so they would need to"]

        beginning_text = choice(text_list)

        beginning_text_label = Label(text=beginning_text,bg="white",font=("Arial", 15, "bold"), fg="black", anchor="center")
        beginning_text_label.place(x=100, y=150)

    # ------------------------------------------------Calling the function Random text at beginning--------------------#

    func_random_text()

    # ----------------------------------------------Function calling random text for the second time ------------------#
    def func_calling_random_text():
        global beginning_text_label

        beginning_text_label.destroy()

        func_random_text()


    # ----------------------------------------------------- Generate Random prompt ------------------------------------#

    random_text_generator_button = Button(text="Generate Prompt", command=func_calling_random_text)
    random_text_generator_button.place(x=100, y=220)

    # ---------------------------------------------------Function Dangerous Text Editor----------------------------#

    def func_dangerous_text_editor():
        global beginning_text,is_button_pressed
        text_editor_window = Toplevel(prompt_generator_window)
        text_editor_window.title("Dangerous Text Editor")
        text_editor_window.geometry("900x500")

        countdown_label = Label(text_editor_window, text="")


        def func_countdown():
            global i,is_button_pressed
            timer_one_sec = 1000
            if i >= 1:
                countdown_label.config(text=i)
                countdown_label.place(x=20, y=5)
                i -= 1
                text_editor_window.after(timer_one_sec, func_countdown)
            else:
                func_calling_random_text()
                is_button_pressed = False
                text_editor_window.destroy()


        def value_of_i(event):
            global i
            i=5

        def func_start_countdown(event):
            global i,is_button_pressed
            i = 5
            text_editor_window.unbind("<KeyPress>", keypress_one)
            func_countdown()
            is_button_pressed=True

        keypress_one=text_editor_window.bind("<KeyPress>",func_start_countdown)

        def infinite_loop():
            global is_button_pressed,i,after
            if is_button_pressed:
                print("true")
                if i==0:
                    text_editor_window.after_cancel(after)
                keypress_two = text_editor_window.bind("<KeyPress>",value_of_i)
            after=text_editor_window.after(1,infinite_loop)

        infinite_loop()

        editor_textbox = Text(text_editor_window)
        editor_textbox.place(x=100, y=100)
        editor_textbox.insert(INSERT, beginning_text)


        text_editor_window.mainloop()

    # --------------------------------------------- Open the text Editor ----------------------------------------------#

    start_writing_button = Button(text="Start Writing", command=func_dangerous_text_editor)
    start_writing_button.place(x=300, y=220)

    prompt_generator_window.mainloop()


func_random_prompt_generator()
