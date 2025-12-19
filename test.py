from typing import Any, Optional


class Node:
    """Internal node class for linked list implementations."""
    def __init__(self, value: Any):
        self.value = value
        self.next: Optional['Node'] = None


class LinkedList:
    """Standard singly linked list with index-based operations."""
    
    def __init__(self):
        self.head: Optional[Node] = None
    
    def insert(self, index: int, value: Any) -> None:
        """Insert value at the specified index position."""
        new_node = Node(value)
        
        # Handle insertion at head (index 0 or negative index)
        if index <= 0 or self.head is None:
            new_node.next = self.head
            self.head = new_node
            return
        
        # Traverse to the position before the insertion point
        current = self.head
        for _ in range(index - 1):
            if current.next is None:
                # Index beyond length, insert at end
                current.next = new_node
                return
            current = current.next
        
        # Insert at the specified position
        new_node.next = current.next
        current.next = new_node
    
    def delete(self, index: int) -> object:
        """Delete node at index and return its value."""
        if self.head is None:
            raise IndexError("Cannot delete from empty list")
        
        # Handle deletion at head
        if index <= 0:
            value = self.head.value
            self.head = self.head.next
            return value
        
        # Traverse to the node before the one to delete
        current = self.head
        for _ in range(index - 1):
            if current.next is None:
                raise IndexError("Index out of bounds")
            current = current.next
        
        if current.next is None:
            raise IndexError("Index out of bounds")
        
        # Delete the node
        value = current.next.value
        current.next = current.next.next
        return value
    
    def to_list(self) -> list:
        """Return a list of values from front to back."""
        result = []
        current = self.head
        while current is not None:
            result.append(current.value)
            current = current.next
        return result
    
    def __len__(self) -> int:
        """Return the number of nodes in the list."""
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count


class CircularLinkedList:
    """Circular linked list with cursor-based operations."""
    
    def __init__(self):
        self.cursor: Optional[Node] = None
    
    def insert(self, value: Any) -> None:
        """Insert value after cursor and move cursor to new node."""
        new_node = Node(value)
        
        if self.cursor is None:
            # Empty list: create single node pointing to itself
            new_node.next = new_node
            self.cursor = new_node
        else:
            # Insert after cursor
            new_node.next = self.cursor.next
            self.cursor.next = new_node
            # Move cursor to new node
            self.cursor = new_node
    
    def delete(self, value: Any) -> bool:
        """Delete first node with matching value. Return True if successful, False otherwise."""
        if self.cursor is None:
            return False
        
        # Special case: only one node
        if self.cursor.next == self.cursor:
            if self.cursor.value == value:
                self.cursor = None
                return True
            return False
        
        # Search for the node to delete
        current = self.cursor
        while True:
            if current.next.value == value:
                # Found the node to delete
                deleted_node = current.next
                current.next = deleted_node.next
                
                # If cursor was deleted, move cursor to previous node
                if deleted_node == self.cursor:
                    self.cursor = current
                
                return True
            
            current = current.next
            
            # Checked all nodes, value not found
            if current == self.cursor:
                return False
    
    def get_next(self) -> Optional[object]:
        """Move cursor to next node and return its value. Return None if empty."""
        if self.cursor is None:
            return None
        
        self.cursor = self.cursor.next
        return self.cursor.value
    
    def search(self, value: Any) -> bool:
        """Check if value exists in the list."""
        if self.cursor is None:
            return False
        
        # Start from cursor and traverse one full cycle
        current = self.cursor
        while True:
            if current.value == value:
                return True
            current = current.next
            if current == self.cursor:
                break
        
        return False

