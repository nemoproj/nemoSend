# nemoCheck is a tool to check the status of a list of IP addresses, 
# (stored in .nemoip files, and via pinging them) and ddos them if they are up. 
# It also includes a bot function to send a message to a discord channel if the IP is up.
# (Using the discord.py library, and webhooks)

## imports 
import os
import sys
import time
import subprocess
import discord
import json
import requests
from discord import Webhook, RequestsWebhookAdapter # Importing discord.Webhook and discord.RequestsWebhookAdapter
from pythonping import ping
# import the .nemoip file
def import_nemoip():
    # check if the .nemoip file exists
    if os.path.isfile('.nemoip'):
        # if it does, open it and read it
        with open('.nemoip', 'r') as f:
            # read the file and return the contents
            return f.read()
    else:
        # if it doesn't, return an error
        return 'Error [-]: .nemoip file not found'


# ping the IPs in the .nemoip file
def ping_ips():
    # get the contents of the .nemoip file
    ip_list = import_nemoip()
    # split the contents into a list
    ip_list = ip_list.split('\n')
    # loop through the list
    for ip in ip_list:
        # ping the IP
        ping(ip,verbose=True)

# send a message to a discord channel via a webhook
def send_message(message):
    # discord webhook url:
    url = "Your Discord Webhook here ☭"
    # message to send
    # something like:
    # (in embed)
    # nemoCheck(): 진관초등학교 컴퓨터실 컴퓨터 상태: 켜짐
    # 핑이 요청이 정상적으로 처리되었습니다.
    
    webhook = Webhook.from_url(url, adapter=RequestsWebhookAdapter()) # Initializing webhook
    embed=discord.Embed(title="nemoCheck():", description="진관초등학교 컴퓨터실 컴퓨터 상태: 켜짐.", color=0xffffff)
    embed.add_field(name="핑이 요청이 정상적으로 처리되었습니다.", value="ddos() function을 시작합니다.", inline=False)
    embed.set_footer(text="공화주의 반란사회 @editor99 제공  @nerdsinspace() ∴ ʃʃ nerdsinspace/nemo")

    # send the message
    webhook.send(embed=embed)



# main function
def main():
    # ping the IPs
    ping_ips()
    # send a message to the discord channel
    send_message('핑이 요청이 정상적으로 처리되었습니다.')
    
# run the main function
if __name__ == '__main__':
    main()
    
