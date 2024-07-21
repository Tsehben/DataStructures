class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def add_child(self, value):
        if value == self.data:
            return
        if value < self.data:
            if self.left:
                self.left.add_child(value)
            else:
                self.left = BinarySearchTreeNode(value)
        elif value > self.data:
            if self.right:
                self.right.add_child(value)
            else:
                self.right = BinarySearchTreeNode(value)
          
    # inorder traversal 

    def inorder_traversal(self):
        elements = []
        # add left 
        if self.left:
            elements += self.left.inorder_traversal()
        # add base element
        elements.append(self.data)
        # add right
        if self.right:
            elements += self.right.inorder_traversal()

        return elements
    
    def search(self, value):
        if value == self.data:
            return True
        
        if value < self.data:
            if self.left:
                return self.left.search(value)
            else:
                return False
              
        if value > self.data:
            if self.right:
                return self.right.search(value)
            else:
                return False
    
    # recursive approach        
    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()
    #iterative approach
    def find_max(self):
        curr = self

        while curr.right:
            curr = curr.right
        return curr.data
    
    def sum_tree(self):
        total = 0
        if self.left:
            total += self.left.sum_tree()
        
        total += self.data

        if self.right:
            total += self.right.sum_tree()

        return total
    
    def postorder_traversal(self):
        elements = []

        # add left
        if self.left:
            elements += self.left.postorder_traversal()
        # add right
        if self.right:
            elements += self.right.postorder_traversal()
        # add root
        elements.append(self.data)

        return elements
    def preorder_traversal(self):

        elements = []

        elements.append(self.data)

        if self.left:
            elements += self.left.preorder_traversal()

        if self.right:
            elements += self.right.preorder_traversal()


        return elements

def build_tree(elements):

    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])
    
    return root


numbers = [19,4,3,12,2,13,7,2,9,8]
new_tree = build_tree(numbers)

print(new_tree.inorder_traversal())
print(new_tree.postorder_traversal())
print(new_tree.preorder_traversal())
print(new_tree.search(7))
print(new_tree.find_min())
print(new_tree.find_max())
print(new_tree.sum_tree())