


def partition(l:int,h:int,arr)->int:
    # print(l,h)
    pivot = arr[h]
    i=l-1
    for j in range(l,h):
        if arr[j]<=pivot:
            i+=1
            arr[j],arr[i]=arr[i],arr[j]
    arr[i+1],arr[h]=arr[h],arr[i+1]
    return i+1

def quick_sort(l:int,h:int,arr)->None:
    # print(arr)
    if l>=h:
        return
    pi = partition(l,h,arr)
    print(pi,l,h,arr)
    quick_sort(l,pi-1,arr)
    quick_sort(pi+1,h,arr)


arr = [1,3,2,10,4,8,5,21,6]
quick_sort(0,len(arr)-1,arr)
print(arr)


