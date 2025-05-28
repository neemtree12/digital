import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

load_dotenv()

sender_email = os.getenv("MAIL_ID")
receiver_email = "ENTER_YOUR_MAIL@gmail.com"
password = os.getenv("PASSWORD") 


subject = "Subject of the Email"
body = "Hello, this is a test email sent from Python!"
msg = MIMEMultipart()
msg["From"] = sender_email
msg["To"] = receiver_email
msg["Subject"] = subject
msg.attach(MIMEText(body, "plain"))


try:
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls() 
        server.login(sender_email, password) 
        server.sendmail(sender_email, receiver_email, msg.as_string())
        print("Email sent successfully!")
except Exception as e:
    print(f"Failed to send email: {e}")
