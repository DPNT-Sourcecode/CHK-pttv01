#!/usr/local/bin/python3
import itertools

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    '''
    Function calculating the total checkout of the skus provided.
    Arg:
       skus : String containing all the skus of the basket.
    Return:
       Integer : Total checkout value of the items or -1.
    '''
    # Let's split the string so we can have each on of the item in the basket. 
    # Each of the item should be a single letter. If not return -1.
    # The inventory and the prices.
    inventory = { 
        'A' : { "single": 50, "multiple": (3, 130) }, 
        'B' : { "single": 30, "multiple": (2, 45) }, 
        'C' : { "single": 20 }, 
        'D' : { "single": 15 }, 
        'E' : { "single": 40, "free": {2, 'B', 1} } 
    }
    # Our basket.
    basket = { 'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0 }
    # We parse the string to be sure every SKU is an existing letter.
    for one_sku in skus:
        if one_sku not in basket:
            return -1
        basket[one_sku] += 1
    # Now we do the calculation.
    cost = 0;
    for key, value in basket.items():
        # If there is a mulitple inside the inventory for the corresponding 
        # letter (i.e. key) we have to separate the different way of calculating.
        if 'multiple' in inventory[key]:
            remain = value % inventory[key]['multiple'][0]
            cost += remain * inventory[key]['single'] 
            cost += ((value - remain) / inventory[key]['multiple'][0]) * inventory[key]['multiple'][1]  
        else:
            cost += value * inventory[key]['single'] 
        # Here we process the free items.
        if 'free' in inventory[key]:
            num_free = (value // inventory[key]['free'][0]) * inventory[key]['free'][2]
            if inventory[key]['free'][2] 

    return cost;

# Testing if we are a single program.
if __name__ == "__main__":
    my_string = "ABCDE";
    res = checkout(my_string)
    if res == -1:
        print("Bad values checked.")
    else:
        print("Bad values failed.")
    my_string = "AAA";
    res = checkout(my_string)
    if res == -1:
        print("Good values failed : {}.".format(str(res)))
    else:
        print("Good values checked : {}.".format(str(res)))
    my_string = "AAADDBB";
    res = checkout(my_string)
    if res == -1:
        print("Good values failed : {}.".format(str(res)))
    else:
        print("Good values checked : {}.".format(str(res)))
        

