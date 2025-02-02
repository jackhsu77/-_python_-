from ldap3 import Server, Connection, ALL, NTLM, Tls
import datetime as dt

#LDAPS (usually on port 636). ??? 用以下就可以, 但我沒測試過
'''
from ldap3 import Server, Connection, Tls, ALL
# Define the server
server = Server('ldaps://your-ldap-server.com', get_info=ALL)
# Create a connection and bind
conn = Connection(server, user='your-username', password='your-password')
if conn.bind():
    print("Successfully bound!")
else:
    print(f"Failed to bind: {conn.result}")
'''

# 如果ldap為a self-signed certificate or an untrusted CA, 
# you may need to specify a custom Tls object to handle the certificate validation.
# 用以下就可以, 但我沒測試過
'''
from ldap3 import Server, Connection, Tls, ALL
import ssl
# Configure TLS with certificate validation
tls_config = Tls(validate=ssl.CERT_NONE)  # Replace CERT_NONE with CERT_REQUIRED for stricter validation
# Define the server
server = Server('ldaps://your-ldap-server.com', tls=tls_config, get_info=ALL)
# Create a connection and bind
conn = Connection(server, user='your-username', password='your-password')
if conn.bind():
    print("Successfully bound!")
else:
    print(f"Failed to bind: {conn.result}")
'''

#invalidCredentials 表示提供的用戶名或密碼錯誤。
#strongerAuthRequired 表示需要啟用加密（例如使用 LDAPS 或 StartTLS）。
#serverDown 無法連接到伺服器，檢查伺服器地址或網路連線。
#其他錯誤 查看 conn.result 或伺服器端的日誌，檢查具體問題。

# 出現automatic bind not successful - strongerAuthRequired, chatgpt說要用.start_tls(), 測試過就好了
# 測試過連接locahost:389 , ok(windows 11安裝AD LDS, 設定LDS叫做adldsjacky, 會在"服務"出現), 透過新增windows帳號就可以此驗證該帳號/密碼是否正確
def authenticate_user(ad_server, user_dn, password):
    # 定義 LDAP 服務器
    #server = Server(ad_server, get_info=ALL)
    server = Server(ad_server, get_info=ALL, use_ssl=False) #use_ssl=False也可以拿掉, 後面的.start_tls和.bind也會成功;    
    
    # 嘗試使用提供的帳號和密碼進行連接
    try:
        #conn = Connection(server, user=user_dn, password=password, authentication=NTLM, auto_bind=True)
        #conn = Connection(server, user=user_dn, password=password, authentication=SIMPLE, auto_bind=True)
        conn = Connection(server, user=user_dn, password=password, authentication=NTLM)
        conn.start_tls()
        if conn.bind():
            print('Authentication successful')
            conn.unbind()
            return True
        else:
            return False
    except Exception as e:
        print('Authentication failed:', e)
        return False

# 測試用戶驗證
#ad_server = 'ldap://ipa.demo1.freeipa.org'
##user_dn = 'admin@demo1.freeipa.org'  # 或者 'DOMAIN\\username'
#user_dn = 'users.accounts.demo1.freeipa.org\\admin'  # 或者 'DOMAIN\\username'
#password = 'Secret123'
ad_server = 'ldap://127.0.0.1'  #可以用 ldap://localhost or ldap://localhost:389 or ldap://192.168.50.52
user_dn = '127.0.0.1\\aaa'  # 可以用adldsjacky\\aaa ,'DOMAIN\\username'    # 測試ok, 可以用aaa和ultra帳號
#user_dn = 'cn=aaa,dc=adldsjacky'
password = '123456'
print(dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " ldap start")
is_authenticated = authenticate_user(ad_server, user_dn, password)
print('Is authenticated:', is_authenticated)
print(dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " ldap end")
exit()















def authenticate_ldap(server_uri, user_dn, password):
    """
    Authenticate against an LDAP server.

    :param server_uri: LDAP server URI, e.g., 'ldap://example.com'
    :param user_dn: User distinguished name, e.g., 'cn=admin,dc=example,dc=com'
    :param password: User password
    :return: True if authentication is successful, False otherwise
    """
    try:
        # Define the server
        server = Server(server_uri, get_info=ALL)
        
        # Establish a connection
        conn = Connection(server, user=user_dn, password=password, auto_bind=True)
    
        # If we reach this point, authentication was successful
        return True
    except Exception as e:
        print(f"Authentication failed: {e}")
        return False

# Example usage with OpenLDAP Test Server
#server_uri = 'ldap://ipa.demo1.freeipa.org'
#user_dn = 'uid=demo,cn=users,cn=accounts,dc=example,dc=com'
#password = 'Secret123'
server_uri = 'ldap://ipa.demo1.freeipa.org'
user_dn = 'uid=admin,cn=users,cn=accounts,dc=demo1,dc=freeipa,dc=org'
#user_dn = 'cn=admin,cn=users,cn=accounts,dc=demo1,dc=freeipa,dc=org'
#user_dn = 'admin.users.accounts@demo1.freeipa.org'
password = 'Secret123'
if authenticate_ldap(server_uri, user_dn, password):
    print("Authentication successful")
else:
    print("Authentication failed")




