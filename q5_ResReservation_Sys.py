'''
Restaurant Reservation System : Design a reservation system for a restuarant
where each table's reservation list is represented as a queue of reservations.
New reservations are added to the appropriate table's queue based on factors 
like reservation time and table availablity. Utilize a combination of queues 
within a larger data structure for efficient reservation management.
'''

class Queue:
    def __init__(self, max):
        self.front = 0
        self.rear = -1
        self.max = max 
        self.q = [None for _ in range(max)]
        self.sz = 0

    def enqueue(self, val):
        if self.size() != self.max:
            self.rear += 1
            self.q[self.rear] = val
        else:
            print("Queue is full")
            return
        self.sz += 1

    def dequeue(self):
        if self.rear == -1:
            return "Error"
        temp = self.q[self.front]
        self.q[self.front] = None
        self.front += 1
        return temp

    def size(self):
        return self.sz

    def isFull(self):
        return self.size() == self.max

    def isEmpty(self):
        return self.size() == 0

    def printQueue(self):
        for i in range(self.max):
            if(self.q[i] != None):
                print(self.q[i], end = " ")

class ReservationSys:
    def __init__(self, n):
        self.sz = n
        self.tables = [Queue(5) for _ in range(n)]
    
    def find_table(self):
        i = 0
        while i != self.sz:
            temp = self.tables[i]
            if not temp.isFull():
                return i
            i += 1
        return 0

    def reserve(self, name):
        temp = self.tables[self.find_table()]
        if not temp.isFull():
            temp.enqueue(name)
        else:
            return "Table full"

    def printReservations(self):
        i = 0
        while i != self.sz:
            x = i + 1
            temp = self.tables[i]
            print("\nTable No: ", x)

            if (temp.isEmpty()):
                print("Null")
            else:
                temp.printQueue()
                print("\n")
            i += 1

def main():
    t = ReservationSys(5)
    t.reserve("RK")
    t.reserve("RK1")
    t.reserve("RK3")
    t.reserve("RK4")
    t.reserve("RK5")
    t.reserve("RK6")
    t.reserve("RK7")
    t.reserve("RK8")
    print("\nTable")
    t.printReservations()

if __name__ == "__main__":
    main()
