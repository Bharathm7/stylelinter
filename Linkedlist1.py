class node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None


def circular(head):
    if head == None:
        return False
    node = head.next
    i = 0

    while (node is not None) and (node is not head):
        i = i + 1
        node = node.next
    return node == head


ll = Linkedlist()
ll.head = node(1)
second = node(2)
third = node(3)
fourth = node(4)

ll.head.next = second
second.next = third
third.next = fourth


if circular(ll.head):
    print("yes")
else:
    print("NO")
