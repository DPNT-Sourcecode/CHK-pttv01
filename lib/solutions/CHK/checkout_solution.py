#!/usr/local/bin/python3
import itertools

# The inventory and the prices.
inventory = { 
    'A' : { "single": 50, "multiple": [(5, 200), (3, 130)] }, 
    'B' : { "single": 30, "multiple": [(2, 45)] }, 
    'C' : { "single": 20 }, 
    'D' : { "single": 15 }, 
    'E' : { "single": 40, "free": (2, 'B', 1) },
    'F' : { "single": 10, "free": (2, 'F', 1) },
    'G' : { "single": 20 }, 
    'H' : { "single": 10, "multiple": [(10, 80), (5, 45)] }, 
    'I' : { "single": 35 }, 
    'J' : { "single": 60 }, 
    'K' : { "single": 80, "multiple": [(2, 150)] }, 
    'L' : { "single": 90 }, 
    'M' : { "single": 15 }, 
    'N' : { "single": 40, "free": (3, 'M', 1) }, 
    'O' : { "single": 10 }, 
    'P' : { "single": 50, "multiple": [(5, 200)] }, 
    'Q' : { "single": 30, "multiple": [(3, 80)] }, 
    'R' : { "single": 50, "free": (3, 'Q', 1) }, 
    'S' : { "single": 30 }, 
    'T' : { "single": 20 }, 
    'U' : { "single": 40, "free": (3, 'U', 1) }, 
    'V' : { "single": 50, "multiple": [(3, 130), (2, 90)] }, 
    'W' : { "single": 20 }, 
    'X' : { "single": 90 }, 
    'Y' : { "single": 10 }, 
    'Z' : { "single": 50 } 
}

# Function calculating the cost for one letter 
# and a number of items.
def calc_cost(key, num_items):
    '''
    Function calculating the cost for one letter 
    and a number of items.
    Args:
        key: Letter corresponding to an item.
        num_items: Number of items.
    Return:
        Integer : Cost for that product.
    '''
    cost = 0
    tmp_num_items = num_items
    if 'multiple' in inventory[key]:
        for rebate in inventory[key]['multiple']:
            num_rebates = tmp_num_items // rebate[0]
            if num_rebates:
                tmp_num_items -= num_rebates * rebate[0] 
                cost += num_rebates * rebate[1] 

    cost += tmp_num_items * inventory[key]['single'] 
    return cost
   
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
    # Our basket.
    basket = { 'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F' : 0 
              , 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L' : 0 
              , 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R' : 0 
              , 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X' : 0 
              , 'Y': 0, 'Z': 0 }
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
        cost += calc_cost(key, value)
        print("Adding for {} :: {} ==> {}".format(key, str(calc_cost(key, value)), str(cost)))

        # Here we process the free items.
        if 'free' in inventory[key]:
            num_free = 0
            if key == inventory[key]['free'][1]:
                num_free = (value // (inventory[key]['free'][0] + inventory[key]['free'][2])) * inventory[key]['free'][2]
            else:
                num_free = (value // inventory[key]['free'][0]) * inventory[key]['free'][2]
            print("{} has free {}".format(key, str(num_free)))
            if num_free and basket[inventory[key]['free'][1]] >= num_free:
                tmp = calc_cost(inventory[key]['free'][1], basket[inventory[key]['free'][1]])  
                print("Removing from cost : {}".format(str(tmp)))
                cost -= calc_cost(inventory[key]['free'][1], basket[inventory[key]['free'][1]])  
                basket[inventory[key]['free'][1]] -= num_free
                cost += calc_cost(inventory[key]['free'][1], basket[inventory[key]['free'][1]])  
            elif num_free:
                cost -= calc_cost(inventory[key]['free'][1], basket[inventory[key]['free'][1]])  

    return cost;

# Testing if we are a single program.
if __name__ == "__main__":
    my_string = "ABCDEF";
    res = checkout(my_string)
    print("Test for {} :: {}".format(my_string, str(res)))

    my_string = "FFFFFF";
    res = checkout(my_string)
    print("Test for {} :: {}".format(my_string, str(res)))

    my_string = "FFFF";
    res = checkout(my_string)
    print("Test for {} :: {}".format(my_string, str(res)))

    my_string = "FF";
    res = checkout(my_string)
    print("Test for {} :: {}".format(my_string, str(res)))

#    my_string = "AAAAAAAA";
#    res = checkout(my_string)
#    print("Test for {} :: {}".format(my_string, str(res)))

#    my_string = "ABCDEABCDE";
#    res = checkout(my_string)
#    print("Test for {} :: {}".format(my_string, str(res)))

#    my_string = "CCADDEEBBA";
#    res = checkout(my_string)
#    print("Test for {} :: {}".format(my_string, str(res)))

#    my_string = "AAADDBB";
#    res = checkout(my_string)
#    print("Test for {} :: {}".format(my_string, str(res)))

#    my_string = "AAADDBBE";
#    res = checkout(my_string)
#    print("Test for {} :: {}".format(my_string, str(res)))

#    my_string = "AAADDBBBEE";
#    res = checkout(my_string)
#    print("Test for {} :: {}".format(my_string, str(res)))

#    my_string = "AAADDBBBEEEE";
#    res = checkout(my_string)
#    print("Test for {} :: {}".format(my_string, str(res)))
        



