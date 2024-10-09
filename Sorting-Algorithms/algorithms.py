"""
Algorithms Script to find sorting using different algorithms
"""

class Algorithms:
    def __init__(self, arr) -> None:
        print("arr to be sort     :: ", arr)
        self.arr = arr
        self.arr_count = len(self.arr)

    def sorted_algorithms(self):
        
        print("Bubble Sort Result :: ", self.bubble())

    def bubble(self) -> list[int]: 
        """
        params: list of integers
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
