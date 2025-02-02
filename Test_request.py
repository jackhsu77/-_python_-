import requests
import threading
import time

url = "https://asr-mts.yubian.com.tw/api/v1/"
Access_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzUxMiJ9.eyJzdWIiOiJ5YnRlc3RfdW5pc29vbiIsImF1ZCI6ImFzci1zZXJ2aWNlLmJyb25jaS5jb20udHciLCJjYXBhYmlsaXR5IjoyLCJyb2xlIjoidXNlciIsIm5pY2tuYW1lIjoieWJ0ZXN0X3VuaXNvb24iLCJwZXJtcyI6WyJzeXNfc3RhdHVzIiwidGFza19hc3NpZ24iLCJ0YXNrX21uZ3IiXSwiZXhwIjoxNzIwNjk1NDIwLCJqdGkiOiIyNGQ5NzFiMi0zNDM3LTQ5M2MtODUwMS1hMDA5MzIwMzQ2ZDYiLCJ0aW1lc3RhbXAiOjE3MjA2NjY2MjA1MjZ9.AMqAii8h0aAkeQ0KXneY97v95I8wZFeYpp2xNxZph2eU7F49MgtCfIlG6-qIsqj4-fG-jsVFiZWvflKakxMtMiXEAPxmoOmuNT7uDE2VdazwqAEETO_sEcts7WUuRomzScU6M-nTKjq4OTtIDhzc0S4E5EwOD9F5AWKZ6N6KbCLQEH8e"
Access_token = ""
task_id = ""

REC_PATH = "D:\\speech-to-text-py\\Costco\\"

RET_OK = 0
RET_STILLWAIT = 1
RET_FAIL = 2

TID_NONE = -1

