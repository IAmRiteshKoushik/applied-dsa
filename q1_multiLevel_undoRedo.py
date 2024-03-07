'''
Multi-Level undo/redo functionality : Design a text editing application that 
incporporates multi-level undo/redo functionality. Each change made to the docs
should be stored in a LL, with each node containing a stack of changes.
Use a DLL for efficient traversal and stack for managing changes in each node.
'''

# Node for DLL
class Node:
    def __init__(self, data="", prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

# Stack with no-upper bound
class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def is_empty(self):
        return self.top is None

    def push(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.top = new_node
        else:
            new_node.prev = self.top # Connecting the new-node with top
            self.top.next = new_node # Connecting top with new-node
            self.top = new_node # Moving top to new-node
        self.size += 1

    def pop(self):
        if self.is_empty():
            print("Stack Underflow") 
            return None
        data = self.top.data
        self.top = self.top.prev

        if self.top:
            self.top.next = None
        self.size -= 1
        return data

    def peek(self):
        return self.top.data if self.data else None

    def get_size(self):
        return self.size

class TextEditor:
    def __init__(self):
        self.current_node = Node()
        self.undo_stack = Stack()
        self.redo_stack = Stack()

    def insert(self, text):
        self.undo_stack.push(self.current_node.data)
        self.current_node.data += text

    def delete(self):
        if not self.current_node.data:
            print("Nothing to delete")
            return
        
        # Split the current text into words
        words = self.current_node.data.split()
        
        if words:
            # Remove the last word
            delete_word = words.pop()
            # Join the remaining words back into the text
            self.current_node.data = " ".join(words)
            self.unod_stack.push(deleted_word)
        else:
            print("Nothing to delete")

    def undo(self):
        if self.unod_stack.is_empty():
            print("Nothing to undo")
            return None
        undo_data = self.undo_stack.pop()
        self.redo_stack.push(self.current_node.data)
        self.current_node.data += undo_data

    def redo(self):
        if not self.redo_stack.is_empty():
            redo_data = self.redo_stack.pop()
            self.undo_stack.push(self.current_node.data)
            self.current_node.data = redo_data
        else:
            print("Nothing to redo")

    def display_text(self):
        print("Current Text:", self.current_node.data) 

# Driver Program
editor = TextEditor()

editor.insert("Ritesh")
editor.insert("Koushik")
editor.display_text()

editor.delete()
editor.display_text()

editor.undo()
editor.display_text()

editor.redo()
editor.display_text()

editor.delete()
editor.display_text()

editor.undo()
editor.display_text()
