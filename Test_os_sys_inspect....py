import os
import sys
import datetime as dt
import time
import inspect
import traceback

import signal
import sys
import time

# 抓取Signal Ctrl+C
# 定義信號處理器
def signal_handler(signum, frame):
    print('Script is being terminated.')
    # 在這裡添加清理代碼
    sys.exit(0)
# 設置信號處理器
signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)
print("Script is running. Press Ctrl+C to terminate.")
# 模擬長時間運行的腳本
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    # 捕捉 Ctrl+C
    signal_handler(signal.SIGINT, None)
exit()


a = [(10,"10")]
it = iter(a)    # 將list物件變成iter物件
b = next(it)    # next()取得iterable物件的下一個元素, 當超過範圍則會有錯誤(StopIteration)
print(b)
try:
    b = next(it)
    print(b)
except Exception as e:
    print("err: " + str(e) + "," + repr(e))
    traceback.print_exc()
print("--------------------")


# enumerate, zip, unpack of tuple
d = enumerate([2,3,6,9,], start=1)
for i, v in d:
    print(i, v)
print("-----------")
d = zip([1,2,3,4,5],(1,2,3,4))
for i in d:
    #for ii, vv in i:
    #    print(ii, vv)
    ii,vv = i
    print(type(i), i, f"--> {ii}: {vv}")
print("---------------")

# def的參數為dict or tuple
def my_function_dict(**kwargs):
    print("test ** --> " + str(type(kwargs)))
    for key, value in kwargs.items():
        print(f"{key} = {value}")
def my_function_tuple(*args):
    print("test * --> " + str(type(args)))
    for value in args:
        print(f"value: {value}")
my_function_tuple(1,3,5)

# Comprehensions
squares = [x**2 for x in range(10)]
print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(even_squares)  # Output: [0, 4, 16, 36, 64]
def double(x):       # using function in it
    return x * 2
doubled = [double(x) for x in range(5)]
print(doubled)  # Output: [0, 2, 4, 6, 8]
# Nested list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [num for row in matrix for num in row]
print(flat)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
# more complex examples
results = ['even' if x % 2 == 0 else 'odd' for x in range(10)]
print(results)  # Output: ['even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd']
# combine 2 lists
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
combined = [(x, y) for x in list1 for y in list2]
print(combined)  # Output: [(1, 'a'), (1, 'b'), (1, 'c'), (2, 'a'), (2, 'b'), (2, 'c'), (3, 'a'), (3, 'b'), (3, 'c')]
# dict complehensions
keys = ['name', 'age', 'city']
values = ['Alice', 25, 'New York']
my_dict = {keys[i]: values[i] for i in range(len(keys))}
print(my_dict)  # Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}



#透過inspect可以知道function是被哪個function呼叫
def function_a():
    # 获取调用堆栈
    stack = inspect.stack()    
    # stack[1] 是直接调用者的信息
    caller_frame = stack[1]
    caller_name = caller_frame.function
    print(f"Called by: {caller_name}")
def function_b():
    function_a()
def function_c():
    function_a()
# 示例调用
function_b()  # Output: Called by: function_b
function_c()  # Output: Called by: function_c
exit()

f = open("c:\\euls\\testfile.txt", encoding="utf-8",mode="r")
a = f.readlines()
for i in a:
    print(i.strip())
print("------------")
print(a)
exit()


data = [1,2,3,4,5,6,7,8,9,0]
b = [data[i:i+3] for i in range(0, len(data),3)]
print(b)
exit()


_file = ".\\Test_pyodbc.py"
for i in enumerate(sys.argv):   # 取得 argv 參數
    print(f"argv {i[0]}: {i[1]}")
mod_time = os.path.getmtime(_file)    # 取得 檔案修改日期時間, 還有getctime, getatime
#print(time.ctime(mod_time))                         # 透過ctime轉成可以讀的字串
t = dt.datetime.fromtimestamp(mod_time)             # 透過fromtimestamp轉成datetime物件
print(t.strftime("%Y/%m/%d %H:%M:%S"), "size bytes: {0}".format(os.path.getsize(_file)))              # 映出datetime物件
print(os.path.abspath("."))     # 取得完整路徑
print(os.get_exec_path())
