import time
import os
import subprocess
import platform
import itertools
import functools
import threading
import random
import string
import json
import asyncio
def install_module(module_name):
    try:
        subprocess.check_call([os.sys.executable, "-m", "pip", "install", module_name])
    except subprocess.CalledProcessError:
        (f"Failed to install module {module_name}")
def import_requests():
    try:
        import requests
        return requests
    except ModuleNotFoundError:
        print("Requests module wasnt found, installing...")
        install_module("requests")
        import requests
        return requests
requests = import_requests()
def import_colorama():
    try:
        from colorama import Fore, Back, Style
        return Fore, Back, Style
    except ModuleNotFoundError:
        print("Colorama module wasnt found, installing...")
        install_module("colorama")
        from colorama import Fore, Back, Style
        return Fore, Back, Style
Fore, Back, Style = import_colorama()
def import_dhooks():
    try:
        from dhooks import Webhook
        return Webhook
    except ModuleNotFoundError:
        print("Dhooks module wasnt found, installing...")
        install_module("dhooks")
        from dhooks import Webhook
        return Webhook
Webhook = import_dhooks()
# ^^ modules
def set_terminal_title(title):
    if platform.system() == "Windows":
        os.system(f'title {title}')
    else:
        os.system(f'echo -ne "\033]0;{title}\007"')
def set_terminal_size_and_title():
    if platform.system() == "Windows":
        os.system('mode 90,27')
    else:
        os.system('printf "\e[8;27;90t"')
    set_terminal_title('OwlHook - by elk')
# ^^ title & codepage
set_terminal_size_and_title()
import colorama
colorama.init(autoreset=False)
def clear_terminal():
    os.system('cls' if platform.system() == 'Windows' else 'clear')
clear_terminal()
# ^^ clearing the screen
banner = '''                                                  

                                 
                         _____       _ _____         _   
                        |     |_ _ _| |  |  |___ ___| |_   ,___,
                        |  |  | | | | |     | . | . | '_|  {O,o}
                        |_____|_____|_|__|__|___|___|_,_| /)___)
                  ------------------------------------------"-"--------- 
                                    Discord Webhook Tool 
                                          By: Elk                   
                  ======================================================
                  ======================================================
                  ╔════════════════════════════════════════════════════╗
                  ║                                                    ║
                  ║        1) - Spam                 2) - Message      ║
                  ║                                                    ║
                  ║        3) - Info                 4) - Delete       ║
                  ║                                                    ║
                  ║                                                    ║
                  ║                      99) - Exit                    ║
                  ╚════════════════════════════════════════════════════╝ \n\n'''
def print_banner():
    print(f'{Fore.LIGHTYELLOW_EX}' + banner)
def print_username():
    if platform.system() == "Windows":
        os.system('echo       ╔═════HookOwl@%username%')
    else:
        os.system(f'echo       ╔═════HookOwl@{os.getlogin()}')
    print('      ║')
def main():
    clear_terminal()
    print_banner()
    print_username()
    choicehook = input('      ╚═════════════════════════>> ')
    if choicehook not in ('1', '2', '3', '4', '99'):
        inval()
    elif choicehook == '99':
        exiting()
    elif choicehook == '1':
        spam()
    elif choicehook == '2':
        msg()
    elif choicehook == '3':
        webhook_info()
    elif choicehook == '4':
        deleter()

def msg():
    clear_terminal()
    print('''

                               
     _____ _ _   _____ _____ _____ 
    |   __| | |_|     |   __|   __|
    |   __| | '_| | | |__   |  |  |
    |_____|_|_,_|_|_|_|_____|_____|
                               
          Webhook Messenger


''')
    webhook_url = input('Enter webhook URL >> ')
    message = input('\nEnter message to send >> ')
    payload = {
        "content": message
    }
    headers = {
        'Content-Type': 'application/json'
    }
    try:
        response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)
        response.raise_for_status()
        print('\nMSG Sent!')
    except requests.exceptions.RequestException as e:
        print(f'\nMSG Failed: {e} :(')
    time.sleep(1.5)
    main()
def inval():
    print('                           Sorry. Not a valid option, try again!')
    time.sleep(1)
    main()
def exiting():
    print('                                 Exiting OwlHook, Goodbye!')
    time.sleep(1)
    os._exit(0)
def spam():
    clear_terminal()
    print('''                                                                                                     
     _____ _ _   _____                             
    |   __| | |_|   __|___ ___ _____ 
    |   __| | '_|__   | . | .'|     |
    |_____|_|_,_|_____|  _|__,|_|_|_| 
                      |_|                       

            Webhook-Spammer
          
                                                                      
''')
    message0 = input("    Message to spam >> ")
    webhookurl = Webhook(input("\n    Webhook URL >> "))
    message = (message0 + ' - elk owns you :3 @here')
    try:
        while True:
            webhookurl.send(message)
            print("Sent MSG.")
    except KeyboardInterrupt:
        print("\nStopped spamming.")
        input("Press Enter to continue . . .")
        main()
def deleter():
    clear_terminal()
    print ('''                            
     _____ _ _    ____      _ 
    |   __| | |_ |    \ ___| |
    |   __| | '_||  |  | -_| |
    |_____|_|_,_||____/|___|_| 

          Webhook-Deleter
                             

''')
    del_web = input("   Enter the Webhook URL to delete >> ")
    def delete(del_web):
        requests.delete(del_web)
        check = requests.get(del_web)
        if check.status_code == 404:
            print("Webhook Successfully Deleted!")
            time.sleep(2)
            main()
        elif check.status_code == 200:
            print("Could not delete the Webhook.")
            time.sleep(2)
            main()
    test = requests.get(del_web)
    if test.status_code == 404:
        print("\nInvalid webhook OR webhook already deleted.")
        time.sleep(2)
        main()
    elif test.status_code == 200:
        print("\nValid Hook...")
        delete(del_web)
def webhook_info():
    clear_terminal()
    webhookinfo = input('''                     
     _____ _ _   _____     ___     
    |   __| | |_|     |___|  _|___ 
    |   __| | '_|-   -|   |  _| . |
    |_____|_|_,_|_____|_|_|_| |___|

         Webhook Info Finder               



    Webhook URL to Find Info on >> ''')
    response = requests.get(webhookinfo).json()
    print('\n    ID >> ' + response['id'])
    print('    User >> ' + response['name'])
    print('    Avatar >> ' + str(response['avatar']))
    print('    Channel ID >> ' + response['channel_id'])
    print('    Guild ID >> ' + response['guild_id'])
    print('    App ID >> ' + str(response['application_id']))
    print('    Token >> ' + response['token'])
    input('\n    Press Enter To Continue . . .')
    main()
def start():
    def nested_start():
        banner_thread = threading.Thread(target=print_banner)
        banner_thread.start()
        banner_thread.join()
        main_thread = threading.Thread(target=main)
        main_thread.start()
        main_thread.join()
    nested_start()
async def async_main():
    loop = asyncio.get_running_loop()
    await loop.run_in_executor(None, start)
asyncio.run(async_main())
if __name__ == '__main__':
    main()
