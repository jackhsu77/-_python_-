
# 可以使用, 但windows檔案總管無法解出pyzipper.WZ_AES, 需用7.zip等工具
import os
import pyzipper
# 文件路径列表
files_to_zip = ["c:\\ultralog\\file1.txt",
                "c:\\ultralog\\file2.txt", "c:\\ultralog\\file3.txt"]
# 输出的 ZIP 文件名
zip_filename = "c:\\ultralog\\encrypted_files.zip"
# ZIP 文件的密码
# 创建加密的 ZIP 文件
# with pyzipper.ZipFile(zip_filename, 'w') as zf:
# with pyzipper.AESZipFile(zip_filename, 'w', compression=pyzipper.ZIP_DEFLATED) as zf:
# with pyzipper.AESZipFile(zip_filename, 'w') as zf:
with pyzipper.AESZipFile(zip_filename, 'w', encryption=pyzipper.WZ_AES) as zf:
    # with pyzipper.AESZipFile('new_test.zip','w',compression=pyzipper.ZIP_LZMA, encryption=pyzipper.WZ_AES) as zf:
    zf.setpassword("123".encode())
    # zf.setencryption(pyzipper.WZ_AES, nbits=256)  # 使用 AES 256 加密
    # zf.setpassword("123".encode())  # 设置密码
    for file in files_to_zip:
        print(file + "..." + file.split("\\")[2])
        # zf.write(file)  # 将文件添加到 ZIP 中
        try:
            with open(file, "rb") as ff:
                buf = ff.read()
                print(f"len: {len(buf)}")
                # zf.write(file)
                zf.writestr(file.split("\\")[2], buf)
        except Exception as e:
            print("err: " + str(e))

print(f"ZIP file created: {zip_filename}")
exit()


def create_aes_protected_zip(output_filename, input_files, password):
    with pyzipper.AESZipFile(output_filename, 'w', compression=pyzipper.ZIP_DEFLATED) as zf:
        for file in input_files:
            zf.write(file, os.path.basename(file))
        zf.setpassword(password.encode('utf-8'))


# Files to include in the ZIP
files_to_zip = ['c:\\euls\\aaa.mp3', 'c:\\euls\\aaa.log', 'c:\\euls\\aaa.txt']
# files_to_zip = ['c:\\euls\\aaa.mp3']

# Output ZIP filename
output_zip = 'c:\\euls\\protected_files.zip'

# Password for the ZIP file
zip_password = 'mypassword'

# Create the password-protected ZIP file
create_aes_protected_zip(output_zip, files_to_zip, zip_password)

print(f"Created {output_zip} with AES password protection.")


'''
# 可以壓縮但給了password沒有作用, ZIP_DEFLATED才可以正常
import zipfile
try:
    ZipName = "c:\\euls\\protected_files.zip"
    tmpzip = zipfile.ZipFile(ZipName, "w", allowZip64=True)
    tmpzip.setpassword("123".encode())
    buf = "123456".encode()
    tmpzip.writestr("file1.txt", buf, compress_type=zipfile.ZIP_DEFLATED)
    buf = "654321".encode()
    tmpzip.writestr("file2.txt", buf, compress_type=zipfile.ZIP_DEFLATED)
    tmpzip.close()
    print(f"zip ok")
except Exception as e:
    print(f"zip err: {e}")
'''
