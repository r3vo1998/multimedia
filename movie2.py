from tkinter import *

class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widget()

    def create_widget(self):
        Label(self, text = "Укажите ваш любимый жанр кино").grid(row = 0, column = 0, sticky = W)
        Label(self, text = "Выберите ровно один: ").grid(row = 1, column = 0, sticky = W)

        self._favorite = StringVar()
        self._favorite.set(None)
        
        Radiobutton(self, text = "Комедия", variable = self._favorite, value = "комедия", command = self.update_text).grid(row = 2, column = 0, sticky = W)

        Radiobutton(self, text = "Драма", variable = self._favorite, value = "драма", command = self.update_text).grid(row = 3, column = 0, sticky = W)

        Radiobutton(self, text = "Романтика", variable = self._favorite, value = "романтика", command = self.update_text).grid(row = 4, column = 0, sticky = W)
                    
        self._results_txt = Text(self, width = 40, height = 5, wrap = WORD)
        self._results_txt.grid(row = 5, column = 0, columnspan = 3)

    def update_text(self):
        message = "Ваш любимый киножанр - "
        message += self._favorite.get()
        
        self._results_txt.delete(0.0, END)
        self._results_txt.insert(0.0, message)

root = Tk()
root.title("Киноман - 2")
app = Application(root)
root.mainloop()
