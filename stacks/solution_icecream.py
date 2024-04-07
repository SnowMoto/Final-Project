#You are at the ice cream shop to create the best cone ever. BUT
#there is a limit of 3 scoops of ice cream. Below is your 
#empty stack to use.

icecream_cone = ["chocolate chip", "cookie dough"]

def add_icecream(icecream_cone):
    """Add one of your favorite ice cream combo to the stack. 
    """
    icecream_cone.append('chocolate huckleberry')
    return icecream_cone

def remove_icecream(icecream_cone, num=1):
    """Now choose to remove all the ice cream from the stack using LIFO 
    or pick 2 scoops of ice cream."""
    
    if len(icecream_cone) == 0:
        print("You don't want icecream?")
    else:
        return icecream_cone.pop(0) #this can be blank or use the index # to select.

#--- Test --- #

print('Favorite ice cream:', add_icecream(icecream_cone))
print('How many ice creams are in the stack:', len(icecream_cone))

print("\nHere are your 2 scoops of ice cream:", icecream_cone)
print("\nIce cream removed: ",remove_icecream(icecream_cone))
