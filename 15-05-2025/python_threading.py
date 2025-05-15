from threading import Thread, Lock
import time
from queue import Queue

# multithreading is a way of achieving multitasking.

def square_number():
    for i in range(100):
        i * i
        

if __name__ == "__main__":
    threads = []
    num_threads = 10
    
    
    # create threads
    for i in range(num_threads):
        thread = Thread(target=square_number)
        threads.append(thread)
        
    # start threads
    for thread in threads:
        thread.start()
        
    # join threads: wait for them to complete
    for thread in threads:
        thread.join()
        
    print('end main')
    
    
    # example 2
    
database_value = 0
    
def increase(lock):
    global database_value
        
    with lock:
        local_copy = database_value
            
        # processing
        local_copy += 1
        time.sleep(0.1)
        database_value = local_copy
        
        
        
if __name__ == "__main__":
    
    lock = Lock()
    print("start value", database_value)
    
    thread1 = Thread(target=increase, args=(lock,))
    thread2 = Thread(target=increase, args=(lock,))
    
    thread1.start()
    thread2.start()
    
    thread1.join() 
    thread2.join()
    
    print('end value', database_value)
    
    print('end main')
    

if __name__ == "__main__":
    
    q = Queue()
    q.put(1)
    q.put(2)
    q.put(3)
    
    first = q.get()
    print(first)
    
    q.task_done()
    q.join()
    
    
import time
from threading import Thread

def task():
    print("Start task")
    time.sleep(3)
    print("Task done")

# Create threads
t1 = Thread(target=task)
t2 = Thread(target=task)

# Start threads
t1.start()
t2.start()

# Wait for them to finish
t1.join()
t2.join()
