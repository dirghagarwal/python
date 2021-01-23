import smtplib

to = input('enter the recipients email id:\n')
content = input('enter the content:')
def sendemail(to, content):
    servr = smtplib.SMTP('smtp.gmail.com', 587)
    servr.ehlo()
    servr.starttls()
    servr.login('urmail@gmail.com', '1234')
    servr.sendmail('urmail@gmail.com', to,content)
    servr.close

sendemail(to, content)