"""
Algorithms Script to find sorting using different algorithms
"""

class Algorithms:
    def __init__(self, arr) -> None:
        print("arr to be sort :: ", arr)
        self.arr = arr
        self.arr_count = len(self.arr)

    def sorted_algorithms(self):
        print("Bubble Sort Result :: ", self.bubble())

    def bubble(self) -> list[int]: 
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
        for i in range(self.arr_count):
            for j in range(self.arr_count -i -1):
                if self.arr[j] > self.arr[j+1]:
                    self.arr[j], self.arr[j+1] = self.arr[j+1], self.arr[j]
        return self.arr


if __name__ == '__main__':
    arr = [ 2, 1, 10, 23 ]
    algo = Algorithms(arr)
    algo.sorted_algorithms()