from node import Node
from linked_list import LinkedList


class Cache:
    def __init__(self, MAX_SIZE):
        self.MAX_SIZE = MAX_SIZE
        self.size = 0
        self.lookup = {}
        self.linked_list = LinkedList()

    def get_data(self, query):
        exist = self.lookup.get(query)

        if exist is None:
            return None

        node = self.linked_list.find_node(query)
        self.linked_list.move_to_front(node)
        return exist

    def set_data(self, query, result):
        exist = self.lookup.get(query)

        if exist is not None:
            node = self.linked_list.find_node(query)
            self.lookup[query] = result
            self.linked_list.move_to_front(node)
        else:
            if self.size == self.MAX_SIZE:
                self.lookup.pop(self.linked_list.tail.query, None)
                self.linked_list.remove_from_tail()
            else:
                self.size += 1

            new_node = Node(query)
            self.linked_list.append_to_front(new_node)
            self.lookup[query] = result


if __name__ == '__main__':
    cache = Cache(3)
    cache.set_data("first", 1)
    cache.set_data("second", 2)
    cache.set_data("third", 3)
    cache.set_data("fourth", 4)
    print(cache.get_data("first"))
    print(cache.get_data("second"))
    cache.set_data("fiver", 5)
    print(cache.get_data("second"))
    print(cache.get_data("fourth"))
    cache.set_data("sixth", 6)
    print(cache.lookup)  # cache should contain(sixth, fourth, second)
