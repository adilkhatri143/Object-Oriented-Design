from node import Node


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def move_to_front(self, node):
        temp = self.head
        before_temp = Node(0)
        while temp.link != None:
            before_temp = temp
            temp = temp.link

        if temp == self.head:
            return
        elif temp.link == None:
            before_temp.link = None
            temp.link = self.head
            self.head = temp
            self.tail = before_temp
        else:
            before_temp.link = temp.link
            temp.link = self.head
            self.head = temp

    def append_to_front(self, node):
        if self.tail == None and self.head == None:
            self.head = node
            self.tail = node
        else:
            node.link = self.head
            self.head = node

    def remove_from_tail(self):
        temp = self.head
        count = 1
        while temp.link != None and temp.link.link != None:
            temp = temp.link
            count += 1

        if count == 1:
            self.head = None
            self.tail = None
            return

        self.tail = temp
        del temp.link
        self.tail.link = None

    def find_node(self, query):
        temp = self.head
        while temp != None and temp.query != query:
            temp = temp.link

        return temp
