from functools import wraps  
def memo(func):    
    cache = {}                                  # Stored subproblem solutions  
    @wraps(func)                                # Make wrap look like func    
    def wrap(*args):                            # The memoized wrapper       
        if args not in cache:                   # Not already computed?          
           cache[args] = func(*args)           # Compute & cache the solution     
        return cache[args]                      # Return the cached solution   
    return wrap                                 # Return the wrapper

def fib(i):
    if i < 2:
        return 1

    return fib(i-1) + fib(i-2) 
