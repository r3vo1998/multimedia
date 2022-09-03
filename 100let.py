from tkinter import *
class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()


    def create_widgets(self):
        self.__init__lbl = Label(self, text = "Чтобы узнать секрет долголетия, введите пароль")
        self.__init__lbl.grid(row = 0, column = 0, columnspan = 2, sticky = W)
        
        self._w_lbl = Label(self, text = "Пароль: ")
        self._w_lbl.grid(row = 1, column = 0, sticky = W)
        
        self._w_ent = Entry(self)
        self._w_ent.grid(row = 1, column = 1, sticky = W)
        
        self._submit_bttn = Button(self, text = "Узнать секрет", command = self.reveal)
        self._submit_bttn.grid(row = 2, column = 0, columnspan = 2, sticky = W)
        
        self._secret_txt = Text(self, width = 35, height = 5, wrap = WORD)
        self._secret_txt.grid(row = 3, column = 0, columnspan = 2, sticky = W)

    def reveal(self):
        contents = self._w_ent.get()

        if contents == "secret":
            message = "Чтобы дожить до 100 лет, надо сначала дожить до 99, а потом вести себя ОЧЕНЬ осторожно."
        else:
            message = "Вы ввели неправильный пароль, так что я не могу поделиться тайной с вами."
            
        self._secret_txt.delete(0.0, END)
        self._secret_txt.insert(0.0, message)


root = Tk()
root.title("Долгожитель")
root.geometry("300x150")
app = Application(root)
root.mainloop()

        
