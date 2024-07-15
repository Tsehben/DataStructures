
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
        original = self.head
        while self.head:
            print(self.head.value,'-->' if self.head.next is not None else '', end='')
            self.head = self.head.next
        self.head = original
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
        original = self.head
        newNode = ListNode(value)
        while self.head.next:
            self.head = self.head.next
        self.head.next = newNode
        self.head = original

    def addAtIndex(self,value, index):
        original = self.head
        for _ in range(index):
            prev = self.head
            self.head = self.head.next
        prev.next = ListNode(value)
        self.head.next 

    

ll1 = LinkedList()
ll1.addToBeginning(12)
ll1.addToBeginning(13)
ll1.addToBeginning(14)
ll1.addToEnd(34)
ll1.printList()
print(ll1.getLength())

   



        

       


