from typing import Any

class Stack:
    def __init__(self, capacity: int = 256) -> None:
        self.stk = [None] * capacity            # data를 저장하는 list 배열
        self.capacity = capacity                # Stack의 최대 크기
        self.stp = 0                            # 저장된 data의 개수(Stack Pointer)
    
    def __len__(self) -> int:
        return self.stp                         # Stack에 저장된 data 개수 반환
    
    def is_empty(self) -> bool:
        return self.stp <= 0                    # Stack이 비어있는지 확인

    def is_full(self) -> bool:
        self.stp >= self.capacity               # Stack이 가득 찼는지 확인
    
    def push(self, value) -> None:
        if self.is_full():                      # 꽉 찼다면 함수 종료
            pass
        self.stk[self.stp] = value              # Stack이 가득 차 있지 않다면 꼭대기에 data 저장
        self.stp += 1                           # Stack Pointer +1
    
    def pop(self) -> Any:
        if self.is_empty():                     # 비어있다면 함수 종료
            pass
        self.stp -= 1                           # 비어있지 않다면 Stack Pointer -1
        return self.stk[self.stp]               # 꼭대기에 있는 data 반환
    
    def peek(self) -> Any:
        if self.is_empty:                       # 비어있다면 함수 종료
            pass
        return self.stk[self.stp-1]             # 비어있지 않다면 꼭대기에 있는 data 반환
    
    def clear(self):    
        self.stp = 0                            # Stack Pointer = 0

    def find(self, value: Any) -> Any:
        for i in range(self.stp -1, -1, -1):    # Stack Pointer에서 0까지 거꾸로(꼭대기 -> 바닥)
            if self.stk[i] == value:            # 발견되면 index 반환
                return i
        return -1 
    
    def count(self, value: Any) -> int:
        c = 0
        for i in range(self.stp):               # Stack Pointer 수 만큼 반복
            if self.stk[i] == value:            # 발견되면 +1
                c += 1
        return c                                # 찾은 개수 반환
    
    def __contains__(self, value: Any) -> bool:
        if self.count(value) > 0:               # value가 발견되면 True
            return True
        else:                                   # 아니면 False
            return False
    
    def dump(self) -> None:
        if self.is_empty():
            print("Stack이 비어있습니다.")
        else:                                   # Stack이 비어있지 않을 때 전부 출력
            print(self.stk[:self.stp])



