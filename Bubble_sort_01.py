"""
Bubble sort
"""
print(__doc__)

class BubbleSort:

    def bubble_sort(self, list_02 = []):
        n = len(list_02)
        for i in range(0, n):
            print("Loop 1 has looped for ", i," times")
            if i == 1:
                break
            for j in range(0, n - 1 - i):

                if list_02[j] > list_02[j + 1]:

                    swap_01 = list_02[j]
                    list_02[j] = list_02[j + 1]
                    list_02[j + 1] = swap_01
                print("Loop 2 has looped for ", j, "Times")

                

        return list_02



if __name__ == "__main__":

    object_02 = BubbleSort()
    list_new = [1, 2, 3, 4, 5, 7, 6]
    print(object_02.bubble_sort(list_new))