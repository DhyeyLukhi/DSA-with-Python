mylist = [79, 29, 83, 42, 16, 90, 56, 34, 20 ,71, 88, 92, 7]

newMergeList = []

def mergeSort(mergeList):
    if len(mergeList) >= 2:
        half = int(len(mergeList)/2)
        leftSide = mergeList[0:half]
        rightSide = mergeList[half:]

        mergeSort(leftSide)
        mergeSort(rightSide)


        i=j=k=0
        while i<len(leftSide) and j<len(rightSide):
            if leftSide[i] < rightSide[j]:
                mergeList[k] = leftSide[i]
                i+=1

            else:
                mergeList[k] = rightSide[j]
                j+=1
            
            k+=1

        while i<len(leftSide):
            mergeList[k] = leftSide[i]
            i+=1
            k+=1

        while j<len(rightSide):
            mergeList[k] = rightSide[j]
            j+=1
            k+=1
 
if __name__ == "__main__":
    mergeSort(mylist)
    print(mylist)