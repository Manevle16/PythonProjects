class Sort:
    """insertionSort"""

    def insertionSort(listOfItems):
        counters = { "compareCounter": 0, "swapCounter": 0 }

        for i in range(1, len(listOfItems)):
            j = i
            while(j > 0):
                counters["compareCounter"] += 1
                if(listOfItems[j] < listOfItems[j - 1]):
                    counters["swapCounter"] += 1
                    temp = listOfItems[j-1]
                    listOfItems[j-1] = listOfItems[j]
                    listOfItems[j] = temp              
                j -= 1
        return counters


