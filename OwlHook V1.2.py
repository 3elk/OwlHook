# TOOL BY ELK
# GIVE ALL CREDIT TO ELK
# VERSION 1.2
# (PS: Go to line 82)
import time
import os
import subprocess


try:
    import requests
except ModuleNotFoundError:
    print("Requests module not found, installing...")
    subprocess.check_call([os.sys.executable, "-m", "pip", "install", "requests"])
    import requests

try:
    from colorama import Fore, Back, Style
except ModuleNotFoundError:
    print("Colorama module not found, installing...")
    subprocess.check_call([os.sys.executable, "-m", "pip", "install", "colorama"])
    from colorama import Fore, Back, Style

try:
    from dhooks import Webhook  # type: ignore
except (ModuleNotFoundError):
    print("Dhooks module not found, installing...")
    subprocess.check_call([os.sys.executable, "-m", "pip", "install", "dhooks"])
    from dhooks import Webhook

os.system('chcp 65001 >nul')
os.system('title {OwlHook - by elk}')
import colorama
from colorama import Fore,Back,Style
colorama.init(autoreset = False)


banner = '''                                                  

                                 
                                           _____       _ _____         _   
                                          |     |_ _ _| |  |  |___ ___| |_    ,___,
                                          |  |  | | | | |     | . | . | '_|   {O,o}
                                          |_____|_____|_|__|__|___|___|_,_|  /)___)
                                 ----------------------------------------------"-"-----   
                                                   Discord Webhook Tool 
                                                         By: Elk                   
                                 ======================================================
                                 ======================================================
                                 ╔════════════════════════════════════════════════════╗
                                 ║                                                    ║
                                 ║        1) - Spammer              2) - Deleter      ║
                                 ║                                                    ║
                                 ║                      99) - Exit                    ║
                                 ╚════════════════════════════════════════════════════╝
      
      '''
print(f'{Fore.LIGHTYELLOW_EX}' + banner)
os.system('echo       ╔═════HookOwl@%username%')
print('      ║')
choicehook = input('      ╚═════════════════════════>> ')


if choicehook not in ('1', '2', '99'):
    print('Sorry, Not a valid option, Goodbye!')
    os.system('timeout /t 3 /nobreak >nul')
    os._exit


elif choicehook == '1':
    os.system('cls; clear')

    print('''                                                                                                     
 _____ _ _   _____                             
|   __| | |_|   __|___ ___ _____ 
|   __| | '_|__   | . | .'|     |
|_____|_|_,_|_____|  _|__,|_|_|_| 
                  |_|                       

        Webhook Spammer
          
                                                                      
''')

    # good boy :3
    message0 = input("Spam message >> ")
    webhookurl = Webhook(input("Webhook URL >> "))
    message = (message0 + ' - elk owns you :3 @here')

    try:
        while True:
            webhookurl.send(message)
            print("Sent MSG.")
    except KeyboardInterrupt:
        print("\nStopped spamming.")
        os.system('pause >nul')
        os._exit


elif choicehook == '2':
    os.system('cls; clear')
    print ('''                            
 _____ _ _    ____      _ 
|   __| | |_ |    \ ___| |
|   __| | '_||  |  | -_| |
|_____|_|_,_||____/|___|_| 

      Webhook Deleter
                             

''')

    del_web = input("Enter the Webhook URL to delete >> ")


    def delete(del_web):
        requests.delete(del_web)
        check = requests.get(del_web)
        if check.status_code == 404:
            print("\nWebhook Successfully Deleted")
            time.sleep(3.5)
        elif check.status_code == 200:
            print("\nCould not delete the Webhook.")
            time.sleep(3.5)


    test = requests.get(del_web)
    if test.status_code == 404:
        print("\nInvalid webhook.")
        time.sleep(3.5)
    elif test.status_code == 200:
        print("\nValid Hook...")
        delete(del_web)


elif choicehook == '99':
    print ('                                                Exiting OwlHook, Goodbye!')
    os.system('timeout /t 001 /nobreak >nul')
    os._exit
