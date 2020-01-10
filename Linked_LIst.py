class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def list_length(self):
        length = 0
        current = self.head
        while current is not None:
            current = current.next
            length += 1
        return length

    def insert_end(self, newNode):
        if self.head is None:
            self.head = newNode
        else:
            lastNode = self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.next
            lastNode.next = newNode

    def insertHead(self, newNode):
        temp = self.head
        self.head = newNode
        self.head.next = temp
        del temp

    def removeLast(self):
        if self.head is None:
            print("Empty")
            return
        prev = self.head
        while prev.next is not None:
            current = prev
            prev = prev.next
        current.next = None

    def insertAt(self, newNode, at):
        if at == 0:
            self.insertHead(newNode)
            return
        current = self.head
        position = 0
        while True:
            if position == at:
                temp.next = newNode
                newNode.next = current
                break
            temp = current
            current = current.next
            position += 1

    def deleteHead(self):
        if self.head is None:
            print("Head is empty!")
            return
        self.head = self.head.next

    def deleteAt(self, at):
        if at == 0:
            self.head = None
            return
        position = 0
        prev = self.head
        current = self.head
        while True:
            if at == position:
                prev.next = current.next
                return
            position += 1
            prev = current
            current = current.next

    def delete_list(self):
        self.head = None

    def rev(self):
        if self.head is None:
            return
        cur = self.head
        prev = None
        temp = None
        while cur is not None:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        self.head = prev

    def printList(self):
        if self.head is None:
            print("Empty!")
            return
        currentNode = self.head
        while True:
            if currentNode is None:
                break
            print(currentNode.data)
            currentNode = currentNode.next


if __name__ == '__main__':
    ll = LinkedList()
    node = Node("45")
    ll.insert_end(node)
    c = Node("23")
    ll.insert_end(c)
    node1 = Node("Hello")
    ll.insert_end(node1)
    a = Node("13")
    ll.insertHead(a)
    # ll.removeLast()
    ll.deleteHead()
    b = Node("32")
    ll.insertAt(b, 1)
    ll.deleteAt(2)
    # ll.delete_list()
    # print(ll.listLength())
    ll.printList()
    ll.rev()
    print("----------")
    ll.printList()
