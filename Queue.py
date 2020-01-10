class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

class Queue:

    def __init__(self):
        self.head=None

    def push(self, new):
        if self.head is None:
            self.head=new
        else:
            temp=self.head
            while True:
                if temp.next is None:
                    break
                temp=temp.next
            temp.next=new

    def print_q(self):
        if self.head is None:
            print("None")
            return
        temp=self.head
        while True:
            if temp is None:
                break
            temp=temp.next

if __name__ == '__main__':
    q = Queue()
    node=Node("23")
    q.push(node)
    q.print_q()
