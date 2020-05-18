import time
import threading

start = time.perf_counter()


def do_something(seconds):
    print("About to sleep")
    time.sleep(seconds)
    print(f"Slept for {seconds} second(s)")
thread = []
for _ in range(5):
    t = threading.Thread(target= do_something(_))
    t.start()
    thread.append(t)

for t in thread:
    t.join()

end = time.perf_counter()

print(f"Execution time is {round(end - start , 2)} seconds")