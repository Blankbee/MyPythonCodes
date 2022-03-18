import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys
mesaj=MIMEMultipart()
mesaj["From"]="jailciv8@gmail.com"
mesaj["To"]="jailciv8@gmail.com"
mesaj["Subject"]="Satp Mail Gönderme"
yazi="""

Smtp ile mail gönderiyorum

All abort to Octrain

"""
mesaj_govdesi=MIMEText(yazi,"plain")
mesaj.attach(mesaj_govdesi)
try:
    mail=smtplib.SMTP("smtp.gmail.com",587)
    mail.ehlo()
    mail.starttls()
    mail.login("jailciv8@gmail.com","pw")
    mail.sendmail(mesaj["From"],mesaj["To"],mesaj.as_string())
    print("Mail gönderildi.")
    mail.close()
except:
    sys.stderr.write("Bir sorun oluştu.")
    sys.stderr.flush()
