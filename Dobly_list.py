class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
        self.prev=None


class Doubly_llist:
    def __init__(self):
        self.head=None

    def inserthead(self, node):
        temp = self.head
        self.head=node
        self.head.next=temp
        if temp is not None:
            temp.prev=self.head
        del temp

    def deletehead(self):
        if self.head is None:
            return
        else:
            self.head=self.head.next

    def deleteend(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head=None
            return
        cur=self.head
        temp=None
        while cur.next is not None:
            cur=cur.next
            temp=cur.prev
        temp.next=None

    def insertend(self,node):
        if self.head is None:
            self.head=node
            return
        current=self.head
        while True:
            if current.next is None:
                break
            current=current.next
        current.next=node
        node.next=None
        node.prev=current

    def rev(self):
        temp=None
        cur=self.head
        while cur is not None:
            temp=cur.next
            cur.next=cur.prev
            cur.prev=temp
            cur=cur.prev
            if temp is not None:
                self.head=temp

    def printList(self):
        if self.head is None:
            print("Empty!")
            return
        currentNode=self.head
        while currentNode is not None:
            print(currentNode.data)
            currentNode=currentNode.next

if __name__ == '__main__':
    d=Doubly_llist()
    node = Node("45")
    d.inserthead(node)
    node = Node("5")
    d.inserthead(node)
    node = Node("0045")
    d.insertend(node)
    d.printList()
    #d.deleteend()
    print("________")
    #d.rev()
    #print("After removing head:")
    d.deletehead()
    d.rev()
    d.printList()