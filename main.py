import math
from tkinter import *
from random import *
from time import *
from tkinter import messagebox

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

is_high_score_attained = False


start_countdown = True

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

        medium_button = Button(prompt_generator_window,text="Medium",command=func_medium_mode)
        medium_button.place(x=200,y=320)

        hard_button = Button(prompt_generator_window,text="Hard",command=func_hard_mode)
        hard_button.place(x=300,y=320)

    def func_easy_mode():
        try:
            with open("easy.txt","r") as easy:
                score=easy.read()
        except FileNotFoundError:
            score=0

        func_dangerous_text_editor(10,"easy",score)

    def func_medium_mode():
        try:
            with open("medium.txt","r") as medium:
                score=medium.read()
        except FileNotFoundError:
            score=0

        func_dangerous_text_editor(7,"medium",score)

    def func_hard_mode():
        try:
            with open("hard.txt","r") as hard:
                score = hard.read()
                if score == "":
                    score = 0
        except FileNotFoundError:
            score = 0

        func_dangerous_text_editor(5,"hard",score)

    # ---------------------------------------------------Function Dangerous Text Editor----------------------------#
    def func_dangerous_text_editor(minutes,mode,score):
        global beginning_text,is_button_pressed,start_countdown
        start_countdown=True
        text_editor_window = Toplevel(prompt_generator_window)
        text_editor_window.title("Dangerous Text Editor")
        text_editor_window.geometry("900x500")
        score = int(score)

        countdown_label = Label(text_editor_window, text="")

        session_time_label = Label(text_editor_window,text="")

        testing_current_score_label = Label(text_editor_window,text="")
        testing_current_score_label.place(x=400,y=30)

        editor_textbox = Text(text_editor_window)
        editor_textbox.place(x=100, y=100)
        editor_textbox.insert(INSERT, beginning_text)

        current_score_label = Label(text_editor_window,text="Current Score : 0")
        current_score_label.place(x=100,y=30)

        high_score_label = Label(text_editor_window,text=f"High Score : {score}")
        high_score_label.place(x=100,y=60)


        def func_countdown(session_time):
            global i,is_button_pressed,difficulty_level_label,easy_button,medium_button,\
                hard_button,is_high_score_attained
            timer_one_sec = 1000
            if i >= 1 and session_time >= 1:
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


                i -= 1
                text_editor_window.after(timer_one_sec, func_countdown,session_time-1)
            else:
                func_calling_random_text()
                is_button_pressed = False
                difficulty_level_label.destroy()
                easy_button.destroy()
                medium_button.destroy()
                hard_button.destroy()
                if not is_high_score_attained:
                    text_editor_window.destroy()


        def func_start_countdown(event):
            global i,is_button_pressed,start_countdown
            i = 5
            if start_countdown:
                func_countdown(minutes*60)
                start_countdown = False
            is_button_pressed=True

        keypress_one=text_editor_window.bind("<KeyPress>",func_start_countdown)

        def infinite_loop():
            global is_button_pressed,beginning_text,i,after,is_high_score_attained
            if type(beginning_text) == str:
                beginning_text = beginning_text.split(" ")
            difficulty_level = False
            if is_button_pressed:
                text_in_the_editor = editor_textbox.get("1.0", "end-1c")

                length_of_text_in_textbox = len(text_in_the_editor.split(" "))

                length_of_beginning_text = len(beginning_text)

                print(length_of_beginning_text)

                text_wrote = length_of_text_in_textbox - length_of_beginning_text

# -------------- Ensuring score didn't go minus even if the text showing is get deleted and start counting from zero---#

                if text_wrote == -1:
                    beginning_text.pop()
                    print(f"length of beginning text : {len(beginning_text)}")

# ------------------------ Ensuring that pressing space didn't get counted as score point-----------------------------#

                for number in range(len(text_in_the_editor)-1,0,-1):
                    if text_in_the_editor[number] == " " and text_in_the_editor[number-1] == " ":
                        text_wrote-=1

                current_score_label.config(text=f"Current Score: {text_wrote}")

                if text_wrote > score and mode == "easy":
                    high_score_label.config(text=f"High Score : {text_wrote}")
                    with open("easy.txt", "w") as easy:
                        easy.write(str(text_wrote))
                    difficulty_level=True
                elif text_wrote > score and mode == "medium":
                    high_score_label.config(text=f"High Score : {text_wrote}")
                    with open("medium.txt", "w") as medium:
                        medium.write(str(text_wrote))
                    difficulty_level=True
                elif text_wrote > score and mode == "hard":
                    high_score_label.config(text=f"High Score : {text_wrote}")
                    with open("hard.txt","w") as hard:
                        hard.write(str(text_wrote))
                    difficulty_level=True
                if i == 0:
                    sleep(1)
                    text_editor_window.after_cancel(after)
                    if difficulty_level:
                        is_high_score_attained = True
                        if messagebox.showinfo("messagebox",f"You've made a new High Score: {text_wrote}",parent=text_editor_window):
                            text_editor_window.destroy()

                # is_button_pressed=False
            after=text_editor_window.after(1,infinite_loop)

        infinite_loop()

        text_editor_window.mainloop()

    # --------------------------------------------- Open the text Editor ----------------------------------------------#

    start_writing_button = Button(text="Start Writing", command=func_difficulty_level_labels)
    start_writing_button.place(x=300, y=220)

    prompt_generator_window.mainloop()


func_random_prompt_generator()
