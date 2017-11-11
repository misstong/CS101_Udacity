def partition(urls,low,high):
    pivot=urls[low]
    i=low
    j=high
    while i<j:        
        while i<j and urls[j]>pivot:
            j-=1
        while i<j and urls[i]<=pivot:
            i+=1
        urls[i],urls[j]=urls[j],urls[i]         
    urls[low],urls[j]=urls[j],urls[low]  
    return j
    

def quicksort(urls,low,high):
    if low>=high:
        return 
    p=partition(urls,low,high)
    quicksort(urls,low,p-1)
    quicksort(urls,p+1,high)


a=[5,3,2,7,3,5]
quicksort(a,0,5)
print partition(a,0,5)
print a
