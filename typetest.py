import sys, os
cwd = os.getcwd()
sys.path.append(cwd + "/GameEngine/Engine")
from World import World

class TypeTest (World):
    def __init__ (self, engine):
        super().__init__(engine)