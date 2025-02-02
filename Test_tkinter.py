import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import datetime as dt
from pypinyin import lazy_pinyin    # for 相似字
from fuzzywuzzy import fuzz         # for 相似字

SIMILARITY_LEVEL = 80               # 70以下精準度不夠, 所以先設80, 通常同音異字或相近音都會是90以上

aFileLines = []
aFilePath = ""





# 相似字 取得字串的羅馬拼音
def Pinyin_string_get(text):
    return ''.join(lazy_pinyin(text))

# 相似字 判斷a字串是否出現在b字串
def Similar_substring_position_find(a, b, FindMulti=False):
    max_similarity = 0
    best_start_pos = -1
    len_a = len(a)
    len_b = len(b)
    a_pinyin = Pinyin_string_get(a)
    #b_pinyin = get_pinyin_string(b)
    #print(a_pinyin, b_pinyin)
    if (FindMulti == False):    
        for start in range(len_b - len_a + 1):
            b_substring = b[start:start + len_a]
            b_substring_pinyin = Pinyin_string_get(b_substring)
            similarity = fuzz.ratio(a_pinyin, b_substring_pinyin)
            if similarity > max_similarity:
                max_similarity = similarity
                best_start_pos = start
        return best_start_pos, max_similarity
    else:
        FindMultiList = []
        PosIgnore = -1
        for start in range(len_b - len_a + 1):
            if start >= PosIgnore:
                PosIgnore = -1
                b_substring = b[start:start + len_a]
                b_substring_pinyin = Pinyin_string_get(b_substring)
                similarity = fuzz.ratio(a_pinyin, b_substring_pinyin)
                if similarity >= SIMILARITY_LEVEL:
                    FindMultiList.append((start, similarity))
                    PosIgnore = start + len_a
        return FindMultiList

#def preload_dialog():
#    filedialog.askopenfilename(filetypes=[("Log files", "*.log")])

def Log_Key():
    global aFileLines
    global aFilePath
    
    sim = aFilePath.split(".log")
    aFilesimPath = sim[0] + "_similarity.log"
    
    sim = txtKey.get("1.0", tk.END).strip()
    if (sim == ""): return
    sim = sim.split(",")
    
    WLines = []
    for Line in aFileLines:
        WLines.append(Line)
        for ss in sim:
            #print(ss + "-->" + Line, type(Line))
            LList = Line.split("text:")
            #print("do " + LList[1])
            r = Similar_substring_position_find(ss, LList[1], True)
            if (len(r) <=0 ):
                WLines.append(f" '{ss}'相似度太低, 沒找到\n")
            else:
                for p in r:
                    WLines.append(f" '{ss}'相似度為{p[1]}%, 可能位於 {p[0]+1} 位置\n")
        WLines.append("\n")

    #print("path: " + aFilesimPath)
    with open(aFilesimPath, "w") as f:
        f.writelines(WLines)

def Find_Key():
    global cmbSTT
    global txtKey
    global lstKey
    
    k = txtKey.get("1.0", tk.END).strip()
    s = cmbSTT.get()
    if(not k) or (not s): return
    r = Similar_substring_position_find(k, s, False)
    now = dt.datetime.now().strftime("%H:%M:%S")
    lstKey.insert(tk.END,  f"{now} max_similarity: {r[0]}, {r[1]}%")
    lstKey.select_clear(0, tk.END)  # 清除所有选择
    lstKey.select_set(tk.END)
    lstKey.see(tk.END)

#msg = messagebox
def select_file():
    global txtpath
    global cmbSTT
    global aFileLines
    global aFilePath
    
    file_path = filedialog.askopenfilename(initialdir=f"C:\\UltraLog\\System\\log", filetypes=[("Log files", "*.log")])
    if file_path:
        aFilePath = file_path
        #txtpath.delete(1.0, tk.END)  # 清空当前内容
        #txtpath.insert(tk.END, file_path)  # 插入新的文件路径
        txtpath.replace(1.0, tk.END, file_path)
        #cmbSTT['values'] = []
        items = []
        aFileLines.clear()
        with open(file_path, "r") as f:
            line = f.readline()
            while line:
                aFileLines.append(line)
                r = line.split("text:")
                items.append(r[1])
                line = f.readline() 
            
        print(f"len: {len(items)}")
        for i, d in enumerate(items,start=1):
            print(f"id: {i} --> {d}",end="")
        cmbSTT['values'] = items
        cmbSTT.current(0)    # 選定第幾個項目
        
    else:
        #msg.showinfo("File Selected", f"No select any file")
        txtpath.delete(1.0, tk.END)  # 清空当前内容
        

