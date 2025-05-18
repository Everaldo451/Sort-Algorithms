class InsertionSort:
    def __init__(self):
        pass

    @classmethod
    def sort(cls, lst:list):
        for i in range(1,len(lst)):
            crr=lst[i]
            j=i-1
            while j>=0 and crr<lst[j]:
                lst[j+1] = lst[j]
                j-=1
            lst[j+1]=crr
        return lst


lst = [3,10,2,7,6,4,1]
print(InsertionSort.sort(lst))