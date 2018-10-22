from ArrayList import ArrayList
from Sort import Sort
import math

while(True):
    try:
        numOfItems = int(input("How many items would you like to contain in the list? "))
        if(numOfItems <= 0 ):
            print("Number of items must be greater than 0")
            continue
        else:
            break
    except ValueError:
        print("Must be of type integer")
        continue

listOfItems = ArrayList(numOfItems)
print(listOfItems.items)

while(True):
    try:
        print("Would you like the list: \n1. Sorted\n2. Reverse Sorted\n3. Semi-Sorted\n4. Unchanged")
        selection = int(input("Please enter number corresponding to selection: "))
        if(selection < 1 or selection > 4):
            print("Please enter a number from the selection")
            continue
        else:
            break
    except ValueError:
        print("Must be of type integer")
        continue

switch = {1: listOfItems.sortList(),
          2: listOfItems.reverseSortList(),
          3: listOfItems.semiSortList(),
          4: None
          }

switch[selection]
print("Before Sort" + str(listOfItems.items))
Sort.insertionSort(listOfItems.items)
print("After Sort" + str(listOfItems.items))

