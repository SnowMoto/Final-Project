class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class StarWarsLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        """Create the function to insert the at the head of the list. 
        HINT: mixed current and new nodes.
        """
        pass
    
    def locate(self, name):
        """Find a character in the list using index for reference.
        """
        current = self.head
        index = 0
        pass

    def delete(self, data):
        """Create a function that can delete from the list at the head.
        HINT: While Loop is handy to locate the node.
        """
        pass

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
character = "name"
index = star_wars_list.locate(character)
if index != -1:
    print(f"{character} found at index {index}")
else:
    print(f"{character} not found in the list")

# Deleting a character
star_wars_list.delete("name")
print("\nStar Wars Characters after deleting:")
star_wars_list.display()
