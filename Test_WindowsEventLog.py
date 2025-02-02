import win32evtlog  # 用於讀取事件日誌
import win32evtlogutil
import win32con
from datetime import datetime, timedelta

'''
# 設定你要查詢的事件日誌名稱 (System, Application, Security)
log_type = "System"  # 可選：System, Application, Security
# 打開事件日誌
hand = win32evtlog.OpenEventLog(None, log_type)         # 測試過 ok
print(f"hand: {hand}")
# 獲取事件日誌紀錄
#events = win32evtlog.ReadEventLog(hand, win32con.EVENTLOG_FORWARDS_READ, 0)    #
events = win32evtlog.ReadEventLog(hand, win32con.EVENTLOG_SEQUENTIAL_READ | win32con.EVENTLOG_FORWARDS_READ, 0)
# 顯示最新的事件紀錄
for i, event in enumerate(events):
    #event_time = datetime.strptime(f"{event.TimeGenerated}", "%Y-%m-%d %H:%M:%S")
    #if start_time <= event_time <= end_time:
        print(f"事件 {i+1}:")
        print(f"事件 ID: {event.EventID}")
        print(f"來源: {event.SourceName}")
        print(f"日期時間: {event.TimeGenerated}")
        print(f"訊息: {win32evtlogutil.SafeFormatMessage(event)}")
        print("-" * 50)
# 關閉事件日誌
win32evtlog.CloseEventLog(hand)
'''

# 設定時間區間
now = datetime.now()
start_time = now - timedelta(days=1)  # 過去一天
end_time = now
hand = win32evtlog.OpenEventLog(None, "System")         # 測試過 ok    
i = 0
while True:
    i = i+1
    if i >=10000: break
    print(f"{i}  ########################################")
    # events 1次只會給10幾筆, 所以要一直呼叫.ReadEventLog搭配EVENTLOG_SEQUENTIAL_READ|EVENTLOG_FORWARDS_READ取得下次紀錄
    events = win32evtlog.ReadEventLog(hand, win32con.EVENTLOG_SEQUENTIAL_READ | win32con.EVENTLOG_FORWARDS_READ,0)
    if not events:
        break
    for event in events:
        event_time = datetime.strptime(f"{event.TimeGenerated}", "%Y-%m-%d %H:%M:%S")
        if start_time <= event_time <= end_time:
            print(f"事件時間: {event_time}")
            print(f"事件 ID: {event.EventID}")
            print(f"來源: {event.SourceName}")
            try:
                print(f"訊息: {win32evtlogutil.SafeFormatMessage(event)}")
            except Exception:
                print(f"無法解析訊息")
            print("-" * 50)
