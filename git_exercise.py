"""
    Created by:     Nathan Nesbitt
    Outline:        A sorting program.
"""

# For converting to hex
import codecs

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

    def string_sort(self):
        if(type(self.array[0]) is not str):
            raise TypeError("Integer sort can only be applied to Strings.")
        
        # Basic Bubble Sort but on strings instead
        for i in range(len(self.array) - 1, 0, -1):
            for j in range(i):
                # If the first character is larger then we simply adjust
                var = 0
                # If the starting characters are the same, we run through the string until not
                if codecs.encode(str.encode(self.array[j][var]), "hex") == codecs.encode(str.encode(self.array[j + 1][var]), "hex"):
                    while(str.encode(codecs.encode(self.array[j][var]), "hex") == codecs.encode(str.encode(self.array[j + 1][var]), "hex")):
                        var += 1
                
                # Basic switch for the bubble sort
                if codecs.encode(str.encode(self.array[j][var]), "hex") > codecs.encode(str.encode(self.array[j + 1][var]), "hex"):
                    temp = self.array[j]
                    self.array[j] = self.array[j + 1]
                    self.array[j + 1] = temp                     
        # Returns the array
        return self.array