# 創建主視窗
root = tk.Tk()
#root.after(100, preload_dialog)

root.title("相似語測試")
root.geometry("538x450")

btnpath = tk.Button(root, text="選擇檔案", command=select_file)
btnpath.grid(row=0, column=0, padx=5, pady=1, sticky="w")
lblpath = tk.Label(root, text="STT檔案:")
lblpath.grid(row=1, column=0, padx=1, pady=1, sticky="w")
txtpath = tk.Text(root, width=63, height=1)
txtpath.grid(row=1, column=1, padx=1, pady=1, sticky="w")


lblSTT = tk.Label(root, text="對話:")
lblSTT.grid(row=2, column=0, padx=2, pady=3, sticky="w")
cmbSTT = ttk.Combobox(root, values=[], width=60)
cmbSTT.grid(row=2, column=1, padx=1, pady=1, sticky="w")
#cmbSTT.current(0)    # 選定第幾個項目

lblKey = tk.Label(root, text="相似語:")
lblKey.grid(row=3, column=0, padx=2, pady=3, sticky="w")
txtKey = tk.Text(root, width=40, height=1)
txtKey.grid(row=3, column=1, padx=1, pady=1, sticky="w")
btnFKey = tk.Button(root, text="單句相似語", command=Find_Key)
btnFKey.grid(row=4, column=0, padx=5, pady=3, sticky="w")
lblKey = tk.Label(root, text="(相似語需80%以上符合 才準確)")
lblKey.grid(row=4, column=1, padx=2, pady=3, sticky="w")

btnFKey = tk.Button(root, text="對話相似語", command=Log_Key)
btnFKey.grid(row=5, column=0, padx=5, pady=1, sticky="w")


lstKey = tk.Listbox(root, width=73, height=16)
#lstKey.place(x=5, y=178)
lstKey.place(x=5, y=175)



#ttk.messagebox.showinfo("aaa", "aaa")
# 運行主事件循環
root.mainloop()

'''
def on_button_click():
    entered_text = text_entry.get()     # 取得text的文字
    selected_option = combo_box.get()   # 取得Combobox的所選項目的文字
    label.config(text=f"Entered: {entered_text}, Selected: {selected_option}")  # 將字串放入label

# 創建主視窗
root = tk.Tk()
root.title("tkinter test")
root.geometry("400x150")

# 創建並放置文本框
#tk.Label(root, text="請輸入文字:").pack(pady=5) # 建立label, pady指的是邊界寬度吧
#text_entry = tk.Entry(root)                    # 建立text 
#text_entry.pack(pady=5)                        # pady指的是邊界寬度吧 
tk.Label(root, text="請輸入文字:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
#text_entry = tk.Entry(root)
text_var = tk.StringVar()                           # 方式2
text_entry = tk.Entry(root, textvariable=text_var)  # 方式2
text_var.set("aaa bbb 優立迅")                      # 方式2
#text_entry.delete(0,tk.END)             # 方式1
#text_entry.insert(0, "default text")    # 方式1
text_entry.grid(row=0, column=1, padx=5, pady=5, sticky="e")


# 創建並放置選擇框
#tk.Label(root, text="請選擇一個選項:").pack(pady=5) # 建立label, pady指的是邊界寬度吧
#combo_box = ttk.Combobox(root, values=["選項1", "選項2", "選項3"])  # 建立combobox, values是選項
#combo_box.pack(pady=5)  # pady指的是邊界寬度吧
#combo_box.current(0)    # 選定第幾個項目

tk.Label(root, text="請選擇一個選項:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
combo_box = ttk.Combobox(root, values=["選項1", "選項2", "選項3"])  # 建立combobox, values是選項
combo_box.grid(row=1, column=1, padx=5, pady=5, sticky="e")
combo_box.current(0)    # 選定第幾個項目


# 創建並放置按鍵
button = tk.Button(root, text="點擊我", command=on_button_click)    # 建立Button, command應該是click
button.grid(row=2, column=0, columnspan=1, pady=5)

# 創建並放置標籤來顯示結果
label = tk.Label(root, text="")
label.grid(row=3, column=0, columnspan=2, pady=5)

# 運行主事件循環
root.mainloop()
'''