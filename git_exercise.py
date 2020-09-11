"""
    Created by:     Nathan Nesbitt
    Outline:        A sorting program.
"""

class Sort:

    def __init__(self, default_array):
        self.array = default_array

    def interger_sort(self):
        """
            A implementation of bubble sort
        """

        # Checks to see if the list type is of type int
        if(type(self.array[0]) is not int):
            raise TypeError("Integer sort can only be applied to integers.")
        
        # Basic Bubble Sort  
        for i in range(len(self.array) - 1, 0, -1):
            for j in range(i):
                if self.array[j] > self.array[j + 1]:
                    temp = self.array[j]
                    self.array[j] = self.array[j + 1]
                    self.array[j + 1] = temp                     
        
        # Returns the array
        return self.array
