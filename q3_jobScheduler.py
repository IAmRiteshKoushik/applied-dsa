'''
Job Scheduling System (Data Center) : Desing a job scheduling system for a 
data center where each server's task queue is represented as a queue of jobs.
New jobs are added to the appropriate server's queue based on factors like 
server load and job priority. Utilize a combination of queues and a priority
queue for efficient job scheduling across multiple servers.
'''

class Node:
    def __init__(self, data, priority, next = None):
        self.data = data
        self.priority = priority
        self.next = next

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value, priority):
        if self.isEmpty() == True:
            self.front = Node(value, priority)

    def dequeue(self):
        pass

    def isEmpty(self):
        return self.front == None

    def printQueue(self):
        temp = self.front
        while temp != None:
            print(temp.data, end = "->")
            temp = temp.next

        print(" ")

class JobSchedulingSystem:
    def __init__(self, n):
        self.n = n
        self.server = [None for _ in range(n)]

    def insertJob(self, val, i, p):
        pass

    def removeJob(self, i, p):
        pass

    def printJobs(self):
        for i in range(len(self.server)):
            if self.server[i] != None:
                print("job", i, ":")
                q = self.server[i]
                q.printQueue() # Error

def main():
    t = JobSchedulingSystem(5)
    t.insertJob(1, 1, 10)
    t.insertJob(1, 1, 2)
    t.insertJob(2, 2, 1)
    t.insertJob(2, 2, 2)
    t.printJobs()

if __name__ == "__main__":
    main()
