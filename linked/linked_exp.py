# First we need to create an object class for the new node.

class Node:
    def _int_(self, data):
        self.data = data
        self.next = None
        
# Next create a function to insert data into the linked list.

    def insert_head(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node
    
# Insert in a specific location using index for reference.

    def insert_middle(self, data, index):
        new_node = Node(data)
        current_node = self.head
        position = 0
        if position == index:
            self.insertAtBegin(data)
        else:
            while(current_node != None and position+1 != index):
                position = position+1
                current_node = current_node.next
 
            if current_node != None:
 
                new_node.next = current_node.next
                current_node.next = new_node
            else:
                print("Index not present")
    
# Insert at the end/tail of the linke list.

    def insert_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
    
        current_node = self.head
        while(current_node.next):
            current_node = current_node.next
    
        current_node.next = new_node

# We learned to insert, not lets delete a node from the linked list at the head.

def remove_head_node(self):
    if(self.head == None):
        return
     
    self.head = self.head.next

# Lets delete at a specific location using index for reference.

def remove_at_index(self, index):
        if self.head == None:
            return
 
        current_node = self.head
        position = 0
        if position == index:
            self.remove_first_node()
        else:
            while(current_node != None and position+1 != index):
                position = position+1
                current_node = current_node.next
 
            if current_node != None:
                current_node.next = current_node.next.next
            else:
                print("Index not present")
    
# Lets remove a node from the tail.
    
def remove_last_node(self):
 
    if self.head is None:
        return
 
    current_node = self.head
    while(current_node.next.next):
        current_node = current_node.next
 
    current_node.next = None
    

