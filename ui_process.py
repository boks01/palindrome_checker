from tkinter import *
from tkinter import messagebox
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
        self.generate_button = Button(
            text="Generate", 
            font=("ariel", 13, "italic"), 
            command=self.checking)
        self.generate_button.grid(row=3, column=0, pady=10)
        self.generate_button.config(width=23)
        self.window.mainloop()
    
    def checking(self):
        taking_word = self.input_word.get()
        check_word = 0
        word_list = [letter.lower() for letter in taking_word]
        len_word = len(word_list)
        if taking_word == "":
            messagebox.showwarning("warning", "warning!!\nyou must fill in all fields!")
        else:
            # print(word_list)
            # print(len_word)
            # print(taking_word)
            for i in range(len_word):
                if word_list[i] == word_list[len_word-(i+1)]:
                    check_word += 1
                    if check_word == len_word - 1:
                        self.result.config(text=f"{taking_word}\nis palindrome word.")
                        # print(f"{taking_word} is palindrome word.")
                else:
                    self.result.config(text=f"{taking_word}\nisn't palindrome word.")
                    # print(f"{taking_word} isn't palindrome word.")