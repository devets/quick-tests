import math
from Image import Image

class Entity():
    """General code for things that appear in the world."""

    def __init__(self):
        self.x = None
        self.y = None
        self.width = None
        self.height = None
        self.image = None
        self.world = None

        self.text = None    #this should remain none unless you want the object to be rendered as text.

        self.animated = False
        self.animationDelay = None
        self.animationCounter = 0

    def isTouching(self, entity):
        """Checks if an entity is in contact with another"""
        if not isinstance(entity, Entity):
            raise TypeError("Only accepts objects of type Entity")
        if (self.x <= entity.x + entity.width and
            self.x + self.width <= entity.x and
            self.y <= self.x + entity.height and
            self.y + self.height <= entity.y):
            return True
        return False

    def isInRange(self, entity, rng):
        """Checks the bounds of the given entity against its own."""
        if not isinstance(entity, Entity):
            raise TypeError("Only accepts objects of type Entity")
        if math.sqrt(((self.x + self.width / 2) - (entity.x + entity.width / 2))**2 +
                     ((self.y + self.height / 2) - (entity.y + entity.height / 2))**2) <= rng:
            return True
        return False

    def getNeighbors(self):

        neighbors = []
        for e in self.world.entity_list():
            if self.isTouching(e):
                neighbors.append(e)
        return neighbors

    def getNeighborsTyped(self, entity):
        """Get all entities in the current world of a specified type that are coliding with the\n
        entity making the call. \n
        entity -- An entity of some specific subclass you are looking for. \n
        Example: \n
        \tenemy = FireEnemy()\n
        \tfireEnemies = self.getNeighborsTyped(enemy) \n
        This will return all FireEnemy entities in the world that are touching the entity acting.
        """
        neighbors = []
        for e in self.world.entity_list():
            if self.isTouching(e) and isinstance(type(entity)) :
                neighbors.append(e)
        return neighbors

    def setImage(self, image):
        """Sets the image \n
        image -- Type Image
        """
        if not isinstance(image, Image):
            raise TypeError("Only accepts objects of type Image")
        self.image = image
        self.width = image.getWidth()
        self.height = image.getHeight()

    def getImage(self, scale):
        """Returns the image associated with the entity. \n
        scale -- A double representation of the scaling factor
        """
        if self.image == None:
            return None

        return self.image.getScaled(scale)

    def animationLoop(self):
        if self.animationCounter == self.animationDelay:
            self.image.nextImage()
            self.animationCounter = 0
        self.animationCounter += 1


class ActiveEntity(Entity):
    """A type of entity that allows for movement within the world."""

    def __init__(self):
        super().__init__()
        self.physical = False
        self.mass = 0
        self.x_speed = 0
        self.y_speed = 0
    
    def physics(self):
        """Applies the appropriate affects of game physics to the entity"""
        if self.physical:
            pass

        self.x = self.x + self.x_speed
        self.y = self.y + self.y_speed

    def run(self):
        """User implementation of run method."""
        pass
    
    def push(self, vector):
        """Adds a momentum vector to the entity\n
        vector -- magnitude and direction (radians) in a tuple
        """
        self.x_speed = (self.mass*self.x_speed+vector[0]*math.cos(vector[1]))/self.mass
        self.y_speed = (self.mass*self.y_speed+vector[0]*math.sin(vector[1]))/self.mass
