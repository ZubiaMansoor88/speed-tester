import tkinter as tk
import time
from tkinter import messagebox

sample_text = "The quick brown fox jumps over the lazy dog."


# TODO: MEASURE START TIME
def set_start_time():
    global start_time
    type_text.config(state=tk.NORMAL)
    type_text.delete('1.0', tk.END)
    start_time = time.time()
    return start_time


# TODO: SET TYPING SPEED OUTCOMES
def typing_speed():
    entered_text = type_text.get("1.0", "end-1c")
    if entered_text == sample_text:
        end = time.time()
        elapsed_time = end - start_time
        words_typed = len(entered_text.split())
        words_per_minute = words_typed / (elapsed_time / 60)
        result_label.config(text=f"Your typing speed is {words_per_minute:.2f} words per minute.")
        result.config(text=f"You are {check_result(words_per_minute)} typist.")
        type_text.config(state=tk.DISABLED)
        check_result(words_per_minute)
    else:
        messagebox.showerror("Invalid Content", "Type the given text accurately")
        type_text.delete('1.0', tk.END)
        


# TODO: EVALUATE TYPING SPEED
def check_result(words_per_minute):
    if words_per_minute <= 30:
        return "a learner"
    elif 30 < words_per_minute <= 35:
        return "a slow"
    elif 35 < words_per_minute <= 45:
        return "an average"
    else:
        return "a fast"


# TODO: CREATE TKINTER WINDOW
window = tk.Tk()
window.title("Speed Tester")

info_label = tk.Label(window, text="Type the given text below:")
info_label.grid(row=0, column=0, columnspan=2)

sample_text_label = tk.Label(window, text=sample_text)
sample_text_label.grid(row=1, column=0, columnspan=2)

type_text = tk.Text(window, wrap=tk.WORD, height=5, width=40)
type_text.grid(row=2, column=0, columnspan=2)
type_text.config(state=tk.DISABLED)

start_button = tk.Button(window, text="Start Typing", command=set_start_time)
start_button.grid(row=3, column=0, padx=5, pady=5)

speed_button = tk.Button(window, text="Test Speed", command=typing_speed)
speed_button.grid(row=3, column=1, padx=5, pady=5)

result_label = tk.Label(window, text="")
result_label.grid(row=4, column=0, columnspan=2)

result = tk.Label(window, text="")
result.grid(row=5, column=0, columnspan=2)

window.mainloop()
