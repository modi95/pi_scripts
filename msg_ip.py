import os

def main():
	conf = create_conf()
	ip = get_ip(conf)


def create_conf():
	os.system("ifconfig > ifconfig.txt")
	conf_file = open("ifconfig.txt", "r")
	return conf_file.read()

def get_ip(conf):
	


if __name__ == "__main__":
	main()