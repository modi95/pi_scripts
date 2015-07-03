import os
import sys

email = True
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
	email = detail[4][detail[4].find('"')+1 : detail[4].rfind('"')]
	sendgrid_username = detail[5][detail[5].find('"')+1 : detail[5].rfind('"')]
	sendgrid_password = detail[6][detail[6].find('"')+1 : detail[6].rfind('"')]
	import sendgrid
	sg = sendgrid.SendGridClient(sendgrid_username,sendgrid_password);
	message = sendgrid.Mail()
	message.add_to(email)
	message.set_subject("Raspberry Pi IP Address")
	message.set_html("Your Raspberry Pi's IP Address is " + ip)
	message.set_text("Your Raspberry Pi's IP Address is " + ip)
	message.set_from(email)
	status, msg = sg.send(message)

def print_help():
	help_msg = '''
Usage:
python msg_ip [options]

options include:
	sms: send ip in an sms to the number listed in sc.config
	email: send ip in an email to the email listed in sc.config
	order of options does not matter

examples:
	python msg_ip sms
	will sms the ip to the number listed in sc.config

	python msg_ip sms email
	will send the ip in an sms and an email to the phone number
	and email address in sc.config
	'''
	print help_msg
	exit()


if __name__ == "__main__":
	if "con" in sys.argv: prnt = True
	if "sms" in sys.argv: sms = True
	if "email" in sys.argv: email = True
	if not sms and not email and not prnt: print_help()
	main()
	exit()
