import smtplib
from email.message import EmailMessage

'''
# imap 收信 沒有測試過
import imaplib
import email
from email.header import decode_header

# Gmail IMAP server details
imap_server = "imap.gmail.com"
email_address = "your_email@gmail.com"
app_password = "your_app_password"  # Use an app password instead of your Gmail password

# Connect to the Gmail IMAP server
mail = imaplib.IMAP4_SSL(imap_server)

# Login to your account
mail.login(email_address, app_password)

# Select the mailbox you want to check (e.g., "INBOX")
mail.select("inbox")

# Search for emails (e.g., all emails)
status, messages = mail.search(None, "ALL")

# Convert the result to a list of email IDs
email_ids = messages[0].split()

# Fetch the latest email (change -1 to get other emails)
latest_email_id = email_ids[-1]
status, msg_data = mail.fetch(latest_email_id, "(RFC822)")

# Parse the email content
for response_part in msg_data:
    if isinstance(response_part, tuple):
        msg = email.message_from_bytes(response_part[1])
        # Decode the email subject
        subject, encoding = decode_header(msg["Subject"])[0]
        if isinstance(subject, bytes):
            # Decode bytes to string
            subject = subject.decode(encoding if encoding else "utf-8")
        print("Subject:", subject)

        # Get the sender's email
        from_ = msg.get("From")
        print("From:", from_)

        # If the email message is multipart
        if msg.is_multipart():
            # Iterate over email parts
            for part in msg.walk():
                # Extract the content type of the email
                content_type = part.get_content_type()
                content_disposition = str(part.get("Content-Disposition"))

                # Get the body of the email
                if "attachment" not in content_disposition:
                    if content_type == "text/plain":
                        body = part.get_payload(decode=True).decode()
                        print("Body:", body)
        else:
            # If the email is not multipart, get the payload (the message body)
            body = msg.get_payload(decode=True).decode()
            print("Body:", body)

# Close the connection and logout
mail.close()
mail.logout()
'''


# smtp 寄信 --> 測試過OK, 改用tls 則用smtplib.SMTP('smtp.gmail.com', 587或25) 都可以, 一定要startls()
msg = EmailMessage()
msg['Subject'] = 'test from jacky'
msg['From'] = 'message@unisoon.biz'
#msg['To'] = 'jacky@unisoon.biz'
msg['To'] = 'jackhsu77@yahoo.com.tw'
#msg.set_content('message from jacky')
# 如果你想发送 HTML 格式的邮件正文
msg.add_alternative("""\
<!DOCTYPE html>
<html>
     <body>
         <p>這是 <b>HTML</b> 格式的郵件內容 from jacky tls</p>
     </body>
 </html>
 """, subtype='html')
try:
    with smtplib.SMTP('smtp.gmail.com', 25) as smtp:  # 使用 SSL 连接到 SMTP 服务器   # fail 跳出錯誤wrong version number, 可能要透過https://support.google.com/accounts/answer/185833?hl=zh-Hant 2階段密碼後才能使用
        #print(smtp.ehlo())
        #smtp.starttls() # 沒有此行則跳出錯誤 send err: SMTP AUTH extension not supported by server.
        smtp.login('message@unisoon.biz', 'ultramsg')
        smtp.send_message(msg)
    print('Send OK')
except Exception as e:
    print(f"send err: {e}")
exit()


# smtp 寄信 --> 測試過OK
msg = EmailMessage()
msg['Subject'] = 'test from jacky'
msg['From'] = 'message@unisoon.biz'
#msg['To'] = 'jacky@unisoon.biz'
msg['To'] = 'jackhsu77@yahoo.com.tw'
#msg.set_content('message from jacky')
# 如果你想发送 HTML 格式的邮件正文
msg.add_alternative("""\
<!DOCTYPE html>
<html>
     <body>
         <p>這是 <b>HTML</b> 格式的郵件內容</p>
     </body>
 </html>
 """, subtype='html')
try:
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:  # 使用 SSL 连接到 SMTP 服务器    # ok , it is used SSL
    #with smtplib.SMTP_SSL('smtp.gmail.com', 587) as smtp:  # 使用 SSL 连接到 SMTP 服务器   # fail 跳出錯誤wrong version number, 可能要透過https://support.google.com/accounts/answer/185833?hl=zh-Hant 2階段密碼後才能使用
    #    print(smtp.ehlo())
    #    smtp.starttls()
        smtp.login('message@unisoon.biz', 'ultramsg')
        smtp.send_message(msg)
    print('Send OK')
except Exception as e:
    print(f"send err: {e}")