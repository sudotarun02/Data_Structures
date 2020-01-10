class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList():
    def __init__(self):
        self.head = None

    def insert_head(self, node):
        newnode=Node(node)
        if self.head is None:
            self.head = newnode
            self.head.next = self.head
        else:
            temp = self.head
            self.head = newnode
            self.head.next = temp
            temp.next = self.head
            del temp

    def insert_end(self, newnode):
        if self.head is None:
            self.head = newnode
            self.head.next = self.head
        else:
            last = self.head
            while True:
                if last.next is self.head:
                    break
                last = last.next
            last.next = newnode
            newnode.next = self.head

    def delete(self, node):
        if self.head is None:
            return
        temp = self.head
        while True:
            if temp == node:
                break
        temp = temp.next

    def print_list(self):
        if self.head is None:
            print("Empty")
            return
        print(self.head.data)
        current = self.head.next
        while True:
            if current is self.head:
                break
            print(current.data)
            current = current.next


if __name__ == '__main__':
    c = LinkedList()
    c.insert_head("45")
    c.print_list()
