import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

mail_content = '''
    Hello world
    Simple email
    Thank You
'''

sender_address = 'youremail'
sender_pass = 'yourpassword'
receiver_address = 'receipient'

message = MIMEMultipart()
message['From'] = sender_address
message['To'] = receiver_address
message['Subject'] = 'Hello world test'

message.attach(MIMEText(mail_content, 'plain'))

session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
session.starttls()
session.login(sender_address, sender_pass)
text = message.as_string()
session.sendmail(sender_address, receiver_address, text)
session.quit()

print('Mail Sent')