import sys, os
cwd = os.getcwd()
sys.path.append(cwd + "/GameEngine/Engine")
from World import World
from Entity import Entity
from Image import Image


class TypeTest (World):
    def __init__ (self, engine):
        super().__init__(engine)
        self.addEntity(Button(1),50, 50) 
        self.addEntity(Button(2),450, 50) 
        self.addEntity(Button(3),850, 50) 
    def run(self):
        pass

class Button (Entity):
    def __init__(self, buttonNum):
        super().__init__()
        if buttonNum == 1:
          self.image = Image("beckyBlueButton.png")
        elif buttonNum == 2:
          self.image = Image("orangeButton-2.png")
        else:
          self.image = Image("yellowLemonVomitButton.png")
        
    
