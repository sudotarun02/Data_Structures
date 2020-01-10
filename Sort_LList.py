class Node:

    def __init__(self, data):
        self.data=data
        self.next=None


class Sort_LList:

    def __init__(self):
        self.head=None

    def push(self, node):
        newNode=Node(node)
        newNode.next=self.head
        self.head = newNode

    def append(self, node):
        newNode=Node(node)
        if self.head is None:
            self.head=newNode
        else:
            lastNode=self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode=lastNode.next
            lastNode.next=newNode

    def middle(self, head):
        if head is None:
            return head
        fast=head
        slow=head
        while fast.next is not None and fast.next.next is not None:
            slow=slow.next
            fast=fast.next.next
        mid=slow.next
        slow.next=None
        return head, mid

    def mergeSort(self, head):
        if head is None or head.next is None:
            return head
        left, right=self.middle(head)
        left=self.mergeSort(left)
        right=self.mergeSort(right)
        head=self.sorted(left, right)
        return head

    def sorted(self, left, right):
        result = None
        if left is None:
            return right
        if right is None:
            return left
        if left.data <= right.data:
            result = left
            result.next = self.sorted(left.next, right)
        else:
            result = right
            result.next = self.sorted(left, right.next)
        return result

    def printList(self):
        if self.head is None:
            print("Empty!")
            return
        currentNode=self.head
        while True:
            if currentNode is None:
                break
            print(currentNode.data,end=" -> ")
            currentNode=currentNode.next


if __name__ == '__main__':
    s = Sort_LList()
    s.push(465)
    s.push(45)
    s.push(0)
    s.push(-20)
    s.push(2.0)
    s.push(201)
    s.push(20)
    s.append(10)
    s.append(9)
    s.append(8)
    s.push(2)
    s.append(7)
    s.printList()
    print("")
    s.head=s.mergeSort(s.head)
    s.printList()