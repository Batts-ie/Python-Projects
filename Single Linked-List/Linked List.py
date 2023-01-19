class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_head(self, data):
        new_node = Node(data, self.head)
        self.head = new_node

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(data)

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

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

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
