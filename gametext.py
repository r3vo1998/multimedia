from tkinter import *

class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widget()

    def create_widget(self):
        Label(self, text = "Введите данные для создания нового рассказа").grid(row = 0, column = 0, columnspan = 2, sticky = W)
        Label(self, text = "Имя человека: ").grid(row = 1, column = 0, sticky = W)
        self.person_ent = Entry(self)
        self.person_ent.grid(row = 1, column = 1, sticky = W)

        Label(self, text = "Существительное во мн. ч.: ").grid(row = 2, column = 0, sticky = W)
        self.noun_ent = Entry(self)
        self.noun_ent.grid(row = 2, column =1, sticky = W)

        Label(self, text = "Глагол в инфинитиве: ").grid(row = 3, column = 0, sticky = W)
        self.verb_ent = Entry(self)
        self.verb_ent.grid(row = 3, column = 1, sticky = W)

        Label(self, text = "Прилагательное (-ые): ").grid(row = 4, column = 0, sticky = W)
        
        self._is_itchy = BooleanVar()
        Checkbutton(self, text = "нетерпеливый", variable = self._is_itchy).grid(row = 4, column = 1, sticky = W)

        self._is_joyous = BooleanVar()
        Checkbutton(self, text = "радостный", variable = self._is_joyous).grid(row = 4, column = 2, sticky = W)

        self._is_electric = BooleanVar()
        Checkbutton(self, text = "пронизывающий", variable = self._is_electric).grid(row = 4, column = 3, sticky = W)

        Label(self, text = "Body Part:").grid(row = 5, column = 0, sticky = W)
        self.body_part = StringVar()
        self.body_part.set(None)
        body_parts = ["пупок", "большой палец ноги", "продолговатый мозг"]
        column = 1
        for part in body_parts:
            Radiobutton(self, text = part, variable = self.body_part, value = part).grid(row = 5, column = column, sticky = W)
            column += 1

        Button(self, text = "Получить рассказ", command = self.tell_story).grid(row = 6, column = 0, sticky = W)
        self.story_txt = Text(self, width = 75, height = 10, wrap = WORD)
        self.story_txt.grid(row = 7, column = 0, columnspan = 4)


    def tell_story(self):
        person = self.person_ent.get()
        noun = self.noun_ent.get()
        verb = self.verb_ent.get()
        adjectives = ""
        if self._is_itchy.get():
            adjectives += "нетерпеливое. "
        if self._is_joyous.get():
            adjectives += "радостное. "
        if self._is_electric.get():
            adjectives += "пронизывающее. "
        body_part = self.body_part.get()
        story = "Знаменитый путешественник "
        story += person
        story += " уже совсем отчаялся довершить дело всей своей жизни - поиск затерянного города, в котором, по легенде, обитали "
        story += noun.title()
        story += ". Но однажды "
        story += noun
        story += " и "
        story += person + " столкнулись лицом к лицу. "
        story += "Мощное. "
        story += adjectives
        story += "ни с чем не сравнимое чувство охватило душу путешественника. "
        story += "После стольких лет поисков цель была наконец достигнута. "
        story += person
        story += " ощутил, как на его " + body_part + " скатилась слезинка. "
        story += "И тут внезапно "
        story += noun
        story += " перешли в атаку, и "
        story += person + " был ими мгновенно сожран. "
        story += "Мораль? Если задумали "
        story += verb
        story += ", надо делать это с осторожностью."

        self.story_txt.delete(0.0, END)
        self.story_txt.insert(0.0, story)
    

root = Tk()
root.title("Сумасшедший сказочник")
app = Application(root)
root.mainloop()
