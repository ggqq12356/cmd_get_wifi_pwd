
# get wifi password in windows with python
# author:WeiJie-Su
# date:2018/08/31

import os

command = "netsh wlan show profiles"

wifi_list = []
for line in os.popen(command).readlines():
	line = line.strip('\r\n')
	if "所有使用者設定檔" in line:
		line = line.split(" : ")[1]
		wifi_list.append(line)

wifi_pwd_list = {}
for wifi in wifi_list:
	for profile in os.popen(command+" key=clear %s" %wifi):
		key_check = profile.strip('\r\n')
		if "金鑰內容" in key_check:
			pwd = profile.split(' : ')[1]
			wifi_pwd_list[wifi] = pwd
			break
	else:
		pwd = "None"
		wifi_pwd_list[wifi] = pwd

with open('wifi_pwd_list.txt', 'w') as file:
	for key in wifi_pwd_list.keys():
		result = "SSID:{} Password:{}".format(key, wifi_pwd_list.get(key))
		file.write(result+"\n")
		print(result.strip('\r\n'))