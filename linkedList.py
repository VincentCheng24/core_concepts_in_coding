class LinkedList:

    def __init__(self):
        self.head = None

    def printList(self):
        p = self.head
        while p is not None:
            print(p.data)
            p = p.next

    def push(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node


    def deleteNode(self, key):

        cur = self.head

        if cur is not None:
            if cur.data == key:
                self.head = cur.next
                cur = None

        while cur is not None:
            if cur.data == key:
                break

            pre = cur
            cur = cur.next

        if cur is None:
            return

        pre.next = cur.next
        cur = None

    def reverseList(self):
        cur = self.head
        pre = None

        while cur is not None:
            nex = cur.next
            cur.next = pre
            pre = cur
            cur = nex

        self.head = pre


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


if __name__ == '__main__':

    # node1 = Node(1)
    # node2 = Node(2)
    # node3 = Node(3)
    #
    # lis = LinkedList()
    # lis.head = node1
    # node1.next = node2
    # node2.next = node3
    #
    # lis.printList()

    llist = LinkedList()
    llist.push(7)
    llist.push(1)
    llist.push(3)
    llist.push(2)

    print("Created Linked List: ")
    llist.printList()
    # llist.deleteNode(1)
    print( "\nLinked List after Deletion of 1:")
    # llist.printList()
    llist.reverseList()
    llist.printList()