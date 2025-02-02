import threading
import time

def def_worker(event):
    print("Worker thread is waiting for event...")
    print(f"event: {event}")
    
    print("Worker thread received the event!")
    
event = threading.Event()

# 创建并启动工作线程

thread1 = threading.Thread(target=def_worker, args=[123])
thread1.start()

print("Main thread is sleeping...")
time.sleep(2)  # 主线程等待一段时间

print("Main thread is setting the event...")
event.set()  # 设置事件标志为True

# 等待工作线程结束
thread1.join()
print("Main thread finished.")
exit()