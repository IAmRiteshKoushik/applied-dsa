'''
Task Priority Management System : Design a task management system where tasks
are categorized into different priority levels. Each priority level is 
represented as a queue, allowing tasks to be added to the appropriate queue 
based on priority. Utilize a combination of queues for each priority level 
withitn a alrger data structure for managing tasks efficiently.
'''

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Queue():
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, val):
        temp = Node(val)
        if self.rear == None:
            self.front = self.rear = temp
        else:
            self.rear.next = temp
            self.rear = temp

    def dequeue(self):
        if self.rear == None:
            print("Nothing to dequeue")
            return
        else:
            temp = self.front
            self.front = self.front.next
            if self.front == None:
                self.rear = None
            return temp.data

    def isEmpty(self):
        return self.front == None

    def printQueue(self):
        temp = self.rear
        while temp != None:
            print(temp.data, end = "->")
            temp = temp.next
        print(" ") # Ending it with an extra line

class TaskPriorityManager:
    def __init__(self, n): # Setting up number of priorities
        self.n = n
        self.priority = [] # Empty list contianing our queues
        for _ in range(n):
            self.priority.append(None)
    
    def insertP(self, val, p):
        if self.priority[p] == None:
            temp = Queue()
            self.priority[p] = temp
            temp.enqueue(val)
        else:
            self.priority[p].enqueue(val)

    def printTask(self):
        for i in range(len(self.priority)):
            if self.priority[i] != None:
                print("Process ", i, ":")
                q = self.priority[i]
                q.printQueue()


def main():
    t = TaskPriorityManager(5)
    t.insertP(1, 1)
    t.insertP(1, 2)
    t.insertP(2, 1)
    t.insertP(2, 2)
    t.printTask()

if __name__ == "__main__":
    main()
