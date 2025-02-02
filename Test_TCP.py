import socket
import sys

'''
import urllib.parse
def urlencode_string(input_string):
    return urllib.parse.quote(input_string)
#https://asr-mts.yubian.com.tw/resource/files/AXnsWs_hFwJvYlFHUIQ8V0zONyWkPPX-6_QQd-a2kzSx9T685Lw0WgUkn02F-T8veLBlN1Up7afN1cMTnAIWNapTLgqalvCSwF5kNO85EtAL0vCsX2kprwJbA_PduNIq/20220518134049_script.txt?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzUxMiJ9.eyJzdWIiOiJ5YnRlc3RfdW5pc29vbiIsImF1ZCI6ImFzci1zZXJ2aWNlLmJyb25jaS5jb20udHciLCJjYXBhYmlsaXR5IjoyLCJyb2xlIjoidXNlciIsIm5pY2tuYW1lIjoieWJ0ZXN0X3VuaXNvb24iLCJwZXJtcyI6WyJzeXNfc3RhdHVzIiwidGFza19hc3NpZ24iLCJ0YXNrX21uZ3IiXSwiZXhwIjoxNzIwNDQ2NTg5LCJqdGkiOiIyNGQ5NzFiMi0zNDM3LTQ5M2MtODUwMS1hMDA5MzIwMzQ2ZDYiLCJ0aW1lc3RhbXAiOjE3MjA0MTc3ODk4ODN9.AeepPBji4k87Jx0-FC3iaN4Ayx3h0XnVQZgjklXC6vk3HNmW4gHZYwkdezNoBhfhbbwvNnEchvhtDwDHsLs8voqWACk5Z9vrr8CteUF3fAcaQKxXU9j_8jEdcswcOTPwL0m3fXvi7EGOlod_Zkyt3eQf-q-FwhnG-kqfZclQtK8pKSrN
#https://asr-mts.yubian.com.tw/resource/files/AXnsWs_hFwJvYlFHUIQ8V0zONyWkPPX-6_QQd-a2kzSx9T685Lw0WgUkn02F-T8veLBlN1Up7afN1cMTnAIWNapTLgqalvCSwF5kNO85EtAL0vCsX2kprwJbA_PduNIq/20220518134049_script.txt?token=
#               eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzUxMiJ9.eyJzdWIiOiJ5YnRlc3RfdW5pc29vbiIsImF1ZCI6ImFzci1zZXJ2aWNlLmJyb25jaS5jb20udHciLCJjYXBhYmlsaXR5IjoyLCJyb2xlIjoidXNlciIsIm5pY2tuYW1lIjoieWJ0ZXN0X3VuaXNvb24iLCJwZXJtcyI6WyJzeXNfc3RhdHVzIiwidGFza19hc3NpZ24iLCJ0YXNrX21uZ3IiXSwiZXhwIjoxNzIwNDQ2NTg5LCJqdGkiOiIyNGQ5NzFiMi0zNDM3LTQ5M2MtODUwMS1hMDA5MzIwMzQ2ZDYiLCJ0aW1lc3RhbXAiOjE3MjA0MTc3ODk4ODN9.AeepPBji4k87Jx0-FC3iaN4Ayx3h0XnVQZgjklXC6vk3HNmW4gHZYwkdezNoBhfhbbwvNnEchvhtDwDHsLs8voqWACk5Z9vrr8CteUF3fAcaQKxXU9j_8jEdcswcOTPwL0m3fXvi7EGOlod_Zkyt3eQf-q-FwhnG-kqfZclQtK8pKSrN
#               eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzUxMiJ9.eyJzdWIiOiJ5YnRlc3RfdW5pc29vbiIsImF1ZCI6ImFzci1zZXJ2aWNlLmJyb25jaS5jb20udHciLCJjYXBhYmlsaXR5IjoyLCJyb2xlIjoidXNlciIsIm5pY2tuYW1lIjoieWJ0ZXN0X3VuaXNvb24iLCJwZXJtcyI6WyJzeXNfc3RhdHVzIiwidGFza19hc3NpZ24iLCJ0YXNrX21uZ3IiXSwiZXhwIjoxNzIwNTM3NTg2LCJqdGkiOiIyNGQ5NzFiMi0zNDM3LTQ5M2MtODUwMS1hMDA5MzIwMzQ2ZDYiLCJ0aW1lc3RhbXAiOjE3MjA1MDg3ODYzMTh9.ABhzvt337Jy3tUIkZP-35tVIAVxNufpN40C-j7EC6vP1NEUFHzeX0_eUI0zb_hj5nNS2_XmaUvQqOlQ4Y5UbSJDIAIG-uGF68hPDq_LPFcBvnQVA3zHO2xxDb44lKOWih8iXpyT3mEIEquLhN6IAO3H-Y8CzFgStUGy_mkBCJp-VnvDD
#https://asr-mts.yubian.com.tw/resource/files/AXnsWs_hFwJvYlFHUIQ8VwfWDJHEAJFcFQft3JzGpG0vdC2dHxNDkT8sqTLqjxckeLBlN1Up7afN1cMTnAIWNapTLgqalvCSwF5kNO85EtCAS6TWEy4YI5o--Z95PLug/20220518134049_caption.srt?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzUxMiJ9.eyJzdWIiOiJ5YnRlc3RfdW5pc29vbiIsImF1ZCI6ImFzci1zZXJ2aWNlLmJyb25jaS5jb20udHciLCJjYXBhYmlsaXR5IjoyLCJyb2xlIjoidXNlciIsIm5pY2tuYW1lIjoieWJ0ZXN0X3VuaXNvb24iLCJwZXJtcyI6WyJzeXNfc3RhdHVzIiwidGFza19hc3NpZ24iLCJ0YXNrX21uZ3IiXSwiZXhwIjoxNzIwNDQ2NTg5LCJqdGkiOiIyNGQ5NzFiMi0zNDM3LTQ5M2MtODUwMS1hMDA5MzIwMzQ2ZDYiLCJ0aW1lc3RhbXAiOjE3MjA0MTc3ODk4ODN9.AeepPBji4k87Jx0-FC3iaN4Ayx3h0XnVQZgjklXC6vk3HNmW4gHZYwkdezNoBhfhbbwvNnEchvhtDwDHsLs8voqWACk5Z9vrr8CteUF3fAcaQKxXU9j_8jEdcswcOTPwL0m3fXvi7EGOlod_Zkyt3eQf-q-FwhnG-kqfZclQtK8pKSrN
#https://asr-mts.yubian.com.tw/resource/files/AXnsWs_hFwJvYlFHUIQ8VwfWDJHEAJFcFQft3JzGpG0vdC2dHxNDkT8sqTLqjxckeLBlN1Up7afN1cMTnAIWNapTLgqalvCSwF5kNO85EtCAS6TWEy4YI5o--Z95PLug/20220518134049_caption.srt?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzUxMiJ9.eyJzdWIiOiJ5YnRlc3RfdW5pc29vbiIsImF1ZCI6ImFzci1zZXJ2aWNlLmJyb25jaS5jb20udHciLCJjYXBhYmlsaXR5IjoyLCJyb2xlIjoidXNlciIsIm5pY2tuYW1lIjoieWJ0ZXN0X3VuaXNvb24iLCJwZXJtcyI6WyJzeXNfc3RhdHVzIiwidGFza19hc3NpZ24iLCJ0YXNrX21uZ3IiXSwiZXhwIjoxNzIwNDQ2NTg5LCJqdGkiOiIyNGQ5NzFiMi0zNDM3LTQ5M2MtODUwMS1hMDA5MzIwMzQ2ZDYiLCJ0aW1lc3RhbXAiOjE3MjA0MTc3ODk4ODN9.AeepPBji4k87Jx0-FC3iaN4Ayx3h0XnVQZgjklXC6vk3HNmW4gHZYwkdezNoBhfhbbwvNnEchvhtDwDHsLs8voqWACk5Z9vrr8CteUF3fAcaQKxXU9j_8jEdcswcOTPwL0m3fXvi7EGOlod_Zkyt3eQf-q-FwhnG-kqfZclQtK8pKSrN
#https://asr-mts.yubian.com.tw/resource/files/DMvd6rmxKQWsT3vHNn3tuIhIw2uih_oRKIDS7oaEj9wZsbFRXic5SRpmKUEBke5ajr8W9SosFWVS8Z7-Fe14rhE9dZPsq3nTYzsl0wYukdgjgv4OcG5MrubhyHTGAx-q/20220518134049_caption.srt?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzUxMiJ9.eyJzdWIiOiJhc3JfYWRtaW4iLCJhdWQiOiJhc3Itc2VydmljZS5icm9uY2kuY29tLnR3IiwiY2FwYWJpbGl0eSI6Miwicm9sZSI6ImFkbWluIiwibmlja25hbWUiOiJhc3JfYWRtaW4iLCJwZXJtcyI6WyJtb2RlbF9tbmdyIiwib3BlcmF0aW9uX2F1ZGl0Iiwic3lzX2NvbmZpZyIsInN5c19zdGF0dXMiLCJ0YXNrX2Fzc2lnbiIsInRhc2tfbW5nciIsInVzZXJfbW5nciJdLCJleHAiOjE3MjA1MzMxNTksImp0aSI6IjI0ZDk3MWIyLTM0MzctNDkzYy04NTAxLWEwMDkzMjAzNDZkNiIsInRpbWVzdGFtcCI6MTcyMDUwNDM1OTQyNn0.AbhwlAbLAT3XwrC8wvzmbJ5nBexPOKeYtwNwSR2M-MliIkBogfM-5W8AZ5nm70YinvlMlhOhQcRhmfTq3EpMJ3BZAe91Bcf-eZgVlbdaRu6Udi8rqqb8nu-qzmdunwKAPiNZRiI16LtE_ZMDGkl8R8GP4EMhcVB2irAnXNndY0ngvxhK
input_string = "eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzUxMiJ9.eyJzdWIiOiJ5YnRlc3RfdW5pc29vbiIsImF1ZCI6ImFzci1zZXJ2aWNlLmJyb25jaS5jb20udHciLCJjYXBhYmlsaXR5IjoyLCJyb2xlIjoidXNlciIsIm5pY2tuYW1lIjoieWJ0ZXN0X3VuaXNvb24iLCJwZXJtcyI6WyJzeXNfc3RhdHVzIiwidGFza19hc3NpZ24iLCJ0YXNrX21uZ3IiXSwiZXhwIjoxNzIwNDQ2NTg5LCJqdGkiOiIyNGQ5NzFiMi0zNDM3LTQ5M2MtODUwMS1hMDA5MzIwMzQ2ZDYiLCJ0aW1lc3RhbXAiOjE3MjA0MTc3ODk4ODN9.AeepPBji4k87Jx0-FC3iaN4Ayx3h0XnVQZgjklXC6vk3HNmW4gHZYwkdezNoBhfhbbwvNnEchvhtDwDHsLs8voqWACk5Z9vrr8CteUF3fAcaQKxXU9j_8jEdcswcOTPwL0m3fXvi7EGOlod_Zkyt3eQf-q-FwhnG-kqfZclQtK8pKSrN"
print(input_string)
print("")
encoded_string = urlencode_string(input_string)
print(encoded_string)
f = open("c:\\euls\\aaa.txt", "+a")
f.write(encoded_string)
f.close()
exit()
'''

