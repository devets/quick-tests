import sys, os
cwd = os.getcwd()
sys.path.append(cwd + "/GameEngine/Engine")
from World import World
from Entity import Entity
from Image import Image

class TypeTest (World):

    def __init__ (self, engine):
        super().__init__(engine)
        self.addEntity(Button(1), 25, 50)
        self.addEntity(Button(2), (750 + 25) / 2, 50)
        self.addEntity(Button(3), 750, 50)

    def run(self):
        pass

class Button (Entity):
  
    def __init__(self, buttonNum):
        super().__init__()
        self.buttonNum = buttonNum
        if buttonNum == 1:
          self.setImage(Image("beckyBlueButton.png"))
        elif buttonNum == 2:
          self.setImage(Image("orangeButton.png"))
        else:
          self.setImage(Image("yellowLemonVomitButton.png"))
        self.mouseDown = False
        
    def run(self):
        self.pushed = False
        
        if self.world.mousePressed() and (self.world.mouseX() < self.x + self.width) and \
                                         (self.world.mouseY() < self.y + self.height) and \
                                         (self.world.mouseX() > self.x) and \
                                         (self.world.mouseY() > self.y):
            self.pushed = True
            if self.buttonNum == 1:
                self.setImage(Image("beckyBlueButton-2.png"))
                print(BLUE)
            elif self.buttonNum == 2:
                self.setImage(Image("orangeButton-2.png"))
                print(ORANGE)
            elif self.buttonNum == 3:
                self.setImage(Image("yellowLemonVomitButton-2.png"))
                print(YELLOW)
                              
            
        else:
            self.pushed = False

        
