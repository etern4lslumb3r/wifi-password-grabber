import subprocess as sp
import re
import os

dir_path = os.getcwd()
file_output_name = "wifipasswords.txt"
output = sp.getoutput(f'netsh wlan show profiles name=*')
wifi_name_list = []
for name_index in [m.start() for m in re.finditer('Name', output)]:
    wifi_name_list.append(
        output[name_index:name_index+output[name_index:].find('Control options')].split(':')[1].strip())

WIFI_SSID_PASSWORD = []

for name in wifi_name_list:
    output = sp.getoutput(f'netsh wlan show profile name="{name}" key=clear')
    output = output[output.find('Key Content'):output.find('Cost settings')]
    output = output[output.find(':')+2:]
    output = output.strip()
    x = ("{:<30}|  {:<}".format(name, output))
    print(x)
    WIFI_SSID_PASSWORD.append(x)
    
with open(file_output_name, 'w') as f:
    for ssid in WIFI_SSID_PASSWORD:
        f.write(ssid + "\n")
