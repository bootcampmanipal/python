# imports
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#Returns an Email server which we can use to send emails
def create_server():
    username = 'bootcamp_manipal@outlook.com'
    password = input('Enter password: ')

    s = smtplib.SMTP(host='smtp-mail.outlook.com', port=587)
    s.starttls()
    s.login(username, password)
    return s

#Sends an email to the address with the given body and using the given server
def send_email(to, body, server):
    username = 'bootcamp_manipal@outlook.com'
        

    message = MIMEMultipart()
    message['From'] = username
    message['To'] = to
    message['Subject'] = "TEST"
    message.attach(MIMEText(body, 'plain'))
    text = message.as_string()
    server.sendmail(username, to, text)
    print('Successfully sent mail to ', to)

def close_server(server):
    server.close()


    #TODO
def read_file(path):
    pass