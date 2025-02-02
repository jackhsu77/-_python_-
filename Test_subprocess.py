import subprocess
import datetime as dt
import sys

now = dt.datetime.now().strftime("%H:%M:%S")
print(f"start: {now}")

#command = ["python", "Test_abc.py","cmd.exe"]
#command = ["python", "Test_abc.py"]
#command = ["ping", "192.168.50.52", "-n", "10"]
command = ["ffmpeg", "-i", "C:\\UltraLog\\aaa\\M3M4_10sec_60sec.wav", "-i", "C:\\UltraLog\\aaa\\M3.wav" ,"-filter_complex", "[0:a]adelay=0|0[a000];[1:a]adelay=140000|140000[a001];[a000][a001]amix=inputs=2", "c:\\UltraLog\\aaa\\abc.wav"]

print()
process = subprocess.Popen(
    command,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True,
    #shell=True,
    bufsize=1
)

# 读取输出
#stdout, stderr = process.communicate()

# 逐行读取 stdout
while True:
    line = process.stdout.readline()                # 一次讀取1行, 搭配的.py的print要加上參數flash=True
    if line == '' and process.poll() is not None:   # .poll() is None表示程式還在執行
        break
    if line:
        print(f"read 1 Line: {line.strip()}")  # 处理每一行的输出
    #sys.stdout.flush()
    
# 确保子进程已经完成
process.wait()
# 如果需要处理错误输出，可以像下面这样处理
stderr_output = process.stderr.read()
if stderr_output:
    print("Error Output:")
    print(stderr_output)

now = dt.datetime.now().strftime("%H:%M:%S")
print(f"stop: {now}")
## 打印输出
#print("Standard Output:")
#print(stdout)
##print("Standard Error:")
##print(stderr)
