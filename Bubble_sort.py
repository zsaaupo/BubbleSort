"""
Bubble sort
"""
print(__doc__)

class BubbleSort():

    def __init__(self, list_01 = []):
        
        self.list_01 = list_01

    def bubble_sort(self):
        i = 0
        for i in range(0, len(self.list_01)):
            j = 0
            for j in range(0, len(self.list_01) - 1 - i): #if len = 5, then len - 1 = 4 then if i = 0 or 1 then 4 - 0 or 1 = 4 or 3 

                if self.list_01[j] > self.list_01[j + 1]:

                    temp = self.list_01[j]
                    self.list_01[j] = self.list_01[j + 1]
                    self.list_01[j + 1] = temp
        
        return self.list_01


object_01 = BubbleSort([5, 4, 3, 2, 1])
print(object_01.bubble_sort())
