import time 

class TimerError(Exception):
    """A coustome exception used to report error in use of Timer class"""
    
class Timer:
    def __init__(self):
        self.start_time = None
        self.end_time   = None
        
    def start(self):
        """start a new timer"""
        if self.start_time is not None:
            raise TimerError("""Timer is running use .stop()""") 
        else:
            self.start_time = int(time.perf_counter())
            
    def stop(self):
        if self.start_time is None:
            raise TimerError("""Timer is not running use .start()""") 
        else:
            self.end_time = int(time.perf_counter()) - self.start_time
            self.start_time = None
            
    def elapsed(self):
        if self.end_time is None:
            raise("""Timer is not been run yet use .start()""")
        else:
            return(self.end_time)
        
        
         
t = Timer()

for j in range(4 , 12):
    t.start()
    n = 0
    for i in range(10**j):
        n += 1
    t.stop()
    print(j,t.elapsed())    
            
            
            