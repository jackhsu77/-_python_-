import sys
import cgi
import ssl
import requests
import urllib.parse
import urllib.request
from datetime import datetime
import lib_declare as libDcl
# print()
print("Status: 200 OK", flush=True)
print("Content-Transfer-Encoding: Binary",flush=True)

xParam = cgi.FieldStorage()
for xKey in xParam.keys():
    if (xKey not in globals()):
        xValue = xParam.getvalue(xKey)
        if (isinstance(xValue, str)):
            globals()[xKey]=xValue
        elif(isinstance(xValue, list)):
            globals()[xKey]=xValue[-1]

uid = "" if ("uid" not in globals()) else uid
ptype = "" if ("ptype" not in globals()) else ptype
pid = "" if ("pid" not in globals()) else pid
temp = "" if ("temp" not in globals()) else temp

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

a = libDcl.carry_acc(uid)
if a:
    CTIServerID = libDcl.readregini("Misc", "IVRInfo", "CTIServerID")
    CTIServerIP1 = libDcl.readregini("Misc", "IVRInfo", "CTIServerIP1")
    CTIServerIP2 = libDcl.readregini("Misc", "IVRInfo", "CTIServerIP2")
    CTIServerIP = CTIServerIP1 if (CTIServerID == "1") else CTIServerIP2

    tmp = str(ptype).split(".")
    if temp != "":
        src = "https://"+CTIServerIP+"/AVRVOC/AVR_"+tmp[0]+"_"+pid+temp+".wav"
    else:
        src = "https://"+CTIServerIP+"/AVRVOC/AVR-"+tmp[0]+"-"+pid+".wav"
    #header_array = requests.head(src)
    header_array = urllib.request.urlopen(src, context=ctx).getcode()
    try:
        header_array = urllib.request.urlopen(src, context=ctx).getcode()
    except:
        header_array = 0
        pass
    
    if header_array == 200:

        filesize = len(urllib.request.urlopen(src, context=ctx).read())
        buf = urllib.request.urlopen(src, context=ctx).read()
    # FileSize = header_array['Content-Length'] if header_array.status_code == 200 else '0'
    #if header_array.status_code == 200:
        # print(src)
        etag = (str(uid).encode())
        
        
        print('Content-Type: audio/wav') 
        print('Content-Length: '+str(filesize)) 
        print(flush=True)
        sys.stdout.buffer.write(buf)        # 一定要搭配 print("Status: 200 OK", flush=True) print("Content-Transfer-Encoding: Binary",flush=True)
        sys.stdout.flush()
        