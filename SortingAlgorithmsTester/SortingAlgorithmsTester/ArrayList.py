from random import Random
class ArrayList:
    """A object that creates and performs functions on a list"""

    def __init__(this, numOfItems):
        this.items = []
        rand = Random()
        for i in range(0, numOfItems):
            this.items.append(rand.randint(0,500))

    def sortList(this):
        items = this.items
        flipped = True
        
        while(flipped):
            flipped = False
            for i in range(0, len(items)-1):
                for j in range(i + 1, len(items)):
                    if(items[i] > items[j]):
                        temp = items[i]
                        items[i] = items[j]
                        items[j] = temp
                        flipped = True

    def reverseSortList(this):
        items = this.items
        flipped = True
        
        while(flipped):
            flipped = False
            for i in range(0, len(items)-1):
                for j in range(i + 1, len(items)):
                    if(items[i] < items[j]):
                        temp = items[i]
                        items[i] = items[j]
                        items[j] = temp
                        flipped = True
    
    def semiSortList(this):
        this.sortList()
        print(this.items)
        items = this.items
        rand = Random()

        for i in range(0,len(items)):
            swap = rand.randint(1,4)

            if(i+swap > len(items)-1):
                continue

            temp = items[i]
            items[i] = items[i+swap]
            items[i+swap] = temp
            i += rand.randint(0, 4)

            if( i > len(items)-1):
                break

