class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def len_iterative(self):
        count = 0
        cur_node = self.head
        while cur_node:
            count += 1
            cur_node = cur_node.next
        return count 

    def move_tail_to_head(self):

        k = 0
        cur_node = self.head
        while cur_node:
            k += 1
            cur_node = cur_node.next
        k = k-1

        if self.head and self.head.next:
            p = self.head 
            q = self.head 
            prev = None
            count = 0
    
        while p and count < k:
            prev = p
            p = p.next 
            q = q.next 
            count += 1
        p = prev
        while q:
            prev = q 
            q = q.next 
        q = prev 

        q.next = self.head 
        self.head = p.next 
        p.next = None



llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")

llist.print_list()
 
llist.move_tail_to_head()

llist.print_list()

