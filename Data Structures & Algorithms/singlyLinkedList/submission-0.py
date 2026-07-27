class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.head = None
    
    def get(self, index: int) -> int:
        cur = self.head
        for i in range(index):
            if cur is None:
                return -1
            cur = cur.next
        return cur.val if cur else -1

    def insertHead(self, val: int) -> None:
        node = ListNode(val)
        node.next = self.head
        self.head = node
        

    def insertTail(self, val: int) -> None:
        if self.head == None:
            self.insertHead(val)
            return
        cur = self.head
        node = ListNode(val)
        while cur.next != None:
            cur = cur.next
        cur.next = node

    def remove(self, index: int) -> bool:
        if self.head == None:
            return False
        if index == 0:
            self.head = self.head.next
            return True
        cur = self.head
        for i in range(index - 1):
            if cur.next == None:
                return False
            cur = cur.next
        
        if cur.next == None:
            return False

        cur.next = cur.next.next
        return True

    def getValues(self) -> List[int]:
        listvals = []
        cur = self.head
        while cur != None:
            listvals.append(cur.val)
            cur = cur.next
        return listvals