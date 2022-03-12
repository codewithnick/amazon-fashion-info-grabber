import random
class Intro:
    def __init__(self):
        with open("intros.txt",encoding="utf8") as f:
            self.intros=f.read().split("\n")
    def get(self):
        return random.choice(self.intros)
    def get_intro(self,product,category):
        intro=self.get()
        intro=intro.replace("[product_title]"," "+product+" ")
        intro=intro.replace("[category]"," "+category+" ")
        return intro
