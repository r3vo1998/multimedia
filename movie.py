from tkinter import *

class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widget()

    def create_widget(self):
        Label(self, text = "Укажите ваши любимые жанры кино").grid(row = 0, column = 0, sticky = W)
        Label(self, text = "Выберите всё, что вам по вкусу: ").grid(row = 1, column = 0, sticky = W)

        self._likes_comedy = BooleanVar()
        Checkbutton(self, text = "Комедия", variable = self._likes_comedy, command = self.update_text).grid(row = 2, column = 0, sticky = W)

        self._likes_drama = BooleanVar()
        Checkbutton(self, text = "Драма", variable = self._likes_drama, command = self.update_text).grid(row = 3, column = 0, sticky = W)

        self._likes_romance = BooleanVar()
        Checkbutton(self, text = "Романтика", variable = self._likes_romance, command = self.update_text).grid(row = 4, column = 0, sticky = W)
                    
        self._results_txt = Text(self, width = 40, height = 5, wrap = WORD)
        self._results_txt.grid(row = 5, column = 0, columnspan = 3)

    def update_text(self):
        likes = ""
        if self._likes_comedy.get():
            likes += "Вам нравятся комедии.\n"
        if self._likes_drama.get():
            likes += "Вас привлекает жанр драмы.\n"
        if self._likes_romance.get():
            likes += "Вам по вкусу кино о любви."
        self._results_txt.delete(0.0, END)
        self._results_txt.insert(0.0, likes)

root = Tk()
root.title("Киноман")
app = Application(root)
root.mainloop()
