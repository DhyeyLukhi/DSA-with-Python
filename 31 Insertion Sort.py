def sort(listArray, min, minIndex):
    crctIndex=0
    for i in range(len(listArray)):
        if min < listArray[i]:
            crctIndex = i
            break
    
    for j in range(crctIndex, minIndex+1):
        listArray[j], min = min, listArray[j]
    
    return listArray

def insertionSort(array):
    for index in range(1, len(array)):
        if array[index] < array[index-1]:
            newSorted = sort(array, array[index], index)
            

    print(f"Sorted Array: {array}")



if __name__ == "__main__":
    items = [12, 54, 84, 5, 2, 45, 69, 3, 65, 57, 24, 1, 4, 22]
    print(f"Unsorted array: {items}")
    insertionSort(array=items)