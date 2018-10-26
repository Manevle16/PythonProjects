import math

class Sort:
    """insertionSort"""

    def __init__(this):
        this.counters = { "compareCounter": 0, "swapCounter": 0 }

    def insertionSort(this, items):
        for i in range(1, len(items)):
            j = i
            while(j > 0):
                this.counters["compareCounter"] += 1
                if(items[j] < items[j - 1]):
                    this.counters["swapCounter"] += 1
                    temp = items[j-1]
                    items[j-1] = items[j]
                    items[j] = temp              
                j -= 1
    
    def selectionSort(this, items):
        for i in range(len(items)):
            min = math.inf
            minIndex = 0
            for j in range(i, len(items)):
                this.counters["compareCounter"] +=1
                if(items[j] < min):
                    min = items[j]
                    minIndex = j
            this.counters["swapCounter"] +=1
            temp = items[i]
            items[i] = items[minIndex]
            items[minIndex] = temp

    def quickSort(this, items, startInd, endInd):
        this.counters["compareCounter"] +=1
        if(startInd < endInd):
             pivot = items[endInd]

             i = startInd - 1

             for j in range(startInd, endInd):
                 this.counters["compareCounter"] +=1
                 if(items[j] <= pivot):
                     this.counters["swapCounter"] +=1
                     i += 1
                     temp = items[i]
                     items[i] = items[j]
             this.counters["swapCounter"] +=1
             temp = items[endInd]
             items[endInd] = items[i+1]
             items[i+1] = temp
             partInd = i + 1
             this.quickSort(items, startInd, partInd - 1)
             this.quickSort(items, partInd + 1, endInd)

    def mergeSort(this, items, left, right):
        this.counters["compareCounter"] +=1
        if(right > left):
            mid = int((left + right)/2)
            this.mergeSort(items, left, mid)
            this.mergeSort(items, mid+1, right)

            n1 = mid - left + 1
            n2 = right - mid
            
            lArr = items[left:n1+left]
            rArr = items[mid+1:mid+1++n2]

            i=0
            j=0
            k=left

            this.counters["compareCounter"] +=1
            while(i < n1 and j < n2):
                this.counters["compareCounter"] +=1
                if(lArr[i] <= rArr[j]):
                    this.counters["swapCounter"] +=1
                    items[k] = lArr[i]
                    i += 1
                else:
                    this.counters["swapCounter"] +=1
                    items[k] = rArr[j]
                    j += 1
                k += 1
                this.counters["compareCounter"] +=1

            this.counters["compareCounter"] +=1
            while(i < n1):
                this.counters["swapCounter"] +=1
                items[k] = lArr[i]
                i += 1
                k += 1
                this.counters["compareCounter"] +=1

            this.counters["compareCounter"] +=1
            while(j < n2):
                this.counters["swapCounter"] +=1
                items[k] = rArr[j]
                j += 1
                k += 1
                this.counters["compareCounter"] +=1

    

