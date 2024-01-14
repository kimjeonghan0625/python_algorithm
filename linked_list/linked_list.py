class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        # example code
        if self.length == 0:
            return None
        pre = temp = self.head
        while temp.next is not None:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

        # my code
        # # head와 tail 모두 None인 경우
        # if self.length == 0:
        #     return None
        # # 노드가 하나밖에 없어서 head와 tail이 같은 경우
        # if self.head == self.tail:
        #     tmp = self.head
        #     self.head = None
        #     self.tail = None
        #     self.length -= 1
        #     return tmp
        # # 일반적인 경우
        # pre = temp = self.head
        # while True:
        #     temp = temp.next
        #     if temp.next == None:
        #         self.tail = pre
        #         self.tail.next = None
        #         self.length -= 1
        #         return temp
        #     pre = temp

        # target = None
        # tmp_node = self.head
        # while tmp_node.next:
        #     if tmp_node.next == self.tail:
        #         target = tmp_node
        #         pop_node = self.tail
        #         target.next = None
        #         self.tail = target
        #         return pop_node
        #     tmp_node = tmp_node.next

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp
        # if self.length == 0:
        #     return None
        # temp = self.head
        # if self.head.next == None:
        #     self.head = None
        #     self.tail = None
        # else:
        #     self.head = self.head.next
        # temp.next = None
        # self.length -= 1
        # return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False


my_linked_list = LinkedList(11)
my_linked_list.append(3)
my_linked_list.append(23)
my_linked_list.append(7)

my_linked_list.set_value(1, 4)
my_linked_list.print_list()
