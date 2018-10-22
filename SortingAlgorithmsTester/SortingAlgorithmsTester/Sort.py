import math

class Sort:
    """insertionSort"""

    def insertionSort(items):
        counters = { "compareCounter": 0, "swapCounter": 0 }

        for i in range(1, len(items)):
            j = i
            while(j > 0):
                counters["compareCounter"] += 1
                if(items[j] < items[j - 1]):
                    counters["swapCounter"] += 1
                    temp = items[j-1]
                    items[j-1] = items[j]
                    items[j] = temp              
                j -= 1
        return counters
    
    def selectionSort(items):
        counters = { "compareCounter": 0, "swapCounter": 0 }


        for i in range(len(items)):
            min = math.inf
            minIndex = 0
            for j in range(i, len(items)):
                counters["compareCounter"] +=1
                if(items[j] < min):
                    min = items[j]
                    minIndex = j
            counters["swapCounter"] +=1
            temp = items[i]
            items[i] = items[minIndex]
            items[minIndex] = temp


