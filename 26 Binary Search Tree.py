class Node:
    def __init__(self, left=None, item=None, right=None):
        self.item = item
        self.left = left
        self.right = right

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        if self.root is None:
            newNode = Node(item=data)
            self.root = newNode
        
        else:
            temp = self.root
            while True:
                if temp.item == data:
                    print("DUPLICATE VALUES ARE NOT ALLOWED")
                    break

                elif data < temp.item:
                    if temp.left is None:
                        newNode = Node(item=data)
                        temp.left = newNode
                        break

                    else:
                        temp = temp.left

                elif data > temp.item:
                    if temp.right is None:
                        newNode = Node(item=data)
                        temp.right = newNode
                        break

                    else:
                        temp = temp.right
    

    def search(self, data):
        if self.root is None:
            return None
        
        else:
            temp = self.root
            
            while temp is not None:
                if data == temp.item:
                    return temp
                
                elif data > temp.item:
                    temp = temp.right
                
                elif data < temp.item:
                    temp = temp.left

            return None
        
    #InOrder Traveresal with Recursion
    def inOrderRecursion(self, node=None):
        
        if self.root is None:
            return "Tree is Empty"
        if node:
            if node.left is not None and node.right is not None:
                self.inOrderRecursion(node=node.left)
                print(node.item)
                self.inOrderRecursion(node=node.right)
            
            elif node.left is not None and node.right is None:
                self.inOrderRecursion(node=node.left)
                print(node.item)
                return
        
            elif node.left is None and node.right is not None:
                print(node.item)
                self.inOrderRecursion(node=node.right)

            else:
                print(node.item)
            
        
        elif node is None:
            self.inOrderRecursion(node=self.root)
    
    #PreOrder Traversal with Recursionk
    def preOrderRecursion(self, node=None):
        if self.root is None:
            return None
        
        if node:
            if node.left is not None and node.right is not None:
                print(node.item)
                self.preOrderRecursion(node=node.left)
                self.preOrderRecursion(node=node.right)

            elif node.left is None and node.right is not None:
                print(node.item)
                self.preOrderRecursion(node=node.right)

            elif node.left is not None and node.right is None:
                self.preOrderRecursion(node=node.left)
                print(node.item)

            elif node.left is None and node.right is None:
                print(node.item)

        elif node is None:
            self.preOrderRecursion(node=self.root)

    #PostOrder Traversal with Recursion
    def postOrderRecursion(self, node=None):
            if self.root is None:
                return None
            
            if node:
                if node.left is not None and node.right is not None:
                    self.postOrderRecursion(node=node.left)
                    self.postOrderRecursion(node=node.right)
                    print(node.item)

                elif node.left is None and node.right is not None:
                    self.postOrderRecursion(node=node.right)
                    print(node.item)

                elif node.left is not None and node.right is None:
                    print(node.item)
                    self.postOrderRecursion(node=node.left)

                elif node.left is None and node.right is None:
                    print(node.item)

            elif node is None:
                self.postOrderRecursion(node=self.root)
    
    def delete(self, data):
        node = self.search(data=data)
        if node is None:
            print("Node is not found in the Tree !!!!")
        
        else:
            parent = self.root
            while True:
                if parent.right == node or parent.left == node:
                    break
            
                elif parent.item > data:
                    parent = parent.left

                elif parent.item < data:
                    parent = parent.right
                
                elif parent.item == data:
                    print("ROOT NODE IS SELECTED")
                    break
        
            if node.left is None and node.right is None:
                if parent.left == node:
                    parent.left = None
                
                else:
                    parent.right = None
        
            elif node.left is not None and node.right is None:
                predeces = self.predecessor(node)
                print(predeces.item)
                parent.left = predeces

            elif node.left is None and node.right is not None:
                sucessor = self.successor(node)
                print(sucessor.item)
                parent.right = sucessor

            else:
                predeces = self.predecessor(node)
                print(predeces.item)
                predeces.right = node.right
                if parent.left == node:
                    parent.left = predeces
                
                else:
                    parent.right = predeces
    

    def predecessor(self, node):
        prede = node.left
        while prede.right is not None:
            prede = prede.right
        
        return prede

    def successor(self, node):
        prede = node.right
        while prede.left is not None:
            prede = prede.left
        
        return prede
            
            
            
            



bst = BST()
bst.insert(30)
bst.insert(20)
bst.insert(15)
bst.insert(25)
bst.insert(45)
bst.insert(70)
bst.insert(40)
bst.insert(100)
bst.insert(27)  
bst.insert(22)
bst.insert(10)

# print(bst.search(20))

# print("InOrder Traversing with Recursion")
# bst.inOrderRecursion()

# print("PreOrder Traversing with Recursion")
# bst.preOrderRecursion()

# print("PostOrder Traversing with Recursion")
# bst.postOrderRecursion()


bst.delete(30)
print("InOrder Traversing with Recursion")
bst.inOrderRecursion()


##ROOT NODE IS NOT GETTING DELETED PROPERLY