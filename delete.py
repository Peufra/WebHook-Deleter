from requests import get, post, patch, delete, status_codes
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

help0 = input(Fore.RED + """*********************************************************************************************************\n                                                -1 WebHook Deleter \n\n*********************************************************************************************************""")
print(Fore.RESET)

if help0 == '1':
    delete1 = input("Entrez l'URL du WebHook : ")
    delete(delete1).status_code
    print("Et Hop !! Le WebHook a été supprimé ! ")
    time.sleep(2000)
    