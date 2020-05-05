import time, msvcrt
from datetime import datetime as dt
import win32com.shell.shell as shell
ASADMIN = 'asadmin'

hosts_temp="hosts"
hosts_dir = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
website_list = ["https://www.facebook.com","www.facebook.com","facebook.com","web.whatsapp.com"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day,8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 18):
        print ("working hours..")
        with open(hosts_dir, 'r+') as hosts_file:
            content=hosts_file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    hosts_file.write(redirect + " " + website + "\n")
    else:
        with open(hosts_dir, 'r+') as hosts_file:
            content=hosts_file.readlines()
            hosts_file.seek(0)  #this will write starting from line 0
            for line in content:
                if not any(website in line for website in website_list):
                    hosts_file.write(line)
            hosts_file.truncate() #will delete all lines beneath the last written line
        print("off office hour")

    time.sleep(60)
