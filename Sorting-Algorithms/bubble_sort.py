'''
Bubble Sort is a simple sorting algorithm. This sorting algorithm 
repeatedly compares two adjacent elements and swaps them if they are in 
the wrong order. 
'''


def bubble_sort(arr):
    """
    params: list of integers

    Sequence: 2, 23, 10, 1
    First Iteration
    (2, 23, 10, 1) –> (2, 23, 10, 1), Here the 
    first 2 elements are compared and remain the same because they 
    are already in ascending order.

    (2, 23, 10, 1) –> (2, 10, 23, 1), Here 
    2nd and 3rd elements are compared and 
    swapped(10 is less than 23) according to ascending order.

    (2, 10, 23, 1) –> (2, 10, 1, 23), Here 
    3rd and 4th elements are compared and 
    swapped(1 is less than 23) according to ascending order

    At the end of the first iteration, the largest 
    element is at the rightmost position which is sorted correctly.

    Second Iteration
    (2, 10, 1, 23) –> (2, 10, 1, 23), Here again, the 
    first 2 elements are compared and remain the 
    same because they are already in ascending order.

    (2, 10, 1, 23) –> (2, 1, 10, 23), Here 2nd and 3rd 
    elements are compared and 
    swapped(1 is less than 10) in ascending order.

    At the end of the second iteration, the second largest 
    element is at the adjacent position to the largest element.

    Third Iteration
    (2, 1, 10, 23) –> (1, 2, 10, 23), Here the first 2 elements 
    are compared and swap according to ascending order.

    The remaining elements are already sorted in the 
    first and second Iterations. After the three iterations, 
    the given array is sorted in ascending order. 
    So the final result is 1, 2, 10, 23.

    self.arr[j] > self.arr[j+1] return Assending Order
    self.arr[j] < self.arr[j+1] return Decsending Order

    return: Sorted list of integers
    """

    for i in range(len(arr)):
        for j in range(0, len(arr) - i -1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


if __name__ == '__main__':
    arr = [ 2, 1, 10, 23 ]
    print(bubble_sort(arr))
