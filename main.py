import math
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

difficulty_level_label = None
easy_button=None
medium_button=None
hard_button=None

def func_random_prompt_generator():
    prompt_generator_window = Tk()
    prompt_generator_window.title("Dangerous Prompt Generator")
    prompt_generator_window.geometry("900x500")
    prompt_generator_window.configure(bg="white")

    # ------------------------------------Welcoming Label-----------------------------------------------------#
    greeting_kind_label = Label(text="The Most Dangerous Random Prompt Generator", font=("Arial", 25, "bold"),
                                fg="black",bg="white")
    greeting_kind_label.place(x=100, y=100)


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

    # --------------------------------------------------------Function for the difficulty levels to show up-------- #
    def func_difficulty_level_labels():
        global difficulty_level_label,easy_button,medium_button,hard_button

        difficulty_level_label = Label(prompt_generator_window,text="Choose difficulty level to begin",bg="white")
        difficulty_level_label.place(x=100, y=280)

        easy_button = Button(prompt_generator_window,text="Easy",command=func_easy_mode)
        easy_button.place(x=100,y=320)

        medium_button = Button(prompt_generator_window,text="Medium",command=lambda :func_dangerous_text_editor(7))
        medium_button.place(x=200,y=320)

        hard_button = Button(prompt_generator_window,text="Hard",command=lambda :func_dangerous_text_editor(5))
        hard_button.place(x=300,y=320)


    # ---------------------------------------------------Function Dangerous Text Editor----------------------------#
    def func_dangerous_text_editor(minutes=None):
        global beginning_text,is_button_pressed
        text_editor_window = Toplevel(prompt_generator_window)
        text_editor_window.title("Dangerous Text Editor")
        text_editor_window.geometry("900x500")

        countdown_label = Label(text_editor_window, text="")

        session_time_label = Label(text_editor_window,text="")

        editor_textbox = Text(text_editor_window)
        editor_textbox.place(x=100, y=100)
        editor_textbox.insert(INSERT, beginning_text)

        current_score_label = Label(text_editor_window,text="Current Score : 0")
        current_score_label.place(x=100,y=30)




        def func_countdown(session_time=None):
            global i,is_button_pressed,difficulty_level_label,easy_button,medium_button,hard_button
            timer_one_sec = 1000
            if i >= 1:
                print(session_time)
                countdown_label.config(text=i)
                countdown_label.place(x=20, y=5)

                session_time_in_minutes = math.floor(session_time/60)
                session_time_in_seconds = session_time%60

                if session_time_in_minutes<10:
                    session_time_in_minutes = f"0{session_time_in_minutes}"

                if session_time_in_seconds<10:
                    session_time_in_seconds = f"0{session_time_in_seconds}"

                if session_time_in_seconds==0:
                    session_time_in_seconds="00"

                session_time_label.config(text=f"Session Time : {session_time_in_minutes}:{session_time_in_seconds}")
                session_time_label.place(x=400, y=5)

                func_infinite_loop(session_time)
                i -= 1
                text_editor_window.after(timer_one_sec, func_countdown,session_time-1)
            elif i==0 or session_time==0:
                score = func_infinite_loop(session_time)
                func_calling_random_text()
                is_button_pressed = False
                difficulty_level_label.destroy()
                easy_button.destroy()
                medium_button.destroy()
                hard_button.destroy()
                text_editor_window.destroy()
                return score



        def value_of_i(event):
            global i
            i=5

        def func_start_countdown(event):
            global i,is_button_pressed
            i = 5
            text_editor_window.unbind("<KeyPress>", keypress_one)
            func_countdown(minutes*60)
            is_button_pressed=True

        keypress_one=text_editor_window.bind("<KeyPress>",func_start_countdown)

        def func_infinite_loop(time=None):
            global is_button_pressed,i,after
            if is_button_pressed:
                text_in_the_editor = editor_textbox.get("1.0", "end-1c")
                length_of_text_in_textbox = len(text_in_the_editor.split(" "))

                length_of_beginning_text = len(beginning_text.split(" "))

                text_wrote = length_of_text_in_textbox - length_of_beginning_text

                current_score_label.config(text=f"Current Score: {text_wrote}")

                if i==0 or time==0:
                    text_editor_window.after_cancel(after)
                    return text_wrote
                keypress_two = text_editor_window.bind("<KeyPress>",value_of_i)
            after=text_editor_window.after(1,func_infinite_loop)

        text_editor_window.mainloop()
        return func_countdown

    def func_easy_mode():
        try:
            with open("easy.txt", "r") as easy:
                score = easy.read()
        except FileNotFoundError:
            score = 0

        current_score = func_dangerous_text_editor(10)

    # --------------------------------------------- Open the text Editor ----------------------------------------------#

    start_writing_button = Button(text="Start Writing", command=func_difficulty_level_labels)
    start_writing_button.place(x=300, y=220)

    prompt_generator_window.mainloop()


func_random_prompt_generator()
