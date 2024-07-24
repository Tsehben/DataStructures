from collections import deque
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
    def delete(self, value):
        # base case, if there is no element return None
        if not self:
            return None
        
        #if value less than root node, recurse left till we find the value if it exists
        if value < self.data:
            if self.left:
                self.left = self.left.delete(value)
        # if value is greater than current node, recurse right
        elif value > self.data:
            if self.right:
                self.right = self.right.delete(value)

        # at this point it  means we have found the elemene
        else:
            # case one with zero or one node
            if self.left is None: 
                return self.right
            elif self.right is None:
                return self.left
            # case with two nodes(children)
            else:
                min_node = self.right.find_min()
                self.data = min_node.data
                self.right = self.right.delete(min_node.data)

        return self

    def bfs(self):
        elements = []
        queue = deque()
        if self:
            queue.append(self)
        
        while len(queue) > 0:
            
            for i in range(len(queue)):
                curr = queue.popleft()
                elements.append(curr.data)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)



        return elements
    def levelOrder(self):

        res = []
        level_nodes = [self]
        level_values =[]
        next_level_nodes = []

        if not self:
            return []

        while level_nodes:
            for node in level_nodes:
                level_values.append(node.data)
                if node.left:
                    next_level_nodes.append(node.left)
                if node.right:
                    next_level_nodes.append(node.right)


            res.append(level_values)
            level_nodes = next_level_nodes

            level_values = []
            next_level_nodes = []
        return res





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
print(new_tree.delete(80))
print(new_tree.inorder_traversal())
print(new_tree.bfs())
print(new_tree.levelOrder())