import random
class Intro:
    def __init__(self):
        with open("intros.txt",encoding="utf8") as f:
            self.intros=f.read().split("\n")
    def get(self):
        return random.choice(self.intros)
    def get_intro(self,book,author):
        intro=self.get()
        intro=intro.replace("[book_title]"," "+book+" ")
        intro=intro.replace("[author_name]"," "+author+" ")
        return intro
