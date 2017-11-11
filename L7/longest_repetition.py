# Question 8: Longest Repetition

# Define a procedure, longest_repetition, that takes as input a 
# list, and returns the element in the list that has the most 
# consecutive repetitions. If there are multiple elements that 
# have the same number of longest repetitions, the result should 
# be the one that appears first. If the input list is empty, 
# it should return None.
def longest_repetition(input_list):
    best=None
    length=0
    current=None
    current_length=0
    for e in input_list:
        if current!=e:
            current=e
            current_length=1
        else:
            current_length+=1
        if current_length>length:
            best=current
            length=current_length
    return best

def longest_repetition(input_list):
    best=None
    length=0
    current=None
    current_length=0
    for e in input_list:
        if current!=e:
            if current_length>length:
                best=current
                length=current_length
            current=e
            current_length=1
        else:
            current_length+=1
    
    if current_length>length:
        best=current
        length=current_length   
    return best

def longest_repetition1(l):# TypeError:nested list
    if len(l)==0:
        return None
    ret={}
    i=1
    count=1
    ret[l[0]]=1
    while i<len(l):
        if l[i] in ret:
            if l[i]==l[i-1]:
                count+=1
            else:
                if count>ret[l[i-1]]:
                    ret[l[i-1]]=count
                    count=1
        else:
            if count>ret[l[i-1]]:
                ret[l[i-1]]=count
                count=1
            ret[l[i]]=1
        i+=1
    if count>ret[l[i-1]]:
        ret[l[i-1]]=count
    keys=ret.keys()
    max=keys[0]
    for key in ret:
        if ret[key]>ret[max]:
            max=key
    return max
    




#For example,

print longest_repetition([1, 2, 2, 3, 3, 3, 2, 2, 1])
# 3

print longest_repetition(['a', 'b', 'b', 'b', 'c', 'd', 'd', 'd'])
# b

print longest_repetition([1,2,3,4,5])
# 1

print longest_repetition([])
# None

