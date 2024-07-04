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
    
    def int_list(self):
        p = self.head
        s = ""
        while p:
            s = s + p.data
            p = p.next
        s = int(s[::-1])
        return s
    
    def two_sum(self,llist):
        a = self.int_list()
        b = llist.int_list()
        s = str(a+b)
        s = list(s[::-1])

        result = LinkedList()
        for i in s:
            result.append(i)
        return result.print_list()
        

    

llist1 = LinkedList()

llist1.append("5")
llist1.append("6")
llist1.append("3")


llist = LinkedList()

llist.append("8")
llist.append("4")
llist.append("2")

print(llist1.two_sum(llist))
