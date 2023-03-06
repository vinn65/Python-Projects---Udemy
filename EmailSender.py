import smtplib

to = input("Enter recipient`s email:\n")

content = input("Enter email Body:\n")

def SendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("senderemail@gmail.com","password")

    server.sendmail("senderemail@gmail.com", to, content)


SendEmail(to, content)