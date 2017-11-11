import time

def time_execution(code):
    start=time.clock()
    result=eval(code)
    runtime=time.clock()-start
    return result,runtime

def spin_loop(n):
    i=0
    while i<n:
        i+=1
