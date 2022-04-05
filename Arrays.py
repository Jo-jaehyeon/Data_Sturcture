from typing import Any

class Arrays:
    def __init__(self, capacity: int = 256) -> None:
        self.arr = [] * self.capacity               # data를 저장하는 list 배열
        self.capacity = capacity                    # Array의 최대 크기
        self.size = 0                               # Array에 들어간 데이터 수

    def __len__(self) -> int:
        return self.size                            # Array에 저잗된 data 개수 반환               
    
    def is_full(self) -> bool:
        return self.size >= self.capacity           # Array가 꽉 찼는지 확인
    
    def is_empty(self) -> bool:
        return self.size <= 0                       # Array가 비어있는지 확인
    
    def insert(self, idx: int, value: Any) -> None:
        if self.is_full():                          # 꽉 찬 경우 함수 종료
            return
        if idx >= self.capacity:                    # 주어진 index가 Array 크기보다 큰 경우 함수 종료
            return

        for i in range(idx, self.capacity - 1):     # 아니라면 주어진 index 번호 ~ list 끝까지 다음을 반복
            self.arr[i + 1] = self.arr[i]           # 주어진 index를 기준으로 뒤로 한칸씩 밀기
            
        self.arr[idx] = value                       # 주어진 index의 값을 변경
        self.size += 1                              # data 개수 + 1
    
    def replace(self, idx: int, value: Any) -> None:
        if self.is_empty:                           # 비어있다면 함수 종료
            return
        self.arr[idx] = value                       # 비어있지 않다면 주어진 index의 값 변경

    def remove(self, idx: int) -> None:
        if self.is_empty():                         # 비어있다면 함수 종료
            return
        if idx >= self.capacity:                    # 주어진 index가 Array 크기보다 큰 경우 함수 종료
            return
                                                    # 비어있지 않다면
        for i in range(idx, self.capacity - 1):     # 주어진 index ~ list끝까지 반복
            self.arr[i] = self.arr[i + 1]           # 주어진 index를 기준으로 앞으로 한칸씩 당기기
        self.size -= 1                              # data의 개수 - 1

    def at(self, idx: int) -> int:
        if self.is_empty():                         # 비어있다면 함수 종료
            return
        if idx >= self.capacity:                    # 주어진 index가 Array 크기보다 큰 경우 함수 종료
            return
        return self.arr[idx]                        # 비어있지 않다면 주어진 index에 저장된 data 반환

    def find(self, value: Any) -> Any:
        for i in range(self.size):                  # data 개수만큼 반복
            if self.arr[i] == value:                # 발견되면 index 반환
                return i
        return -1 
    
    def count(self, value: Any) -> int:
        c = 0
        for i in range(self.size):                  # data 개수만큼 반복
            if self.stk[i] == value:                # 발견되면 +1
                c += 1
        return c                                    # 찾은 개수 반환
    
    def __contains__(self, value: Any) -> bool:
        if self.count(value) > 0:                   # value가 발견되면 True
            return True
        else:                                       # 아니면 False
            return False
    
    def dump(self) -> None:
        if self.is_empty():
            print("Array가 비어있습니다.")
        else:                                       # Array가 비어있지 않을 때 전부 출력
            print(self.arr[:self.size])