
import json
a ={}
a["a"] = 123
a["b"] = dict()
a["b"]["b_1"] = "b_1"
a["b"]["b_2"] = {}
a["b"]["b_2"]["b_2_1"] = "11111"
a["b"]["b_2"]["b_2_2"] = "222"
print(a)
print(json.dumps(a))
b = json.loads(json.dumps(a))
with open(".\\a.txt", "a") as e:
    e.write(str(b))

print(list(map(lambda x: x+10,[1,2,3])))
print(list(filter(lambda x: x%2==1, [1,3,3,4,5,6,7])))
print("----------------------")
#for i in a.values():
#    print(i, dir(type(i)))

class cls_a:
    address: str
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def address_get(self):
        return self.__class__.address
    
c1 = cls_a("jack", 50)
c2 = cls_a("tom",30)
c1.__class__.address = "new taipei"
print(f"c1: {c1.name}, {c1.age}, {c1.address}, {c1.address_get()}")
print(f"c2: {c2.name}, {c2.age}, {c2.address}, {c2.address_get()}")
exit()


import time
print(time.ctime())
a = time.time()
print(time.localtime().tm_mon, time.localtime().tm_mday, time.localtime().tm_hour, time.localtime().tm_min, time.localtime().tm_sec)
time.sleep(1.238)
print(round(time.time()-a, 2))


exit()

#下載檔案
from smb.SMBConnection import SMBConnection
# Samba 伺服器的連接資訊
#server_ip = '127.0.0.1'
server_ip = '192.168.31.180'
#server_ip = 'localhost'
shared_folder = 'euls'
username = 'jackhsu'
password = '3137hsu'
client_name = 'your_client_name'  # 任意定義的名稱
server_name = 'jack-jacky-hsu'  # Samba 伺服器的 NetBIOS 名稱
# 建立與 Samba 伺服器的連接
conn = SMBConnection(username, password, client_name, server_name, use_ntlm_v2=True)
try:
    conn.connect(server_ip, 139)
except Exception as e:
    print("139 port Err: " + str(e))
# 下載檔案
remote_file_path = '2.jpg'
local_file_path = 'c:\\euls\\2_from_smb.jpg'
with open(local_file_path, 'wb') as file_obj:
    conn.retrieveFile(shared_folder, remote_file_path, file_obj)
print(f"file download complete: {local_file_path}")

# 上傳檔案
remote_file_path = 'test_f\\upload.jpg'
#with open(local_file_path, 'rb') as file_obj:
#    conn.storeFile(shared_folder, remote_file_path, file_obj)
#print(f"file upload complete: {remote_file_path}")


# 檢查檔案是否存在
# 必須先列出要尋找目錄下的所有檔案後, 再用for找到你要的檔案
try:
    '''
    files = conn.listPath(shared_folder, "1.jpg")
    if files:
        print(f"file exist: {remote_file_path}")
    else:
        print(f"file not exist: {remote_file_path}")
    '''
    for file in conn.listPath(shared_folder, '/test_f'):
        if (file.filename != ".") and (file.filename != ".."):
            print(file.filename, type(file))
except Exception as e:
    print(f"file not exist: {remote_file_path}, err: {e}")

exit()
# 刪除檔案
try:
    conn.deleteFiles(shared_folder, remote_file_path)
    print(f"file is deleted：{remote_file_path}")
except Exception as e:
    print(f"file can't delete：{remote_file_path}, err: {e}")
# 關閉連接
conn.close()

