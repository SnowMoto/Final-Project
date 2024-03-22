class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class StarWarsLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        """Need to create the function to insert the at the head of the list. 
        HINT: mixed current and new nodes.
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    
    def locate(self, name):
        """Find a character in the list using index for reference.
        """
        current = self.head
        index = 0
        while current:
            if current.data == name:
                return index
            current = current.next
            index += 1
        return -1

    def delete(self, data):
        """Need to create a function that can delete from the list at the head.
        HINT: While Loop is handy to locate the node.
        """
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        prev = None
        while current:
            if current.data == data:
                prev.next = current.next
                return
            prev = current
            current = current.next

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# Creating a Star Wars linked list
star_wars_list = StarWarsLinkedList()
star_wars_list.insert("Luke Skywalker")
star_wars_list.insert("Darth Vader")
star_wars_list.insert("Princess Leia")
star_wars_list.insert("Han Solo")

# Displaying the list
print("Star Wars Characters:")
star_wars_list.display()

#Locate a character
target_character = "Han Solo"
index = star_wars_list.locate(target_character)
if index != -1:
    print(f"{target_character} found at index {index}")
else:
    print(f"{target_character} not found in the list")
    
# Deleting a character
star_wars_list.delete("Darth Vader")
print("\nStar Wars Characters after deleting:")
star_wars_list.display()
