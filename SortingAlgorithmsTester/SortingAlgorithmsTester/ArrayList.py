from random import Random
class ArrayList:
    """A object that creates and performs functions on a list"""

    def __init__(this, numOfItems):
        this.items = []
        rand = Random()
        for i in range(0, numOfItems):
            this.items.append(rand.randint(0,100))

        
    
    