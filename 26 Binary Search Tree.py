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

    def maxval(self, node):
        maxval = node
        while maxval.right is not None:
            maxval = maxval.right
        
        return maxval

    def minval(self, node):
            minval = node
            while minval.left is not None:
                minval = minval.left
            
            return minval
    
    def delete(self, data):
        self.root = self.recursivedelete(root=self.root, data=data)
    
    def recursivedelete(self, root, data):
        if root is None:
            return None
        
        if data < root.item:
            root.left = self.recursivedelete(root=root.left, data=data)
        
        elif data > root.item:
            root.right = self.recursivedelete(root=root.right, data=data)
        
        else:
            if root.left is None:
                return root.right
            
            elif root.right is None:
                return root.left
            
            # Find successor (min in right subtree) and replace
            successor = self.minval(root.right)
            root.item = successor.item  # Extract the item value, not the node
            root.right = self.recursivedelete(root.right, successor.item)  # Update the subtree
    
        return root

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
bst.insert(26)

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
# bst.preOrderRecursion()
##ROOT NODE IS NOT GETTING DELETED PROPERLY