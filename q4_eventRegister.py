'''
Event Registration System (Conference) : Design an event registration system 
for a conference where attendees register for different sessions. Each 
sessions' attendee list is represeted as a stack allowign attendees to register
and unregister for sessions. Utilize a combination of stacks within a larger
data structure to manage session registrations efficiently.
'''

class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            return None
        data = self.top.data
        self.top = self.top.next
        return data

    def print_stack(self):
        current = self.top
        while current:
            print(current.data)
            current = current.next

class Node2:
    def __init__(self, name, next = None):
        self.data = Stack()
        self.next = next
        self.name = name

class Event:
    def __init__(self):
        self.head = None

    def register(self, name, event):
        if self.head is None:
            self.head = Node2(event)
            self.head.data.push(name)
        else:
            temp = self.head
            while temp.next is not None and temp.name != event:
                temp = temp.next

            if temp.name != event:
                new_event = Node2(event)
                new_event.next = self.head
                self.head = new_event
                new_event.data.push(name)
            else:
                temp.data.push(name)

    def unregister(self, event):
        if self.head is None:
            return "No events"

        else:
            temp = self.head
            while temp is not None and temp.name != event:
                temp = temp.next

            if temp is not None:
                temp.data.pop()
                if temp.data.top is None:
                    temp.name = temp.next.name
                    temp.data = temp.next.data
                    temp.next = temp.next.data
                else:
                    self.head = None
    
    def printEvents(self):
        temp = self.head
        while temp is not None:
            print("Event name: ", temp.name)
            print("Regisgtered Users: ")
            temp.data.print_stack()
            print("---------------")
            temp = temp.next

def main():
    e = Event()
    e.register("Alice", "Birth")
    e.register("BOB", "doom")
    e.register("BOBI", "doom")

    e.printEvents()
    print("\n\nAfter Unregistration")
    e.unregister("doom")
    e.printEvents()

if __name__ == "__main__":
    main()

