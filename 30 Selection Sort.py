def selection(array):
    for i in range(len(array)):
        min = array[i]
        for j in range(i, len(array)):
            if array[j] < min:
                min = array[j]
                index = j
        
        array[i], array[index] = array[index], array[i]
    
    print(f"Sorted array: {array}")


if __name__ == "__main__":
    items = [2, 4, 1, 45, 23, 63, 65, 3, 9, 36, 54, 8]
    selection(array=items)