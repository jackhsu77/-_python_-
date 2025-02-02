import datetime


import time


def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)
        return wrapper
    return decorator


@repeat(3)
def greet():
    print("Hello!")


greet()
exit()


def square(m):
    return m ** 2


a = map(square, [1, 4, 6])

t = ""
for i in a:
    t += str(i) + ","
print(t)


def sum(*a, **kwargs):
    t = 0
    print('type: '+str(type(a)))
    print('type: ' + str(type(kwargs)) + ", name=" +
          kwargs["name"] + ", age=" + str(kwargs["age"]))
    for i in kwargs:
        print(f"{i} --> {kwargs[i]}")
    for i in kwargs.items():
        print(f"key: '{i[0]}', '{i[1]}")
    for i in a:
        t += i
    return t


print("total: " + str(sum(1, 3, 5, 6, name="jack", age=50)))


def def_sort(x):
    print(x)
    return x[0]


dictionary = {'a': 3, 'c': 1, 'b': 2}
# sorted_items = sorted(dictionary.items(), key=lambda x: x[1])
sorted_items = sorted(dictionary.items(), key=def_sort)
print(sorted_items)  # 輸出: [('b', 1), ('c', 2), ('a', 3)]


a = sorted([1, 2, 35, 6], reverse=True)
print(a)
exit()


def log_log(info):
    with open("c:\\ultralog\\test1.log", "a+") as e:
        dt = datetime.datetime.now().strftime("%Y %m %d %H:%M:%S")
        dt = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        print(dt)
        e.write(info + "\n")


def Log_showdata():
    # with open("c:\\ultralog\\test1.log", "r") as e:
    with open("c:\\ultralog\\test1.log", "rb") as e:
        data = e.read(4)
        print(str(data == b'123\r'))
        data = data[1:3]
        print(data)
        for i in data:
            print(i)


log_log("test許")
Log_showdata()

a = {"a": b'1', "b": b'2'}
for i in a:
    print(a[i])
