#!/usr/bin/python3
'''
MyList Class
'''


class MyList(list):
    '''
    Subclass of list
    '''
    def print_sorted(self):
        '''
        prints list in ascending sort
        '''
        print(sorted(self))
