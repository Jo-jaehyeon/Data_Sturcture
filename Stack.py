from typing import Any

class Stack:
    def __init__(self, capacity: int = 256) -> None:
        self.stk = [None] * capacity            # 데이터를 저장하는 list 배열
        self.capacity = capacity                # 스택의 최대 크기
        self.ptr = 0                            # 저장된 데이터의 개수(스택 포인터)
    
    def __len__(self) -> int:
        return self.ptr                         # 스택에 저장된 데이터 개수 반환
    
    def is_empty(self) -> bool:
        return self.ptr <= 0                    # 스택이 비어있는지 확인

    def is_full(self) -> bool:
        self.ptr >= self.capacity               # 스택이 가득 찼는지 확인
    
    def push(self, value) -> None:
        if self.is_full():              
            pass
        self.stk[self.ptr] = value              # 스택이 가득 차 있지 않다면 꼭대기에 데이터 저장
        self.ptr += 1                           # 스택 포인터 +1
    
    def pop(self) -> Any:
        if self.is_empty():             
            pass
        self.ptr -= 1                           # 비어있지 않다면 스택 포인터 -1
        return self.stk[self.ptr]               # 꼭대기에 있는 데이터 반환
    
    def peek(self) -> Any:
        if self.is_empty:
            pass
        return self.stk[self.ptr-1]             # 비어있지 않다면 꼭대기에 있는 데이터 반환
    
    def clear(self):    
        self.ptr = 0                            # 스택 포인터 = 0

    def find(self, value: Any) -> Any:
        for i in range(self.ptr -1, -1, -1):    # 스택 포인터 -> 0까지 거꾸로(꼭대기 -> 바닥)
            if self.stk[i] == value:            # 발견되면 index 반환
                return i
        return -1 
    
    def count(self, value: Any) -> int:
        c = 0
        for i in range(self.ptr):               # 스택 포인터 수 만큼 반복
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
            print("스택이 비어있습니다.")
        else:                                   # 스택이 비어있지 않을 때 전부 출력
            print(self.stk[:self.ptr])



