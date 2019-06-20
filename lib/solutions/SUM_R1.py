#!/usr/local/bin/python3


# Define a function that receives two parameters
# and return the sum. The parameters should be 
# between 0 and 100.
def sum(val1, val2):
    '''
    Function returning the sum of two parameters.
    Args:
        val1 : Integer between 0 and 100.
        val2 : Integer between 0 and 100.
    Return:
        Integer : Sum of val1 and val2.
    '''
    return val1 + val2;

if __name__ == '__main__':
   # Tests.
   print("1 + 3 = {}".format(sum(1,3)))
   print("0 + 0 = {}".format(sum(0,0)))
