class MyCircularQueue(object):
    def __init__(self, k):
        self.queue=[None]*k
        self.front=0
        self.rear=0
        self.size=0

    def enQueue(self, value):
        if not self.isFull():
            self.queue[self.rear]=value
            self.rear=(self.rear+1)%len(self.queue)
            self.size+=1
            return True
        return False

    def deQueue(self):
        if not self.isEmpty():
            self.front=(self.front+1)%len(self.queue)
            self.size-=1
            return True
        return False

    def Front(self):
        if not self.isEmpty():
            return self.queue[self.front]
        return -1

    def Rear(self):
        if not self.isEmpty():
            return self.queue[self.rear-1]
        return -1

    def isEmpty(self):
        if self.size==0:
            return True
        return False

    def isFull(self):
        if self.size==len(self.queue):
            return True
        return False

        myCircularQueue = MyCircularQueue(3)
        print(myCircularQueue.enQueue(1)) # return True
        print(myCircularQueue.enQueue(2)) # return True
        print(myCircularQueue.enQueue(3)) # return True
        print(myCircularQueue.enQueue(4)) # return False
        print(myCircularQueue.Rear()) # return 3
        print(myCircularQueue.isFull()) #return True
        print(myCircularQueue.deQueue()) #return True
        print(myCircularQueue.enQueue(4)) #return True
        print(myCircularQueue.Rear()) #return 4