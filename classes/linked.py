class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    # def __repr__(self):
    #     return f"[{self.data}]->{self.next}"


class LinkedList:
    def __init__(self):
        self.head = None

    # def __str__(self):
    #     return str(self.head)


linkedlist = LinkedList()
temp = Node(1)
linkedlist.head = temp
for i in range(2, 6):
    temp.next = Node(i)
    temp = temp.next
print(linkedlist.head.next)
