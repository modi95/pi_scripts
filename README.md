#Raspberry Pi Setup Scripts

These scripts are here to help you get up and running with your Raspberry Pi asap.

#Scripts

1. Message IP: Your RPi will message you its IP address on booting. This should help with ssh'ing into your Pi easily without using a screen. Useful at Hackathons.

#Using these

1. Download these files.
2. Open config.sc and provide the details that you think would be relevent to the scripts you want to use.
3. To run a command scripts when the RPi boots, add the command to the rc.local file in /etc/rc.local. Add these commands to the end of the file, before the  "exit 0" command at the end.

I realize this isn't ideal. I'll work on making this easier soon.