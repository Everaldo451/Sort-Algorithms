class BubbleSort:
    def __init__(self):
        pass

    @classmethod
    def sort(cls, lst:list):
        for i in range(len(lst)-1, 0, -1):
            for j in range(i):
                if lst[j+1]<lst[j]:
                    lst[j], lst[j+1] = lst[j+1], lst[j]
        return lst


lst = [10,3,2,7,6,4,1]
print(BubbleSort.sort(lst))