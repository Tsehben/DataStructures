
# Node Class
class ListNode():
    def __init__(self, value):
        self.value = value
        self.next = None

# linked List class
class LinkedList():
    def __init__(self):
        self.head = None

    def printList(self):
        current = self.head
        while current:
            print(current.value,'-->' if current.next is not None else '', end='')
            current = current.next
        
        print()
    def getLength(self):
        length = 0
        while self.head:
            length += 1
            self.head = self.head.next
        return length

    def addToBeginning(self,value):
        newNode = ListNode(value)
        newNode.next = self.head
        self.head = newNode

    def addToEnd(self, value):
        current = self.head
        newNode = ListNode(value)
        while current.next:
            current = current.next
        current.next = newNode
        

    def addAtIndex(self, index, value):
        if index == 0:
            self.addToBeginning(value)
            return

        current = self.head
        prev = None
        index_v = 0

        while current:
            if index_v == index:
                new_node = ListNode(value)
                prev.next = new_node
                new_node.next = current
                return
            prev = current
            current = current.next
            index_v += 1

        if index_v == index:  
            new_node = ListNode(value)
            prev.next = new_node


    # Deletion
    def deleteFirst(self):
        current = self.head
        dummy = ListNode(None)
        dummy.next = current.next
        self.head = dummy.next
    
    def deleteLast(self):
        pass



ll1 = LinkedList()
ll1.addToBeginning(12)
ll1.addToBeginning(13)
ll1.addToBeginning(14)
ll1.addToEnd(34)
ll1.addToEnd(19)
ll1.addToEnd(36)
ll1.deleteFirst()

# ll1.addAtIndex(23,0)
# ll1.addAtIndex(23,8)
ll1.printList()
print(ll1.getLength())

   



        

       


