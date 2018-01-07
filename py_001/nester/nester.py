import sys

def print_lol(the_list, indenet=False, level=0, fn=sys.stdout):
    """recurrence"""
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item, indenet, level+1, fn)
        else:
            if indenet:
                for tab_stop in range(level):
                    print ("\t" *level, fn)
            print(each_item, fn)
