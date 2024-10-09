'''
This sorting algorithm maintains a sub-array that is always sorted. 
Values from the unsorted part of the array are placed at the 
correct position in the sorted part
'''


def insertion_sort(arr):
    '''
    params: list of integers

    Sequence: 7, 2, 1, 6
    (7, 2, 1, 6) –> (2, 7, 1, 6), In the first iteration, 
    the first 2 elements are compared, here 2 is less 
    than 7 so insert 2 before 7.
    
    (2, 7, 1, 6) –> (2, 1, 7, 6), In the second iteration the 
    2nd and 3rd elements are compared, here 1 is 
    less than 7 so insert 1 before 7.
    
    (2, 1, 7, 6) –> (1, 2, 7, 6), After the second iteration 
    (1, 7) elements are not in ascending order so first 
    these two elements are arranged. So, insert 1 before 2. 
    
    (1, 2, 7, 6) –> (1, 2, 6, 7), During this iteration the last 2 
    elements are compared and swapped after all the previous 
    elements are swapped.

    return: Sorted list of integers
    '''
    pass



if __name__ == '__main__':
    arr = [7, 2, 1, 6] 
    insertion_sort(arr)
