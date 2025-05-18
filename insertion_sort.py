class InsertionSort:
    def __init__(self):
        pass

    @classmethod
    def sort(cls, lst:list):
        for i in range(1,len(lst)):
            crr=lst[i]
            j=i-1
            while j>=0 and crr<lst[j]:
                att=lst[j]
                lst[j]=crr
                lst[j+1]=att
                j-=1
        return lst


lst = [3,10,2,7,6,4,1]
print(InsertionSort.sort(lst))