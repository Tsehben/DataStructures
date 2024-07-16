
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
        current = self.head
        length = 0
        while current:
            length += 1
            current = current.next
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
        if index < 0 or index >= self.getLength():
            print("Out of Bounds")
            return
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
        prev = None
        current = self.head
        while current.next:
            prev = current
            current = current.next
        prev.next = None

    def deleteAtIndex(self, index):
        if index < 0:
            print("Index must be a non-negative integer")
            return

        if index == 0:
            if self.head:
                self.head = self.head.next
            else:
                print("Index out of bounds")
            return

        current = self.head
        prev = None
        index_v = 0

        while current:
            if index_v == index:
                if prev:
                    prev.next = current.next
                return
            prev = current
            current = current.next
            index_v += 1

        
        print("Index out of bounds")

        # search the linkedList  
    def findIndex(self, index):
        count_index = 0 
        current = self.head
        if index < 0 or index >= self.getLength():
            print("index out of range")
            return
        while current:
            if index == count_index:
                print(current.value)
                return
            current = current.next
            count_index += 1
        return
    def findValue(self, value):
        count = 0
        current = self.head
        while current:
            if current.value == value:
                print(f"Index is {count}")
                return
            current = current.next
            count += 1
        print("Element not found ")
        return
    def isEmpty(self):
        current = self.head
        if not current:
            print("List is Empty")
        else:
            print("List Not Empty")
        return
    def Clear(self):
        
       
        self.head = None
        return
    def reverseList(self):
        prev = None
        current = self.head

        while current:
            tempNext = current.next
            current.next = prev
            prev = current
            current = tempNext
        self.head = prev
            


ll1 = LinkedList()
ll1.addToBeginning(12)
ll1.addToBeginning(13)
ll1.addToBeginning(14)
ll1.addToEnd(34)
ll1.addToEnd(19)

ll1.addToEnd(36)
# ll1.deleteAtIndex(5)

ll1.printList()
ll1.findIndex(4)
ll1.findValue(13)
ll1.reverseList()
print(ll1.getLength())

ll1.printList()



   



        

       


