import time

def log(func):
    def wrapper(*args,**kw):
        start_time = time.time()
        func(*args, **kw)
        stop_time = time.time()
        t = stop_time - start_time
        print('%s excuted in %s ms.' %(func.__name__,t))
        return func(*args, **kw)
    return wrapper

@log
def count(x,y):
    time.sleep(0.314)
    return x*y


a = count(1,2)