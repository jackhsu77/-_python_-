import json, pickle, shelve


# Azure Docker STT後的檔案
with open('c:\\euls\\Mono_eaststone_20240530144557_wav.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
#for key, value in data["AudioFileResults"][0]["SegmentResults"].items():
#    print(f"{key}: {value}\n")
for item in data["AudioFileResults"][0]["SegmentResults"]:
    print(f"Channel: {item['Channel']}, Offset: {item['OffsetInSeconds']}, Dur: {item['DurationInSeconds']}, Text: {item['DisplayText']}")


exit()

a = dict()
for i in range(3):
    a["int" + str(i+1)] = i *10

# json, 速度比pickle快, 資料量也比pickle小
s = json.dumps(a)
print(f"type={type(s)} ==> {s}")
aa = json.loads(s)
print(f"type={type(aa)} ==> {aa}")

# 通常pickle作法將東西放到dict
with open(".\\test.pickle", mode="wb") as f:
    pickle.dump(a,f)
with open(".\\test.pickle", mode="rb") as f:
    aa = pickle.load(f)
print(f"pickle type={type(aa)} ==> {aa}")

a = dict()
with shelve.open(".\\test.shelve", flag="c") as she:
    for i in range(3):
        idx:str = "s" + str(i+1) 
        a[idx] = list()
        for j in range(i+1):
            a[idx].append(j * 100)
        she[idx] = a

with shelve.open(".\\test.shelve", "r") as she:
    print(f"shelve: ")
    for key in she.keys():
        print(f"key: {key}--> " + str(she[key]))