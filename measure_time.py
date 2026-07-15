import time 

#in term of class and object 
class timer:
    def __init__(self):
        self.start_time = 0
        self.end_time   = 0
        
    def start(self):
        self.start_time = time.perf_counter()
        
    def end(self):
        self.end_time = time.perf_counter() - self.start_time
        
    def elapsed(self):
        return(self.end_time)

#simple 
start = int(time.perf_counter())

#execute some code

end = int(time.perf_counter())

elapsed = end - start

print(elapsed)