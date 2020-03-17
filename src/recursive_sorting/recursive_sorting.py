# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(l, r):
    m_arr=[]
    x,y = 0,0
    while x<len(l) and y<len(r):
        if l[-1]<r[0]:
            return l+r 
        elif r[-1]<l[0]:
            return r+l
        elif l[x]<r[y]:
            m_arr.append(l[x])
            x += 1
        elif l[x]>r[y]:
            m_arr.append(r[y])
            y += 1
        elif l[x]==r[y]:
            m_arr.append(l[x])
            m_arr.append(r[y])
            x += 1
            y += 1
    return m_arr

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO
    if len(arr)>1:
        sep = len(arr)//2
        l = arr[:sep] 
        r = arr[sep:]
        print(l,r)
        arr = merge(merge_sort(l),merge_sort(r))
        print(arr)
        return arr 
    return arr

test = [2,1,3,8,7,6,5]


# test = [0,3,2,5,4,7,6,9,8,10]
print(merge_sort(test))


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
