mylist = [58, 62, 91, 43, 29, 37, 88, 72, 16, 30]

left = 0
right = len(mylist)
loc = 0


def locToRight():
    while mylist[loc] < mylist[right]:
        right-=1
    
    mylist[loc], mylist[right] = mylist[right], mylist[loc]
    right-=1
    loc = right
    leftToLoc()

def leftToLoc():
    while mylist[left] < mylist[loc]:
        left+=1

    mylist[loc], mylist[left] = mylist[left], mylist[loc]
    left+=1
    loc = left
    locToRight()


def QuickSort():
    locToRight()

if __name__ == "__main__":
    QuickSort()
    print(mylist)