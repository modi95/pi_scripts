import os
import sys

email = False
sms = False
prnt = False
config_sc = open("config.sc", "r")
detail = config_sc.readlines()


def main():
	conf = create_conf()
	ip = get_ip(conf)
	if prnt:
		print ip
	if sms:
		send_sms(ip)
	if email:
		send_email(ip)
	config_sc.close()
	return


def create_conf():
	os.system("ifconfig > ifconfig.txt")
	conf_file = open("ifconfig.txt", "r")
	conf = conf_file.read()
	conf_file.close()
	return conf


#I'm assuming your Pi is connected via ethernet
#This function can exit early if this is the case
def get_ip(conf):
	conf_eth0 = conf[conf.find("eth0"):conf.find("\n\nlo")]
	loc_addr = conf_eth0.find("inet addr:")
	if (loc_addr > 0 and not "127.0.0.1" in conf_eth0):
		return conf_eth0[(conf_eth0.find("inet addr:") + 10):conf_eth0("  Bcast:")]
	
	conf_wlan0 = conf[conf.find("wlan0"):conf.__len__()]
	loc_addr = conf_wlan0.find("inet addr:")
	if (loc_addr > 0 and not "127.0.0.1" in conf_wlan0):
		return conf_wlan0[(conf_wlan0.find("inet addr:") + 10):conf_wlan0.find("  Bcast:")]


def send_sms(ip):
	ACCOUNT_SID = detail[0][detail[0].find('"')+1 : detail[0].rfind('"')]
	AUTH_TOKEN = detail[1][detail[1].find('"')+1 : detail[1].rfind('"')]
	ph_number = detail[2][detail[2].find('"')+1 : detail[2].rfind('"')]
	twil_number = detail[3][detail[3].find('"')+1 : detail[3].rfind('"')]
	from twilio.rest import TwilioRestClient

	client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
	message = client.messages.create(body=("RPi IP: " + ip),
		to=ph_number, from_=twil_number)

	#print message.sid
	print ("sms sent to " + ph_number)
	return

def send_email(ip):
	import smtplib
	sender = 'from@fromdomain.com'
	to_email = detail[4][detail[4].find('"')+1 : detail[4].rfind('"')]

	message = """From: From Person <from@fromdomain.com>
	To: To Person <to@todomain.com>
	Subject: SMTP e-mail test

	This is a test e-mail message.
	"""

	print to_email
	s = smtplib.SMTP('localhost')
	s.sendmail(sender, [to_email], message)
	s.quit()
	print ("This function has not been implemented as yet")


def print_help():
	os.system("cat msg_ip_help.txt")
	exit()


if __name__ == "__main__":
	if "con" in sys.argv: prnt = True
	if "sms" in sys.argv: sms = True
	if "email" in sys.argv: email = True
	if not sms and not email and not prnt: print_help()
	main()
	exit()