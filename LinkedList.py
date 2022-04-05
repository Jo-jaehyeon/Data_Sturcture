from typing import Any

class Node:
    def __init__(self, value: Any):
        self.data = value
        self.next = None

class LinkedList:
    def __init__(self, value: Any):
        root = Node(value) 
        self.head = root                   # 제일 앞 Node
        self.tail = root                   # 제일 뒤 Node
        self.head.next = self.tail

        self.size = 1                      # data의 개수
    
    def __len__(self) -> int:
        return self.size

    def get_node(self, idx: int) -> Node:
        cnt = 0
        node = self.head

        while cnt < idx:
            cnt += 1
            node = node.next

        return node

    def add_node(self, idx: int, value: Any) -> None:
        new_node = Node(value)  
        if idx == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            before_node = self.get_node(idx - 1)
            next_node = before_node.next

            before_node.next = new_node
            new_node.next = next_node

            if before_node == self.tail:
                self.tail = new_node

        self.size += 1

    def delete_node(self, idx) -> None:
        if self.size == 0:
            return 

        if idx == 0:
            self.head = self.head.next
            return 
        
        before_node = self.get_node(idx-1)
        before_node.next = before_node.next.next
        self.size -= 1

        return 
    
    def dump(self):
        cnt = 0
        node = self.get_node(0)
        while cnt < self.__len__():
            print(node.data, end = ' ')
            cnt += 1
            node = node.next

