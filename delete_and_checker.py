from discord import webhook
from requests import check_compatibility, get, post, patch, status_codes, delete
import discord
import time
from discord.ext import commands
from colorama import Fore, Style, Back, init
import requests
from requests.api import request
from requests.models import Response
init()

print(Fore.YELLOW + """ ██▓███  ▓█████  █    ██   █████▒██▀███   ▄▄▄      
▓██░  ██▒▓█   ▀  ██  ▓██▒▓██   ▒▓██ ▒ ██▒▒████▄    
▓██░ ██▓▒▒███   ▓██  ▒██░▒████ ░▓██ ░▄█ ▒▒██  ▀█▄  
▒██▄█▓▒ ▒▒▓█  ▄ ▓▓█  ░██░░▓█▒  ░▒██▀▀█▄  ░██▄▄▄▄██ 
▒██▒ ░  ░░▒████▒▒▒█████▓ ░▒█░   ░██▓ ▒██▒ ▓█   ▓██▒
▒▓▒░ ░  ░░░ ▒░ ░░▒▓▒ ▒ ▒  ▒ ░   ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░
░▒ ░      ░ ░  ░░░▒░ ░ ░  ░       ░▒ ░ ▒░  ▒   ▒▒ ░
░░          ░    ░░░ ░ ░  ░ ░     ░░   ░   ░   ▒   
            ░  ░   ░               ░           ░  ░""")
print(Fore.RESET)

help0 = input(Fore.RED + """*********************************************************************************************************\n     -1 WebHook Deleter                                      -2 WebHook Checker\n *********************************************************************************************************""")
print(Fore.RESET)

if help0 == '1':
    delete1 = input("Entrez l'URL du WebHook : ")
    delete(delete1)
    print("Et Hop !! Le WebHook a été supprimé ! ")
    
    
def webhook_check():
    response0 = input("Entrez ici l'URL de votre WebHook : ")
    response1 = requests.get(response0).status_code
    if response1 == 200: 
        print("Le Token marche à merveille ! ")


if help0 == '2':
    webhook_check()
    time.sleep(2000)