from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def aes_encrypt(plaintext, key):
    cipher = AES.new(key, AES.MODE_CBC)
    iv = cipher.iv
    ciphertext = cipher.encrypt(pad(plaintext.encode('utf-8'), AES.block_size)) # AES.block_size == 16
    return iv + ciphertext

def aes_decrypt(ciphertext, key):
    iv = ciphertext[:AES.block_size]    # AES.block_size == 16
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext[AES.block_size:]), AES.block_size)
    return plaintext.decode('utf-8')

# 示例用法
key = get_random_bytes(16)  # 16 bytes key for AES-128
#key = b"1234567890123456"
print(f"random key: {key}, aes block size: {AES.block_size}")
plaintext = "This is a secret message"

ciphertext = aes_encrypt(plaintext, key)
print(f"Ciphertext: {ciphertext}")

decrypted_text = aes_decrypt(ciphertext, key)
print(f"Decrypted text: {decrypted_text}")

print("\n RSA Test....\n")
# RSA, 測試過可以用, 可以生成public key, private key
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP    # 透過此, 每次加密用相同的public key就算是相同的語詞就會有不同的編碼
import base64
# 生成密钥对
key = RSA.generate(2048)  # 2048 位的密钥长度
private_key = key
public_key = key.publickey()
# 将公钥和私钥导出为 PEM 格式
private_key_pem = private_key.export_key().decode('utf-8')
public_key_pem = public_key.export_key().decode('utf-8')
#print("public :\n", public_key_pem)
#print("private:\n", private_key_pem)
# 要加密的消息
message = "Hello, RSA with PyCryptodome!"
# 加密
cipher = PKCS1_OAEP.new(public_key)
encrypted_message = cipher.encrypt(message.encode('utf-8'))
encrypted_message_base64 = base64.b64encode(encrypted_message)  # 可选择编码为 base64 便于存储或传输
print("encrypt:", encrypted_message_base64.decode())


# 解密
cipher = PKCS1_OAEP.new(private_key)
decrypted_message = cipher.decrypt(encrypted_message)
print("decrypt:", decrypted_message.decode('utf-8'))