def Bronci_login():
    global url
    global Access_token
    #1. 長問的登入系統API
    #https://asr-mts.yubian.com.tw/api/v1/login
    #若網址錯誤則response.status_code為404或其他錯誤
    #帳密錯誤則回傳json {'code': 42210, 'error': 'unauthorized'}
    #帳密錯誤則回傳json {'code': 200, 'token': token, 'expiration': valid_duration_in_sec}
    url_login = url + "login"
    payload = {
        "username": "ybtest_unisoon",
        "password": "unisoon@2024"
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(url_login, json=payload, headers=headers)
    if (response.status_code == 200):
        result = response.json()
        if (result['code'] ==200):
            print(f"login code: {result['code']}, token: {result['token']}, expiration: {result['expiration']}")
            Access_token = result['token']
        else:
            print(f"login code: {result['code']}, err: {result['error']}")
    else:
        print(f"login URL err: {response.status_code}")

# 連續送多次logout看起來沒問題
def Bronci_logout():
    global url
    #https://asr-mts.yubian.com.tw/api/v1/logout
    url_logout = url + "logout"
    headers = {
        "Authorization": "Bearer " + Access_token
    }
    response = requests.post(url_logout, headers=headers)
    if (response.status_code == 200):
        result = response.json()
        if (result['code'] ==200):
            print(f"logout code: {result['code']}, username: {result['username']}, message:{result['message']}")
        else:
            print(f"logout err {str(result)}")
    else:
        print(f"logout URL err: {response.status_code}")



# Access_token==""  -->  400 Bad request
#                        401 unauthorized 表示token過期
# Result json ex: 1. name: basic-hakka, version: 2023.06.02
#                 2. name: basic-taigi, version: 2023.06.25
def Bronci_Models():
    global url
    global Access_token
    url_models = url + "models"
    headers = {
        "Authorization": "Bearer " + Access_token
    }
    response = requests.get(url_models, headers=headers)
    if (response.status_code == 200):
        result = response.json()
        if (result['code'] ==200):
            for i,d in enumerate(result['data'],start=1):
                print(f"models_{i} name: {d['name']}, version: {d['version']}")
        else:
            print(result)
    else:
        print(f"models URL err: {response.status_code}")

def Bronci_Checktasks(tid):
    global url
    global Access_token
    
    if tid == "":
        print("Checktasks No task id !!")
        exit()
    url_tasks = url + "subtitle/tasks/" + str(tid)
    headers = {
        "Authorization": "Bearer " + Access_token
    }
    #print(f"url: {url_tasks}")
    # url_tasks == https://asr-mts.yubian.com.tw/api/v1/subtitle/tasks/479
    response = requests.get(url_tasks, headers=headers)
    if (response.status_code == 200):
        result = response.json()
        # 看過status =0, 11, 13, 3
        if (result['code'] ==200):
            for s in result['data']:
                st_str= Status_str(s['status']) #等待確認==0; 任務已確認，等待處理==11; 檔案下載中==12; 產生字幕中==13; 任務已完成==3; 任務失敗==4; 任務已取消==5
                print(f"check tasks code: {result['code']}, id:{s['id']}, status:{s['status']}({st_str}), file:{s['uploadedFileName']}")
                if (s['status'] == 3):
                    return RET_OK
                elif (s['status'] in [0,11,12,13]):
                    return RET_STILLWAIT
                else:
                    return RET_FAIL
        else:
            print(result)
            return RET_FAIL
    else:
        print(f"check tasks URL err: {response.status_code}")
        return RET_FAIL

def Bronci_GetSubtitle(tid):
    global url
    global Access_token
    sl = []

    if tid == "":
        print("GetSubtitle No task id to check !!")
        exit()
    url_tasks = url + "subtitle/tasks/" + str(tid) + "/subtitle-json?editor=1&category=dia"
    headers = {
        "Authorization": "Bearer " + Access_token
    }
    print(f"url: {url_tasks}")
    #url_tasks = https://asr-mts.yubian.com.tw/api/v1/subtitle/tasks/479/subtitle-json?editor=1&category=dia
    response = requests.get(url_tasks, headers=headers)
    if (response.status_code == 200):
        result = response.json()
        if (result['code'] ==200):
            for s in result['data']:
                print(f"{s}")
                sl.append(f"id:{str.ljust(str(s['id']),3)}, speaker:{s['speaker']}, startTime:{s['startTime']}, endTime:{s['endTime']}, text:{s['text']}\n")
            taskLog_Write(tid, sl)
        else:
            print(result)
    else:
        print(f"GetSubtitle URL err: {response.status_code}")
    
def Bronci_Createtasks(filename):
    global url
    global Access_token
    global task_id
    url_tasks = url + "subtitle/tasks"
    #url_tasks = "https://asr-mts.yubian.com.tw/api/v1/subtitle/tasks"
    headers = {
        "Authorization": "Bearer " + Access_token
    }
    payload = {
        "sourceType":2,
        "title": "jacky_tasks",
        "modelName": "taigi-model",
        "audioChannel": 0,
        "speakerNum": 0,
        "dspMode": 1
    }
    file = [("file",(filename, open(REC_PATH + filename, "rb"), "audio/wav"))]
    
    task_id = ""
    response = requests.post(url_tasks, data=payload, headers=headers, files=file)
    if (response.status_code == 200):
        result = response.json()
        if (result['code'] ==200):
            print(f"Create tasks code: {result['code']}, message:{result['message']}, taskid: {result['id']}")
            task_id = result['id']
            return task_id
        else:
            print(f"Create tasks err: {str(result)}")
            return TID_NONE
    else:
        print(f"Create tasks URL err: {response.status_code}")
        return TID_NONE

def Status_str(status:int):
    #等待確認==0; 任務已確認，等待處理==11; 檔案下載中==12; 產生字幕中==13; 任務已完成==3; 任務失敗==4; 任務已取消==5
    if (status == 0):
        return "等待確認(wait confirm)"
    elif(status == 11):
        return "任務已確認 等待處理(confirmed, wait process)"
    elif(status == 12):
        return "檔案下載中(file downloading)"
    elif(status == 13):
        return "產生字幕中(creating subtitle)"
    elif(status == 3):
        return "任務已完成(task completed)"
    elif(status == 4):
        return "任務失敗(task fail)"
    elif(status == 5):
        return "任務已取消(task canceled)"

def taskLog_Write(tid, ResultData):
    with open(".\\" + "___" + str(tid) + ".log", "+a") as f:
        f.writelines(ResultData)

ttid = ""
tid = []
Bronci_login()
#Bronci_Models()
# 看起來可以1次送3筆上去, 但STT還是一筆筆依序下去做
ttid = Bronci_Createtasks("20220518134049.wav")
if ttid != TID_NONE: tid.append(ttid)
ttid = Bronci_Createtasks("20220518112549.wav")
if ttid != TID_NONE: tid.append(ttid)
ttid = Bronci_Createtasks("20220518135451.wav")
if ttid != TID_NONE: tid.append(ttid)
if (len(tid) > 0):
    while(True):
        for i in tid:   #1次問3筆
            r = Bronci_Checktasks(i)
            if r == RET_OK:
                print(f"id {i} STT ok")
                Bronci_GetSubtitle(i)
                tid.remove(i)
            elif r == RET_STILLWAIT:
                print(f"id {i} STT wait finish....")
            else:
                print(f"id {i} STT err")
                tid.remove(i)
        if (len(tid) <=0):
            break
        time.sleep(2)            

Bronci_logout()
exit()

# 測試檢查檔案是否存在
url = 'http://127.0.0.1:998/MediaTemp/Test.wav'
def check_file_exists(url):
    try:
        response = requests.head(url)   # 发送HEAD请求
        if response.status_code == 200: # 状态码200表示文件存在
            return True
        else:
            return False
    except requests.RequestException as e: # 捕获所有请求异常
        print(f"An error occurred: {e}")
        return False
if check_file_exists(url):
    print("The file exists.")
else:
    print("The file does not exist.")
