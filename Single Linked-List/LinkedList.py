class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
    def __repr__(self):
        return str(self.data)
class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        return ' -> '.join([str(node) for node in self])
    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("Previous node does not exist")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def append(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        else:
            self.tail.next = node
        self.tail = node
    def delete_by_value(self, data):
        if not self.head:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next and current.next.data != data:
            current = current.next
        if current.next:
            current.next = current.next.next

    def delete_at_pos(self, pos):
        cur_node = self.head
        if pos == 0:
            self.head = cur_node.next
            cur_node = None
            return
        prev = None
        count = 0
        while cur_node and count != pos:
            prev = cur_node
            cur_node = cur_node.next
            count += 1
        if cur_node is None:
            return
        prev.next = cur_node.next
        cur_node = None

    def find_index(self, value):
        current = self.head
        index = 0
        while current:
            if current.data == value:
                return index
            current = current.next
            index += 1
        return -1
    def delete(self):
        item_id = int(input("Welches Element sollte gelöscht werden?: "))
        self.delete_at_pos(item_id)
        print(self)
    def search(self):
        item_value = int(input("Welches Element soll gesucht werdne?: "))
        print(self.find_index(item_value))

    def swap_data(self, first, second):
        first.data, second.data = second.data, first.data
    def insertionSortASC(self):
        front = self.head
        while front is not None:
            back = front.next
            while back is not None and back.prev is not None and back.data < back.prev.data:
                back.data, back.prev.data = back.prev.data, back.data
                back = back.prev
            front = front.next

    def insertionSortDesc(self):
        front = self.head
        back = None
        while front is not None:
            back = front.next
            while back is not None and back.prev is not None and back.data > back.prev.data:
                self.swap_data(back, back.prev)
                back = back.prev
            front = front.next
    def menu(self):
        repeat = True
        answer = None
        while(repeat):
            answer = input("Löschen [l] - Suche [s] - Einfügen nachher [a] - Einfügen davor [b] "
                           "- Knoten danach entfernen [d] - Knoten davor entfernen [v] \n - "
                           "Sortieren ASC [o] - Sortieren DESC [u] - Beenden [any] ").lower()
            if answer == "l":
                self.delete()
            elif answer == "s":
                self.search()
            elif answer == "a":
                self.insert_after_node()
            else:
                repeat = False
                print("leaving ....")

