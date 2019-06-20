#!/usr/local/bin/python3

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
    list_of_sku = skus.split()
    # We parse the string to be sure every SKU is a single letter.
    for one_sku in list_of_sku:
        if len(one_sku) != 1:
            return -1
    return 0;

# Testing if we are a single program.
if __name__ == "__main__":
    my_string = "A B C DE";
    if checkout(my_string) == -1:
        print("Bad values checked.")
    else:
        print("Bad values failed.")
    my_string = "A B C D";
    if checkout(my_string) == -1:
        print("Good values failed.")
    else:
        print("Good values checked.")
        
