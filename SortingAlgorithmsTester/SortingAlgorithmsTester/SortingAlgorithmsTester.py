from ArrayList import ArrayList
from Sort import Sort
import math
import time

while(True):
    while(True):
        try:
            numOfItems = int(input("How many items would you like to contain in the list? "))
            if(numOfItems <= 0):
                print("Number of items must be greater than 0")
                continue
            else:
                break
        except ValueError:
            print("Must be of type integer")
            continue

    listOfItems = ArrayList(numOfItems)

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

    switch = {1: listOfItems.sortList,
              2: listOfItems.reverseSortList,
              3: listOfItems.semiSortList
              }

    if(selection != 4):
        switch[selection]()

    print(listOfItems.items)

    while(True):
        try:
            print("What sort would you like to implement?: "
                  "\n1. Insertion Sort\n2. Selection Sort\n3. Quick Sort\n4. Merge Sort")
            selection = int(input("Please enter number corresponding to selection: "))
            if(selection < 1 or selection > 4):
                print("Please enter a number from the selection")
                continue
            else:
                break
        except ValueError:
            print("Must be of type integer")
            continue
    sort = Sort()

    switch = {1: sort.insertionSort,
              2: sort.selectionSort,
              3: sort.quickSort,
              4: sort.mergeSort
              }

    startTime = time.time()
    if(selection == 3 or selection == 4):
        switch[selection](listOfItems.items, 0, len(listOfItems.items)-1)
    else:
        switch[selection](listOfItems.items)
    elapsedTime = time.time() - startTime
    print(elapsedTime)
    print("After Sort" + str(listOfItems.items))
    print("# of compares: " + str(sort.counters["compareCounter"]) + "  # of swaps: " +
          str(sort.counters["swapCounter"]) + "  Time taken: " + str(elapsedTime) + "\n")
