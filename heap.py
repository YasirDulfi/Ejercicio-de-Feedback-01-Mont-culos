class Heap():
    def __init__(self, size) -> None:
        self.max_size = size
        self.heap = []
        self.size = 0

    def getParentIndex(self,index):
        return int((index-1)/2)
    
    def getLeftChildIndex(self, index):
        return (2*index+1)
    
    def getRightChildIndex(self, index):
        return (2*index + 2)
    
    def hasParent(self, index):
        return self.getParentIndex(index) >= 0
    
    def hasLeftChild(self, index):
        return self.getLeftChildIndex(index) < self.size
    
    def hasRightChild(self, index):
        return self.getRightChildIndex(index) < self.size
    
    def getParent(self,index):
        return self.heap[int((index-1)/2)]
    
    def getLeftChild(self, index):
        if(self.hasLeftChild(index)):
            return self.heap[2*index+1]
        return None
    
    def getRightChild(self, index):
        if(self.hasRightChild(index)):
            print("El index: "+str(index))
            print(2*index + 2)
            print(self.size)
            print(len(self.heap))
            return self.heap[2*index + 2]
        return None
    
    def isFull(self):
        return self.size == self.max_size
    
    def swap(self, index1, index2):
        temp = self.heap[index1]
        self.heap[index1] = self.heap[index2]
        self.heap[index2] = temp

    def isEmpty(self):
        return len(self.heap) == 0
    
    def peek(self, position=0):
        if(self.size == 0):
            return None
        return self.heap[position]

    def eliminarPaciente(self, pacienteEliminar):
        for index, paciente in enumerate(self.heap):
            if(paciente.nombre == pacienteEliminar.nombre):
                self.heap.pop(index)
                self.size -=1

class MinHeap(Heap):
    def __init__(self, size) -> None:
        super().__init__(size)

    
    def heapifyUp(self):
        index = self.size-1
        while(self.hasParent(index) and self.heap[index].horas_espera < self.getParent(index).horas_espera):
            self.swap(index, self.getParentIndex(index) )
            index = self.getParentIndex(index)
    
    def heapifyDown(self):
        index = 0
        while(self.hasLeftChild(index)):
            if(self.hasRightChild(index ) and self.getRightChild(index) < self.getLeftChild(index)):
                self.swap(index, self.getRightChildIndex(index))
                index = self.getRightChildIndex(index)
            
            if(self.hasLeftChild(index) and self.getLeftChild(index)<self.getRightChild(index)):
                self.swap(index, self.getLeftChildIndex(index))
                index = self.getRightChildIndex(index)

    
    def peekByTime(self):
        for persona in self.heap:
            if(persona.horas_espera >= 5):
                return persona
        return None
    def insert(self, paciente):
        if(self.isFull()):
            raise("Heap lleno!")
        else:
            self.heap.append(paciente)
            self.size += 1
            self.heapifyUp()

    def removeMin(self):
        if(self.size == 0):
            print("El Heap esta vacio")
            raise("Empty Heap")
        data = self.heap[0]

        if(self.heap[2]<self.heap[1]):
            self.heap[0] = self.heap[2]
            for index,values in enumerate(self.heap):
                if index >= 2 and (index+1 < (self.size-1)) :
                    self.heap[index] = self.heap[index+1]
                if(index+1 > (self.size-1)):
                    self.heap[-2] = self.heap[-1]
                    self.heap.pop(-1)
        if(self.heap[1]<self.heap[2]and (index+1 < (self.size-1))):
            self.heap[0] = self.heap[1]
            for index, value in enumerate(self.heap):
                if index >=1:
                    self.heap[index] = self.heap[index+1]
                if(index+1 > (self.size-1)):
                    self.heap[-2] = self.heap[-1]
                    self.heap.pop(-1)
        self.size -= 1

    def removeMin2(self):
        if(self.size == 0):
            print("Heap vacio")
            raise("Empty Heap")
        data = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heapifyDown()
        self.heap.pop(-1)
        self.size -= 1







class MaxHeap(Heap):
    def __init__(self, size) ->None:
        super().__init__(size)
        self.max_size = size
        self.size = 0
        self.heap = []

    def heapifyUp(self):
        index = self.size - 1
        while(self.hasParent(index) and self.heap[index].nivel_urgencia>self.getParent(index).nivel_urgencia):
            self.swap(index, self.getParentIndex(index))
            index = self.getParentIndex(index)

    def heapifyDown(self):
        index = 0
        while(self.hasLeftChild(index)):
            print("Hepify Down")

            if(self.hasRightChild(index) and self.getRightChild(index).nivel_urgencia>self.getLeftChild(index).nivel_urgencia and self.getRightChild(index).nivel_urgencia>self.heap[index].nivel_urgencia):
                self.swap(index, self.getRightChildIndex(index))
                index = self.getRightChildIndex(index)
                print('condicion 1')
                continue

            print("condicion 2")
            self.swap(index, self.getLeftChildIndex(index))
            index =  self.getLeftChildIndex(index)

    def insert(self, data):
        if(self.isFull()):
            print("El heap esta lleno")
            raise("El heap esta lleno")

        self.heap.append(data)
        self.heapifyUp()
        self.size += 1

    def removeMax(self):
        if(self.size == 0):
            print("El heap esta vacio")
            raise("El heap esta vacio")
        data = self.heap[0] 
        self.heap[0] = self.heap[-1]
        self.heapifyDown()
        self.heap.pop(-1)
        self.size -= 1

    
"""
elHeap = MaxHeap(7)

elHeap.insert(1)
elHeap.insert(15)
elHeap.insert(12)
elHeap.insert(100)
elHeap.insert(10)
elHeap.insert(120)
elHeap.insert(0)

print("el Heap es:  "+str(elHeap.heap))

elHeap.removeMax2()

print("el 2ndo Heap es:  "+str(elHeap.heap))
"""