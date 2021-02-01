import os
import urllib.request
from dotenv import load_dotenv
from godaddypy import Client, Account

load_dotenv()

with urllib.request.urlopen('https://api.ipify.org') as response:
    ip = response.read()
    ip = str(ip, 'utf-8')

public_ip = 'public_ip.txt'
ip_file = open(public_ip, 'r')
old_ip = ip_file.readline()

if ip != old_ip:
    new_ip = open(public_ip, 'w')
    new_ip.write(ip)
    new_ip.close()

    account = Account(api_key=os.getenv('API_KEY'), api_secret=os.getenv('API_SECRET'))
    client = Client(account)

    client.update_record_ip(ip, os.getenv('DOMAIN_NAME'), os.getenv('DOMAIN_RECORD'), 'A')