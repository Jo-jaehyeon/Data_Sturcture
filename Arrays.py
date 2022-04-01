from typing import Any

from cv2 import INTERSECT_FULL

class Arrays:
    def __init__(self, capacity: int = 256) -> None:
        self.arr = [] * self.capacity
        self.capacity = capacity
        self.size = 0

    def __len__(self) -> int:
        return self.capacitygit 
    
    def is_full(self) -> bool:
        return self.size >= self.capacity
    
    def is_empty(self) -> bool:
        return self.size <= 0
    
    def insert(self, idx: int, value: Any) -> None:
        if self.is_full():
            return
        
        for i in range(idx, self.capacity - 1):
            self.arr[i + 1] = self.arr[i]
        
        self.arr[idx] = value
        self.size += 1
    
    def replace(self, idx: int, value: Any) -> None:
        if self.is_empty:
            return

        self.arr[idx] = value

    def remove(self, idx: int) -> None:
        if self.is_empty():
            return
        
        for i in range(idx, self.capacity - 1):
            self.arr[i] = self.arr[i + 1]
        self.size -= 1

    def at(self, idx: int) -> int:
        if self.is_empty():
            return

        return self.arr[idx]