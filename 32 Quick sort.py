mylist = [58, 69, 91, 43, 29, 37, 88, 72, 16, 30]


def locToRight(mylist, left, right, loc):

    print(f"\n\nlocToRight \n\tmylist:{mylist}\n\tLeft:{left}\n\tRight:{right}\n\tLoc:{loc}\n\t before checking")

    while mylist[loc]<mylist[right]:
        right-=1
        if right<=left:
            QuickSort(quicklist=mylist[:loc])
            QuickSort(quicklist=mylist[loc:])

    mylist[loc], mylist[right] = mylist[right], mylist[loc]
    loc = right

    if len(mylist) <= 2:
        return

    leftToLoc(mylist=mylist, left=left, right=right, loc=loc)

def leftToLoc(mylist, left, right, loc):
    
    print(f"\n\nleftToLoc \n\tmylist:{mylist}\n\tLeft:{left}\n\tRight:{right}\n\tLoc:{loc}\n\t before checking")
    
    while mylist[left]<=mylist[loc]:
        left+=1
        if left>right:
            QuickSort(quicklist=mylist[:loc])
            QuickSort(quicklist=mylist[loc:])

    mylist[left], mylist[loc] = mylist[loc], mylist[left]
    loc = left

    if len(mylist) <= 2:
        return

    locToRight(mylist=mylist, left=left, right=right, loc=loc)

            

def QuickSort(quicklist):
    left = 0
    loc = 0
    right = len(quicklist)-1

    locToRight(mylist=quicklist, left=left, right=right, loc=0)


if __name__ == "__main__":
    QuickSort(mylist)