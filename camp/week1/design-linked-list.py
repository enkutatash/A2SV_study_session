class Node:
    def __init__(self,val=0):
        self.val=val
        self.next=None
class MyLinkedList:

    def __init__(self):
        self.head=Node()
        self.tail=None
        

    def get(self, index: int) -> int:
        i=0
        curr=self.head.next
        while curr:
            if i==index:
                return curr.val
            i+=1
            curr=curr.next
        return -1
        

    def addAtHead(self, val: int) -> None:
        newNode=Node(val) 
        newNode.next=self.head.next
        self.head.next=newNode
        if self.tail==None:
            self.tail=newNode

        

    def addAtTail(self, val: int) -> None:
        newNode=Node(val)
        if self.head.next==None:
            self.head.next=newNode
            self.tail=newNode
        else:
            self.tail.next=newNode
            self.tail=newNode
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index==0:
            self.addAtHead(val)
            return
        newNode=Node(val)
        i=0
        curr=self.head.next
        prev=curr
        while curr:
            if i==index:
                temp=prev.next
                prev.next=newNode
                newNode.next=temp
                return 
            i+=1
            prev=curr
            curr=curr.next
        if i==index:
            self.tail=newNode
            prev.next=newNode

            return
        

    def deleteAtIndex(self, index: int) -> None:
        i=0
        curr=self.head.next
        prev=curr
        if index==0:
            self.head.next=self.head.next.next
        else:
            while curr:
                if i==index:
                    prev.next=curr.next
                    if curr.next==None:
                        self.tail=prev
                    return 
                i+=1
                prev=curr
                curr=curr.next
        
        return
    

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)