def Bubble(array):
    for i in range(len(array)):
        for j in range(len(array)-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
        
        print(f"Pass {i+1}  Array: {array}")

    print(f"Sorted Array: {array}")


def modifiedBubble(array):
    for i in range(len(array)):
        swap = False
        for j in range(len(array)-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
            
                if not swap:
                    swap = True
        
        print(f"Pass {i+1}  Array: {array}")
        if not swap:
            break

    print(f"Sorted Array: {array}")


if __name__ == "__main__":
    items = [1, 5, 6, 15, 54, 24, 2, 3, 78, 65, 25]
    # Bubble(array=items)
    modifiedBubble(array=items)