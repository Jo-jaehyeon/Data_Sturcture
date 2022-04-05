from typing import Any

class Queue:
    def __init__(self, capacity: int = 256) -> None:
        self.que = [None] * capacity                # data를 저장하는 list 배열
        self.capacity = capacity                    # Queue의 최대 크기
        self.front = 0                              # 맨 앞 원소 커서
        self.rear = 0                               # 맨 뒤 원소 커서
        self.no = 0                                 # 현재 data 개수

    def __len__(self) -> int:
        return self.no                              # Queue에 저장된 data 개수 반환
    
    def is_empty(self) -> bool:
        return self.no <= 0                         # Queue가 비어있는지 확인

    def is_full(self) -> bool:
        return self.no >= self.capacity             # Queue가 가득 찼는지 확인
    
    def enque(self, value) -> None:
        if self.is_full():                          # 꽉 찼다면 함수 종료
            return

        self.que[self.rear] = value                 # Queue가 가득 차 있지 않다면 data 저장
        self.rear += 1                              # 맨 뒤 원소 커서 +1
        self.no += 1                                # data 개수 +1
       
        if self.rear == self.capacity:              # 맨 뒤 원소 커서가 list 끝에 도달했다면 0으로 당기기
            self.rear = 0
    
    def deque(self) -> Any:
        if self.is_empty():                         # 비어있다면 함수 종료
            return

        value = self.que[self.front]
        self.front += 1                             # 비어있지 않다면 맨 앞 커서 +1
        self.no -= 1                                # 원소 개수 -1
       
        if self.front == self.capacity:             # 맨 앞 원소 커서가 list 끝에 도달했다면 0으로 당기기
            self.front = 0

        return value                                # 맨 앞 원소 반환
    
    def peek(self) -> Any:
        if self.is_empty:
            return

        return self.que[self.front]                 # 비어있지 않다면 맨 앞에 있는 data 반환
    
    def clear(self):    
        self.no = self.front = self.queue = 0       # 원소 개수, 맨 앞 원소 커서, 맨 뒤 원소 커서 = 0
        
    def find(self, value: Any) -> Any:
        for i in range(self.no):                    # 원소 개수만큼 반복
            idx = (i + self.front) % self.capacity  # front부터 원소 개수 만큼 스캔
            if self.que[idx] == value:              # 발견되면 index 반환
                return idx
        return -1 
    
    def count(self, value: Any) -> int:
        c = 0
        for i in range(self.no):                    # 원소 개수 만큼 반복
            idx = (i + self.front) % self.capacity
            if self.que[idx] == value:              # 발견되면 +1
                c += 1
        return c                                    # 찾은 개수 반환
    
    def __contains__(self, value: Any) -> bool:
        if self.count(value) > 0:                   # value가 발견되면 True
            return True
        else:                                       # 아니면 False
            return False
    
    def dump(self) -> None:
        if self.is_empty():
            print("Queue가 비어있습니다.")
        else:                                       # Queue가 비어있지 않을 때 전부 출력
            for i in range(self.no):
                print(self.que[(i + self.front) % self.capacity], end=' ')
            print()



