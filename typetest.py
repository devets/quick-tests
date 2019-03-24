import sys, os
cwd = os.getcwd()
sys.path.append(cwd + "/GameEngine/Engine")
from World import World
from Entity import Entity, ActiveEntity
from Image import Image

class TypeTest (World):

    def __init__ (self, engine):
        super().__init__(engine)
        self.addEntity(Button(1), 125, 150)
        self.addEntity(Button(2), (750 + 125) / 2, 150)
        self.addEntity(Button(3), 750, 150)

    def run(self):
        pass

class Button (ActiveEntity):
  
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
        
        #if self.world.mousePressed():
        #    print("ENTITY: "+str(self.x)+","+str(self.y)+" - MOUSE: "+str(self.world.mouseX())+","+str(self.world.mouseY()))



        if self.world.mousePressed() and ((self.world.mouseX() <= self.x + self.width) and \
                                         (self.world.mouseX() >= self.x) and \
                                         (self.world.mouseY() <= self.y + self.height) and \
                                         (self.world.mouseY() >= self.y)):
                print("It worked")
                
                self.pushed = True
                if self.buttonNum == 1:
                    self.setImage(Image("beckyBlueButton-2.png"))
                    print("BLUE")
                elif self.buttonNum == 2:
                    self.setImage(Image("orangeButton-2.png"))
                    print("ORANGE")
                elif self.buttonNum == 3:
                    self.setImage(Image("yellowLemonVomitButton-2.png"))
                    print("YELLOW")

        
