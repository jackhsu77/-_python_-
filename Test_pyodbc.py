import pyodbc
import datetime as dt
import os

# 設置連接參數
server:str = '127.0.0.1'
database:str = 'Ultra_sys'
username:str = 'ultraaa'
password:str = 'g7t3l2o6U1r4la5'

Ret_DB_OK = 0
Ret_DB_Err_Conn = -999

conn:pyodbc.Connection = None

def Debug_log_Write(s:str):
    f = open("c:\\euls\\test.log", "+a")
    f.write(dt.datetime.now().strftime("%H:%M:%S ") + s + os.linesep)
    f.close()

# 建立連接
def DB_Connect():
    global conn

    try:
        conn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};'
            f'SERVER={server};'
            f'DATABASE={database};'
            f'UID={username};'
            f'PWD={password}'
        )
    except Exception as e:
        s = "DB_Connect Err: " + str(e)
        print(s)
        Debug_log_Write(s)
        conn=None
    if (conn):
        return Ret_DB_OK
    else:
        return Ret_DB_Err_Conn

def DB_Select(StrSelect : str):
    cursor:pyodbc.Cursor=None
    if (conn):
        # 創建一個cursor對象
        cursor = conn.cursor()
        # 執行查詢
        #query = 'SELECT [Server],[ComputerName],[IP],[Port],[Serial] FROM Host'
        cursor.execute(StrSelect)
        # 獲取數據
        rows = cursor.fetchall()
        #cursor.close()
        return rows
    else:
        return -999

t = DB_Connect()
print(f"DB_Connect ret: {t}")
t = DB_Select('SELECT [Server],[ComputerName],[IP],[Port],[Serial] FROM Host')
print(f"DB_Select ret: {t}")

if (t != Ret_DB_Err_Conn):
    # 迭代並顯示數據
    for row in enumerate(t):
        print("row" + str(row[0]) + "--> " + str(row[1]))
try:
    conn.close()
except:
    pass
