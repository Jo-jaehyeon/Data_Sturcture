from typing import Any

class Node:
    def __init__(self, value: Any):
        self.data = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None                                # 제일 앞 Node
        self.tail = None                                # 제일 뒤 Node
        self.size = 0                                   # data의 개수
    
    def __len__(self) -> int:
        return self.size                                # 연결된 Node 개수 반환

    def get_node(self, idx: int) -> Node:
        cnt = 0                             
        node = self.head                                # head node 가져오기

        while cnt < idx:                                # idx에 도달할 때 까지 Node.next 반복
            cnt += 1
            node = node.next

        return node                                     # 찾아낸 node 반환

    def add_node(self, idx: int, value: Any) -> None:
        new_node = Node(value)                          # value를 data로 하는 Node 생성

        if self.size == 0:                              # data의 개수가 0개인 경우
            self.head = new_node                        # new_node를 head로 지정

        elif self.size == 1:                            # data의 개수가 1개인 경우 
            self.tail = new_node                        # new_node를 tail로 지정 후 head와 연결
            self.head.next = self.tail

        else:
            if idx == 0:                                # 추가하려는 위치가 첫번째 인 경우
                new_node.next = self.head               # new_node에 head node 연결 후 head로 변경
                self.head = new_node        

            else:                                       # 추가하려는 위치가 node 사이인 경우
                before_node = self.get_node(idx - 1)    # 추가하려는 위치 양 옆 node 찾기
                next_node = before_node.next

                before_node.next = new_node             # 양 옆 node에 새로운 node 연결
                new_node.next = next_node

                if before_node == self.tail:            # 만약 추가하려 했던 위치가 마지막이라면
                    self.tail = new_node                # new_node를 tail로 변경
        
        self.size += 1                                  # node 개수 +1

    def delete_node(self, idx) -> None:
        if self.size == 0:                              # node 개수가 0이라면 함수 종료
            return 

        if idx == 0:                                    # 지우려는 node가 head라면
            self.head = self.head.next                  # head를 head.next로 변경 후 종료
            return 
        
        before_node = self.get_node(idx - 1)            # 삭제하려는 위치 이전 node 
        if before_node == self.tail:                    # 만약 삭제하려 했던 위치가 범위 밖이라면 함수 종료
            return
        next_node = self.get_node(idx + 1)              # 삭제하려는 위치 다음 node
        before_node.next = next_node                    # node 재연결
        self.size -= 1                                  # node 개수 -1
    
    def dump(self) -> None:
        cnt = 0                                         # 모든 node의 data 출력하는 함수
        node = self.get_node(0)
        while cnt < self.__len__():
            print(node.data, end = ' ')
            cnt += 1
            node = node.next