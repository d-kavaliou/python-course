class Node:
#класс который создается для узлов
    def __init__(self, data):
        #для головы узел устанавливается значение data
        self.data = data
        #для следующего узла устанавливается значение none
        self.next = None

class LinkedList:
    def __init__(self):
        #создаем пустой односвязный список
        self.head = None

    def append(self, data):
        #создаем новый узел с информацией
        new_node = Node(data)
        #если self.head => none => false и с not => true
        if not self.head:
            #то голова с новым узлом
            self.head = new_node
            return  
        #последний узел - новый узел
        last_node = self.head
        #пока последний узел не пустой
        while last_node.next:
            #переходим в конец списка
            last_node = last_node.next
            #вставляем туда новый элемент
        last_node.next = new_node   
    def print_reverse(self, node):
        if node is None:
            return
        self.print_reverse(node.next)
        print(node.data)

llist = LinkedList()
llist.append(1)
llist.append(2)
llist.append(3)
llist.append(4)


llist.print_reverse(llist.head)

