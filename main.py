import sys, os
cwd = os.getcwd()
sys.path.append(cwd + "/GameEngine/Engine")
from Engine import Engine, EngineInit
from typetest import TypeTest

class Main(EngineInit):

    def startWorld(self, ex):
        return TypeTest(ex)

if __name__ == "__main__":
    main = Main()
    Engine.start(main)
