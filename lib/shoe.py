#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self._size = 0
        self.size = size  # This will trigger the setter
        self.color = None
        self.condition = None
        
    @property
    def size(self):
        return self._size
        
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            print("size must be an integer")
        else:
            self._size = value
            
    def change_color(self, color):
        self.color = color
        
    def cobble(self):
        print("Your shoe is as good as new!")  # Changed the message to match the expected output
        self.condition = "New"
    pass