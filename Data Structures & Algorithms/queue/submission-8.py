class Node:
    def __init__(self, val, next, prev):
        self.val = val
        self.next = next
        self.prev = prev

class Deque:
    
    def __init__(self):
        self.head: Node = None
        self.tail: Node = None
        self.size = 0
        

    def isEmpty(self) -> bool:
        return True if self.size == 0 else False
        

    def append(self, value: int) -> None:
        if self.size == 0:
            self.head = Node(val=value, next=None, prev=None)
            self.tail = self.head
        elif self.size == 1:
            newTail = Node(val=value, next=None, prev=self.head)
            self.head.next = newTail
            newTail.prev = self.head
            self.tail = newTail #audit up to here
        else:
            newTail = Node(val=value, next=None, prev=self.tail)
            self.tail.next = newTail
            newTail.prev = self.tail
            self.tail = newTail
        
        self.size+=1
        return
        

    def appendleft(self, value: int) -> None: #add at head
        if self.size == 0:
            self.head = Node(val=value, next=None, prev=None)
            self.tail = self.head
        elif self.size == 1:
            newHead = Node(val=value, next=self.head, prev=None)
            self.head.prev = newHead
            self.tail = self.head
            self.head = newHead
            
        else:
            newHead = Node(val=value, next=self.head, prev=None)
            self.head.prev = newHead
            self.head = newHead
    
        self.size+=1
        return

    def pop(self) -> int: #removal from tail
        if self.size == 0:
            return -1
        if self.size == 1:
            retVal = self.tail.val
            self.head = None
            self.tail = None
            self.size-=1
            return retVal
        
        
        retVal = self.tail.val
        newTail = self.tail.prev
        self.tail.prev = None
        newTail.next = None
        self.tail = newTail
        
        self.size-=1
        print("popping value: {}".format(retVal))
        return retVal
        
        

    def popleft(self) -> int: #removal from head
        if self.size == 0:
            return -1
        if self.size == 1:
            retVal = self.head.val
            self.head = None
            self.tail = None
            self.size-=1
            return retVal
        
        retVal = self.head.val
        newHead = self.head.next
        self.head.next = None
        newHead.prev = None
        self.head = newHead

        self.size-=1
        
        return retVal
