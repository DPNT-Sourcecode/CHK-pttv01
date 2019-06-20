#!/usr/local/bin/python3

# noinspection PyUnusedLocal
# friend_name = unicode string
def hello(friend_name):
    ''' 
    Method returning a string saying hello to 
    the name provided as parameter.
    Arg:
        friend_name : Name to say hello to.
    Return:
        String saying : Hello friend_name.
    '''
    return "Hello, World!"

if __name__ == '__main__':
    print("{}".format(hello("Bruno")))
    print("{}".format(hello("")))



