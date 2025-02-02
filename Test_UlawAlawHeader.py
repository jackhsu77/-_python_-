import time
import sys
import os


F_ULAW = "0"
F_ALAW = "8"

if (len(sys.argv)<3):
    print("Parameter Error: example --> \n python.exe c:\\test\\Test_UlawAlawHeader.py c:\\test\\aaa.wav 0 \n python.exe c:\\test\\Test_UlawAlawHeader.py c:\\test\\aaa.wav 8")
    sys.exit()

filepath = sys.argv[1]
if not os.path.exists(filepath):
    print(f"{filepath} not found")
fileformat = sys.argv[2]
filesize = os.path.getsize(filepath)
print(f"{filepath}: {filesize} bytes")

if (fileformat == F_ULAW) or (fileformat == F_ALAW):
    with open(filepath + ".wav", "wb") as f:
        f.write(b"RIFF")                # RIFF
        
        '''
        _filesize = filesize + 38
        hex_str = hex(_filesize)[2:]
        if len(hex_str) % 2 != 0:
            hex_str = '0' + hex_str
        hex_list = [hex_str[i:i+2] for i in range(0, len(hex_str), 2)][::-1]
        if (len(hex_list) < 4):
            _nlen = len(hex_list)
            for i in range(_nlen,4):
                hex_list.append("0")
        for i in hex_list:
            a =1    
            hex_number = int(i, 16)
            byte_data = hex_number.to_bytes(1, byteorder='big')  # 1 byte 對應 'AB'
            f.write(byte_data)
        '''
        hex_str = (filesize+38).to_bytes(4, "little")
        f.write(hex_str)
        f.write(b"WAVE")                # WAVE
        f.write(b"fmt\x20")             # fmt         
        f.write(b"\x12\x00\x00\x00")    
        if (fileformat == F_ULAW):
            f.write(b"\x07\x00")            # ulaw = 7, alaw = 6
        else:
            f.write(b"\x06\x00")            # ulaw = 7, alaw = 6
        f.write(b"\x01\x00")                # channel數
        f.write(b"\x40\x1f\x00\x00")        # 取樣率8000
        f.write(b"\x40\x1f\x00\x00")        # 每秒音訊Byte數
        f.write(b"\x01\x00\x08\x00\x00\x00")
        f.write(b"FACT")
        f.write(b"\x04\x00\x00\x00")
        f.write(b"\x00\x00\x00\x00")
        f.write(b"data")
        
        hex_str = filesize.to_bytes(4, "little")
        f.write(hex_str)
                
        
        with open(filepath, "rb") as f2:
            bb = f2.read()
            f.write(bb)
    print("do ok")
else:
    print("do nothing, ONLY support Ulaw(0) or Alaw(8)")
