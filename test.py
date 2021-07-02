class Test:
    def __init__(self, word):
        self.word = word
    
    def checking(self):
        check_word = 0
        len_word = len(self.word)
        word_list = [letter.lower() for letter in self.word]
        for i in range(len_word):
            if word_list[i] == word_list[len_word-(i+1)]:
                check_word += 1
                if check_word == len_word - 1:
                    return f"{self.word} is palindrome word."
            else:
                return f"{self.word} isn't palindrome word."