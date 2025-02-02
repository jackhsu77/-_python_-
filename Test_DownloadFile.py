import os
import sys

""" # 這樣可以讓瀏覽器直接開啟撥放軟體
print("Status: 200 OK", flush=True)
print("Content-Transfer-Encoding: Binary",flush=True)
filepath = "D:\\UltraLog\\Media\\3_20231127201246.wav"
filesize = os.path.getsize(filepath)
with open(filepath, "br") as src:
    buf = src.read()
print('Content-Type: audio/wav') 
print('Content-Length: '+str(filesize)) 
print(flush=True)
sys.stdout.buffer.write(buf)        # 一定要搭配 print("Status: 200 OK", flush=True) print("Content-Transfer-Encoding: Binary",flush=True)
sys.stdout.flush()
exit() 
"""

# 讓瀏覽器跳出存檔視窗下載
# print 可以改用stdout.write 但要加上\r\n, 最後一行要2個\r\n
filepath = "D:\\UltraLog\\Media\\3_20231127201246.wav"
filename = "abc" + os.path.basename(filepath)
print('Content-type: application/octet-stream', flush=True)
print('Content-Transfer-Encoding: Binary', flush=True)
print(f'Content-disposition: attachment; filename={filename}' , flush=True)
print(flush=True)

if os.path.exists(filepath):
    fp = open(filepath, "rb")
    #filesize = os.path.getsize(filepath)
    data=fp.read()
    sys.stdout.buffer.write(data)
    sys.stdout.flush()
    fp.close()
else:
    sys.stdout.buffer.write(f"not found file: {filepath}".encode())
    sys.stdout.flush()
exit()