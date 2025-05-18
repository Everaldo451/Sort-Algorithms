class SelectionSort:
    def __init__(self):
        pass

    @classmethod
    def sort(cls, lst:list):
        for i in range(len(lst)-1):
            min, min_idx=lst[i+1], i+1
            for j in range(i+2,len(lst)):
                if lst[j]<min:
                    min, min_idx=lst[j], j
            if min<lst[i]:
                lst[min_idx], lst[i]=lst[i], min
        return lst


lst = [3,10,2,7,6,4,1]
print(SelectionSort.sort(lst))