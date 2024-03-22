# Below is a simple example of Stack implementation using a list.

pancake = []

# Add topings using the append() function 
# to push element in the stack
def add_toppings(pancake):
    pancake.append('blueberry')
    pancake.append('huckleberry')
    pancake.append('chocolate chips')
    return pancake

print('Pancake toppings:', add_toppings(pancake))

# Now going to see how many items are not in the stack using len.
print('How many toppings are in the list:', len(pancake))

# Pop function to remove unwanted toppings from the stack and show only the desired.
# There are several ways to do this, but I will show a simple 2 ways.
def remove_all(pancake):
    pancake.pop()
    pancake.pop()
    pancake.pop()
    return pancake
print("\nAll of the toppings are removed using Pop.")

# OR Create an if statement to select one topping.

def sub_pancake(pancake):
    if len(pancake) == 0:
            print("There are no toppings left.")
    else:
        return pancake.pop(1)
        
print("\nFavorite pancake topping: ", sub_pancake(pancake))
print("\nWhat was removed:", pancake)