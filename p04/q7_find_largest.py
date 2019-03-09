alist = [5, 1, 8, 7, 2]
def find_largest(alist):
    if len(alist)==1:
        return alist[0]
    elif alist[len(alist)-1]>alist[0]:
        return find_largest(alist[1:])
    else:
        return find_largest(alist[:-1])
    
find_largest(alist)
        
