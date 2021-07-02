from tkinter import *
BG = "#446491"
FONT_COLOUR = "#E4FCF9"
class Palindrome_ui:
    def __init__(self):
        self.window = Tk()
        self.window.title("Palindrome checker")
        self.window.config(padx=10, pady=10, bg=BG)
        self.text = Label(text="Palindrome checker", font=("ariel", 20, "italic"), fg=FONT_COLOUR)
        self.text.grid(row=0, column=0)
        self.text.config(pady=20, padx=20, bg=BG)
        self.input_word = Entry(width=40)
        self.input_word.grid(row=1, column=0, pady=10)
        self.result = Label(text="None", font=("ariel", 13), bg=BG, fg=FONT_COLOUR)
        self.result.grid(row=2, column=0)
        self.generate_button = Button(text="Generate", font=("ariel", 13, "italic"))
        self.generate_button.grid(row=3, column=0, pady=10)
        self.generate_button.config(width=23)
        self.window.mainloop()