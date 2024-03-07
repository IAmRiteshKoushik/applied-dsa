class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class Stack:
    def __init__(self):
        self.top = None

    def push(self,data):
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

class EventRegistrationSys:
    def __init__(self):
        self.sessions = {}

    def register(self, attendee, session):
        if session not in self.sessions:
            self.sessions[session] = Stack()
        self.sessions[session].push(attendee)

    def unregister(self, session):
        if session in self.sessions:
            self.sessions[session].pop()

    def print_events(self):
        for session, attendee_stack in self.sessions.items():
            print("Session: ", session)
            print("Registered Attendees:")
            attendee_stack.print_stack()
            print()

def main():
    conference_system = EventRegistrationSys()

    # Registered attendees for different sessions
    conference_system.register("Alice", "Session 1") 
    conference_system.register("Bob", "Session 1")
    conference_system.register("Charlie", "Session 2")
    conference_system.register("David", "Session 3")

    # Print initial registration
    conference_system.print_events()

    # Unregister an attendee
    conference_system.unregister("Session 1")

    # Print updated registration
    conference_system.print_events()

if __name__ == "__main__":
    main()

