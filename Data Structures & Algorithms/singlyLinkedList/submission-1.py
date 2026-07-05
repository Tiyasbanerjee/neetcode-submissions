class Node:
    def __init__(self, val=0):
        self.val = val      
        self.next = None   

class LinkedList:

    def __init__(self):
        self.main_pointer = Node(0)
        self.data_size = 0
    
    def get(self, index: int) -> int:
        if index >= self.data_size or index<0:
            return -1
        else:
            j = self.main_pointer.next
            for i in range(index):
                j = j.next
            
            return j.val


    def insertHead(self, val: int) -> None:
        self.data_size += 1
        new_head = Node(val)
        new_head.next = self.main_pointer.next
        self.main_pointer.next = new_head
        return None

    def insertTail(self, val: int) -> None:
        self.data_size += 1

        new_tail = Node(val)
        new_tail.next = None
        
        j = self.main_pointer

        while j.next != None:
            j = j.next
        
        j.next = new_tail

        return None

    def remove(self, index: int) -> bool:

        if index >= self.data_size or index<0:
            return False
       
        else: 
            self.data_size -= 1
            
            j = self.main_pointer

            for i in range(index):
                j = j.next
            
            j.next = j.next.next

            return True

    def getValues(self) -> List[int]:
        arr = []
        j = self.main_pointer.next

        while j is not None:
                arr.append(j.val)
                j = j.next
            
            
        return arr
        
