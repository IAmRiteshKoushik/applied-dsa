'''
Bug Tracking System (SDE) : Design a bug tracking system for software development
where each software component's bug list is repreented as a stack of bugs. New 
bugs are added to the appropriate component's stack ad bugs are resolved by 
popping the from the stack. Utilize a combination of stacks within a larger 
data structure for efficient bug tracking across software components.
'''

class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class Stack:
    def __init__(self):
        self.top = None

    def push(self, val):
        temp = Node(val)
        temp.next = self.top
        self.top = temp

    def pop(self):
        if self.top == None:
            return "Empty"
        else:
            temp = self.top.data
            self.top = self.top.next
            return temp

    def print_stack(self):
        current = self.top
        while current:
            print(current.data)
            current = current.next

class BugNode:
    def __init__(self, component):
        self.data = Stack()
        self.next = None
        self.component = component

class BugTrack:
    def __init__(self):
        self.head = None

    def insertBug(self, component, bug):
        if self.head == None:
            self.head = BugNode(component)
            self.head.data.push(bug)
        else:
            temp = self.head

            while temp != None and temp.component != component:
                temp = temp.next

            # Taking temp to None
            if temp.component != component:
                newBug = BugNode(component)
                newBug.next = self.head
                self.head = newBug.next
                newBug.data.push(bug)
            else:
                temp.data.push(bug)

    def resolveBug(self, component):
        if self.head == None:
            return "No Bugs"

    def printBugs(self):
        temp = self.head
        while temp != None:
            print("Component Name: ", temp.component)
            print("Bugs: ")
            temp.data.print_stack()
            print("----------------")
            temp = temp.next
        
def main():
    b = BugTrack()
    b.insertBug("ALU", "Register x0A failed")
    b.insertBug("ALU", "Register x0B failed")
    b.printBugs()
    b.resolveBug("ALU")
    b.printBugs()

if __name__ == "__main__":
    main()
