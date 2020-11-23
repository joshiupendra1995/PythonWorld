# Python code to illustrate Sending mail from  
# your Gmail account  
import smtplib

# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security 
s.starttls()

email = "xxxxxxx"
password = "xxxxxxx"
send_to = "xxxxxx"
# Authentication 
s.login(email, password)

# message to be sent 
message = "Hello world"

# sending the mail 
s.sendmail(email, send_to, message)

print("Mail Sent")
# terminating the session 
s.quit()
