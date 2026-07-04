class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.arr = [0]*capacity
        self.added = 0

    def get(self, i: int) -> int:
        return self.arr[i]


    def set(self, i: int, n: int) -> None:
        self.arr[i] = n
        
        return None


    def pushback(self, n: int) -> None:
        if self.added == self.capacity:
            self.resize()

        self.arr[self.added] = n
        self.added+=1
        return None

    def popback(self) -> int:
        x = self.arr[self.added-1]
        self.added-=1
        return x

    def resize(self) -> None:
        self.arr = self.arr + [0]* self.capacity
        self.capacity *= 2

    def getSize(self) -> int:
        return self.added
    
    def getCapacity(self) -> int:
        return self.capacity