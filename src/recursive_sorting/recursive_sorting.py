# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(l, r): # assuming l=[2] & r=[1,3]
    m_arr=[]
    x,y = 0,0
    if l[-1]<r[0]:
        return l+r 
    elif r[-1]<l[0]:
        return r+l
    while x<=len(l) and y<=len(r):
        if x==len(l):
            m_arr=  m_arr + r[y:]
            break 
        elif y==len(r):
            m_arr = m_arr + l[x:]
            break
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
        return merge(merge_sort(l),merge_sort(r))
    return arr


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
