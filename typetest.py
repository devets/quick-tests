import sys, os
cwd = os.getcwd()
sys.path.append(cwd + "/GameEngine/Engine")
from World import World
from Entity import Entity
from Image import Image


class TypeTest (World):
    def __init__ (self, engine):
        super().__init__(engine)
        self.addEntity(Button(),50, 50) 
    def run(self):
        pass

class Button (Entity):
    def __init__(self):
        super().__init__()
        self.image = Image("beckyBlueButton.png")
        
    