import socket
import threading

# 定義伺服器的 IP 和埠
HOST = '127.0.0.1'
PORT = 54321

# 用來儲存客戶端連線的列表
clients = []

# 處理每個客戶端的連線
def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(f"Received from {client_socket.getpeername()}: {message}")
            else:
                break
        except:
            break
    client_socket.close()

# 主伺服器函數
def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)
    print(f"Server listening on {HOST}:{PORT}")

    while True:
        client_socket, client_address = server.accept()
        print(f"Accepted connection from {client_address}")
        clients.append(client_socket)
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    start_server()
exit()


arg:str = ""
if len(sys.argv) <=1:
    print("give arg Cli or Svr")
    exit()

arg = sys.argv[1].lower()
if arg == "cli":
    # 定義主機和端口
    HOST = '127.0.0.1'
    PORT = 54321  # 遠程主機開放的端口

    # 建立一個socket對象
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 連接到伺服器
    client_socket.connect((HOST, PORT))

    print(f"成功連接到 {HOST}:{PORT}")

    # 傳送數據給伺服器
    message = "Hello, Server!"
    client_socket.sendall(message.encode('utf-8'))

    # 從伺服器接收數據
    data = client_socket.recv(1024)
    print(f"從伺服器接收到數據: {data.decode('utf-8')}")

    # 關閉連接
    client_socket.close()
elif arg =="svr":
    
    # 定義主機和端口
    HOST = '0.0.0.0'  # 伺服器監聽所有可用的網絡接口
    PORT = 54321      # 與客戶端通信的端口

    # 建立一個socket對象
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 綁定地址和端口
    server_socket.bind((HOST, PORT))

    # 開始監聽連接
    server_socket.listen(1)
    print(f"伺服器正在 {HOST}:{PORT} 等待連接...")

    # 接受客戶端的連接
    client_conn, client_addr = server_socket.accept()
    print(f"接受到來自 {client_addr} 的連接")

    # 從客戶端接收數據
    data = client_conn.recv(1024)
    print(f"從客戶端接收到數據: {data.decode('utf-8')}")

    # 向客戶端發送回應
    response = "Hello, Client!"
    client_conn.sendall(response.encode('utf-8'))

    # 關閉連接
    client_conn.close()
    server_socket.close()
