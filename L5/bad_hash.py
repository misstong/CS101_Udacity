def bad_hash_string(keyword,buckets):
    return ord(keyword[0])%buckets

def test_hash_function(func,keys,size):
    results=[0]*size
    keys_used=[]
    for w in keys:
        if w not in keys_used:
            hw=func(w,size)
            results[hw]+=1
            keys_used.append(w)
    return results

def better_hash_string(keyword,buckets):
    n=0
    for c in keyword: #  loop in string
        n+=ord(c)
    return n%buckets
        
