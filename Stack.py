class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

class Stack:
    def __init__(self):
        self.head=None

    def push(self, newnode):
        if self.head is None:
            self.head=newnode
        else:
            lastnode=self.head
            while True:
                if lastnode.next is None:
                    break
                lastnode=lastnode.next
            lastnode.next=newnode

    def pop(self):
        if self.head is None:
            print("Empty Stack!")
            return
        else:
            prev=self.head
            while prev.next is not None:
                current=prev
                prev=prev.next
            current.next=None

    def print(self):
        if self.head is None:
            print("Empty!")
            return
        currentNode=self.head
        while True:
            if currentNode is None:
                break
            print(currentNode.data)
            currentNode=currentNode.next

if __name__=='__main__':
    s=Stack()
    exp=input("Entre the experssion:")
    l = len(exp)
    i = 0
    while (i < l):
        ch = exp[i]
        s.push(ch)
        i = i + 1
    s.print()
