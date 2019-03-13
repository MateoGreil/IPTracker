#!/usr/bin/python3

import requests
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from config import *

ipAddr = requests.get("https://api.ipify.org").text

print("Checking for new ip...")

def updateIpStore(ipAddr, ipStorePath):
	currentIp = open(ipStorePath, 'w')
	currentIp.write(ipAddr)
	currentIp.truncate()
	currentIp.close()

def sendNewIp(ipAddr):
	smtp = smtplib.SMTP("smtp.gmail.com", 587)
	smtp.ehlo()
	smtp.starttls()
	smtp.ehlo()
	smtp.login(fromAddr, myPassword)

	msg = MIMEMultipart()
	msg['From'] = fromAddr
	msg['To'] = ', '.join(toAddr)
	msg['Subject'] = "Nouvelle IP pour la RPi"
	body = ipAddr
	msg.attach(MIMEText(body, 'plain'))

#	message = "Nouvelle ip : " + ipAddr
	smtp.sendmail(fromAddr, toAddr, msg.as_string())
	smtp.quit()

if os.path.isfile(ipStorePath):
	currentIp = open(ipStorePath, 'r+')
	if currentIp.read() != ipAddr:
		print("Nouvelle IP: " + ipAddr)
		currentIp.close()
		updateIpStore(ipAddr, ipStorePath)
		sendNewIp(ipAddr)
