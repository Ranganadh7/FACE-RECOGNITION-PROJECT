import smtplib
try:
                
    mail=smtplib.SMTP('smtp.gmail.com:587')
    mail.ehlo()
    mail.starttls()
    mail.login("ur mail","password")
    mail.sendmail("ur mail","sender mail","unknown person detected")
    mail.close()
    print("Mail sent")
    
    
except:
                
    print("failed")
