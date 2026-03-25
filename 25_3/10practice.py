# List Comprehension 
my_list = [x**2 for x in range(1000000)] 

# Generator Expression 
my_gen = (x**2 for x in range(1000000)) 

# print(next(my_gen)) # 0
# print(next(my_gen)) # 1
# print(next(my_gen)) # 4
# print(next(my_gen)) # 9
# print(next(my_gen)) # 16
# print(next(my_gen)) # 125
# print(next(my_gen)) # 36
# print(next(my_gen)) # 49
# print(next(my_gen)) # 64
# print(next(my_gen)) # 1
# print(next(my_gen)) # 1

def fibonacci_gen(n:int):
    current,previous = 0,1
    while True :
        yield current
        current,previous = previous+current,current


# fib = fibonacci_gen(10)
# for _ in range(10):
#     print(next(fib))


raw_logs = [
    "2026-03-25 10:01:05 INFO User 'armaan' logged in",
    "2026-03-25 10:02:15 ERROR Database connection timeout",
    "2026-03-25 10:05:00 INFO Uploading file to AWS S3",
    "2026-03-25 10:06:30 WARNING Disk usage at 85%",
    "2026-03-25 10:08:12 ERROR Failed to initialize Docker container",
    "2026-03-25 10:10:05 INFO System update complete",
    "2026-03-25 10:12:45 ERROR Unauthorized access attempt at /admin",
    "2026-03-25 10:15:20 INFO Heartbeat signal received"
]

def logs_filter(raw_logs:list):
    for log in raw_logs:
        if "ERROR".casefold() in log.casefold():
            yield log

gen_log = logs_filter(raw_logs)

upper_logs = (log.upper() for log in gen_log)

# 3. Consuming the pipeline
for log in upper_logs:
    print(log)



def window_generator(data, size):
    for i in range(size):
        yield data[i:i+size]

numbers = [10, 20, 30, 40, 50, 60]
for window in window_generator(numbers, 5):
    print(window)