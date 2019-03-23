import smtplib
server=smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
server.login("priyanshuajmera@gmail.com","password")
subject="Hello"
msg='Subject:{}\n{}'.format(subject,"How are you?")
server.sendmail("priyanshuajmera@gmail.com","uagarwal54@gmail.com",msg)
server.quit
