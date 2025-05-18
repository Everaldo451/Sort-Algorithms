class SelectionSort:
    def __init__(self):
        pass

    @classmethod
    def sort(cls, lst:list):
        for i in range(len(lst)-1):
            min=lst[i+1]
            min_idx=i+1
            for j in range(i+2,len(lst)):
                if lst[j]<min:
                    min=lst[j]
                    min_idx=j
            if min<lst[i]:
                current=lst[i]
                lst[i]=min
                lst[min_idx]=current
        return lst


lst = [3,10,2,7,6,4,1]
print(SelectionSort.sort(lst))