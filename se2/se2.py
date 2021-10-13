"""
CS 121
Short Exercises #2
"""

def peep(p, e):
    """
    Determine whether or not peep = pp^e

    Inputs:
      p (int): first digit
      e (int): second digit

    Returns: True if peep = pp^e, False otherwise
    """

    ### EXERCISE 1 -- Replace pass with your code
    n=1000*p+100*e+10*e+p
    If n == (11p)^e:
        return True
    else:
        return False
 
def has_more(lst1, lst2, target):
    """
    Determine which list contains more of the target value

    Inputs:
      lst1 (list): first list
      lst2 (list): second list
      target: the target value

    Returns: True if lst1 contains more of target, False otherwise
    """

    ### EXERCISE 2 -- Replace pass with your code
    lst1 = []
    lst2 = []
    m = 0 
    n = 0

   for i in lst1:
       if i == target:
          m += 1
   for i in lst2:
       if i == target:
          n += 1
   if m>n:
       return True
   else:
       return False

def make_star_strings(lst):
    """
    Create a list of star strings

    Input:
      lst (list of nonnegative integers): the list

    Returns: A list of strings of stars (*)
    """

    ### EXERCISE 3 -- Replace pass with your code
    star = '*'
    star_list = []
    for i in list_input:
        i_star = i*star
        star_list.append(i_star)
    return star_list

def replace(lst, replacee, replacer):
    """
    Replace one element in a list with another

    Input:
      lst (list): the list
      replacee: the element to replace
      replacer: the element to replace replacee with

    Returns: None, modifies lst in-place
    """

    ### EXERCISE 4 -- Replace pass with your code
    if replacee in lst:
        for replacee in lst:
            replacee == replacer
            return lst
    else:
            return None
    

def rows_and_columns_contain(lst, target):
    """
    Determines whether every row and every column of a list
      of lists contains a target value

    lst (list of lists): the list of lists
    target: the target value

    Returns: True if every row and every column of lst contains
      target, False otherwise
    """

    ### EXERCISE 5 -- Replace pass with your code
    pass
