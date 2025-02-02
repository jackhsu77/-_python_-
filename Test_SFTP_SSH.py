import paramiko
import datetime as dt

# SFTP服务器地址 # 目前我用 OpenSSH SSH Server(服務裡面有)
# hostname = "1.2.3.4"            # 不存在的地址
# hostname = '127.0.0.1'          # loopback
# hostname = "192.168.31.180"     #家裡
# hostname = "192.168.50.53"      #公司
# hostname = "192.168.11.180"     #公司
# hostname = "192.168.11.131"     # 公司安達測試機
hostname = "192.168.8.156"      # 長問測試機

# port = 22               # SFTP Service port,   # 通常式22
port = 2222               # SFTP Service port,  # 長問測試機用2222

# username = 'jackhsu'    # account
# password = 'aaaaaaa'    # password

# username = 'ultra'    # account     # 給長問測試機回傳.dla到我這台的的帳密 (雙聲道)
# password = '!QAZ2wsx'    # password # 給長問測試機回傳.dla到我這台的的帳密 (雙聲道)
# username = 'ultra2'    # account    # 給長問測試機回傳.dla到我這台的的帳密 (單聲道)
# password = '!QAZ2wsx'    # password # 給長問測試機回傳.dla到我這台的的帳密 (單聲道)


# username = 'ultra'        # account      # 公司安達測試機
# password = '!QAZ2wsx'     # password     # 公司安達測試機

# username = 'jacky2'    # account     # 長問測試機的帳密 (單聲道)
# password = 'jacky2'    # password    # 長問測試機的帳密 (單聲道)
username = 'jacky'    # account     # 長問測試機的帳密 (雙聲道)
password = 'jacky'    # password    # 長問測試機的帳密 (雙聲道)


# local_file_path = 'c:\\ultralog\\sftp_test.txt'
# remote_file_path = '.\\Media\\20241016\\001\\abc.txt'
# local_file_path = 'D:\\speech-to-text-py\\Costco\\20220518134049.wav'
# remote_file_path = '1000135303320240219114813_998877665544_test3.wav'

# remote_file_path = '.\\media\\20241216\\008\\20241216010000.wav'
# local_file_path = 'c:\\ultralog\\20241216010000.wav'

# remote_file_path = '.\\Media\\20241217\\001\\20241217175531.wav'    # 公司安達測試機
# local_file_path = 'c:\\ultralog\\from192_168_11_131.wav'            # 公司安達測試機


# 永豐金 小於5秒檔案, 修改設定後確定可以轉出, 19和8都有人聲可以轉出.dia, 6的沒有人聲(這筆不會下載, 但可以從長問測試機的網站下載, 發現6.UltraLog071301420241014165818_caption為0k)
# remote_file_path = '19.UltraLog071301520241014155543.wav'
# local_file_path = 'C:\\Users\\jackhsu\\Downloads\\19.UltraLog071301520241014155543.wav'
# remote_file_path = '8.UltraLog071301920241014155659.wav'
# local_file_path = 'C:\\Users\\jackhsu\\Downloads\\8.UltraLog071301920241014155659.wav'
# remote_file_path = '6.UltraLog071301420241014165818.wav'
# local_file_path = 'C:\\Users\\jackhsu\\Downloads\\6.UltraLog071301420241014165818.wav'

# remote_file_path = 'a2.wav'
# local_file_path = 'C:\\ultralog\\a2.wav'

remote_file_path = '1131226133401.wav'
local_file_path = 'C:\\ultralog\\1131226133401.wav'


# Ryan給的單筆雙聲道錄音檔
# remote_file_path = '1131226133401_4.wav'
# local_file_path = 'C:\\Users\\jackhsu\\Downloads\\1131226133401_4.wav'

'''
# Ryan給的10筆雙聲道錄音檔
remote_file_path = '1131226155648.wav'
local_file_path = 'C:\\Users\\jackhsu\\Downloads\\1131226155648.wav'
remote_file_path = '1131230155341.wav'
local_file_path = 'C:\\Users\\jackhsu\\Downloads\\1131230155341.wav'
remote_file_path = '1131231133018-.wav'
local_file_path = 'C:\\Users\\jackhsu\\Downloads\\1131231133018-.wav'
remote_file_path = '1131231134531-.wav'
local_file_path = 'C:\\Users\\jackhsu\\Downloads\\1131231134531-.wav'
remote_file_path = '1131231145810-.wav'
local_file_path = 'C:\\Users\\jackhsu\\Downloads\\1131231145810-.wav'
remote_file_path = '1131231155528-.wav'
local_file_path = 'C:\\Users\\jackhsu\\Downloads\\1131231155528-.wav'
remote_file_path = '1140103113621.wav'
local_file_path = 'C:\\Users\\jackhsu\\Downloads\\1140103113621.wav'
remote_file_path = '1140103135704.wav'
local_file_path = 'C:\\Users\\jackhsu\\Downloads\\1140103135704.wav'
remote_file_path = '1140106131727.wav'
local_file_path = 'C:\\Users\\jackhsu\\Downloads\\1140106131727.wav'
remote_file_path = '1140106134332-.wav'
local_file_path = 'C:\\Users\\jackhsu\\Downloads\\1140106134332-.wav'
'''


def sftp_upload():
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        ssh.connect(hostname, port, username, password,
                    timeout=6.0)    # timeout設定最多幾秒
        # ssh.connect(hostname, port, username, password)
        sftp = ssh.open_sftp()

        sftp.put(local_file_path, remote_file_path)
        print(f"Upload OK: {local_file_path} -> {remote_file_path}")

        sftp.close()
        ssh.close()
    except Exception as e:
        # 把服務 OpenSSH SSH Server關閉, 2秒後 則有錯誤Upload err: [Errno None] Unable to connect to port 22 on 127.0.0.1
        # IP為1.2.3.4 有設Timeout 則會等Timeout參數幾秒後跳出, 錯誤 timed out
        # IP為1.2.3.4 沒設Timeout 則等20秒後 錯誤 Upload err: [WinError 10060] 連線嘗試失敗，因為連線對象有一段時間並未正確回應，或是連線建立失敗，因為連線的主機無法回應
        # 帳密錯誤則會出現錯誤  Authentication failed.
        # 來源檔案不存在        [Errno 2] No such file
        print(f"Upload err: {e}")


def sftp_download():
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname, port, username, password)

        sftp = ssh.open_sftp()

        sftp.get(remote_file_path, local_file_path)
        # sftp.get("test.log", local_file_path)
        print(f"download OK: {remote_file_path} -> {local_file_path}")

        sftp.close()
        ssh.close()
    except Exception as e:
        print(f"download err: {e}")


count = dt.datetime.now()
sftp_upload()
# sftp_download()  # 下载文件
count = dt.datetime.now() - count
print(f"elapse sec: {count.seconds}")
