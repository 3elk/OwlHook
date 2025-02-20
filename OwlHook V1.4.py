# https://github.com/3elk/OwlHook
# OWLHOOK BY ELK
# GIVE ALL CREDIT TO ELK
# OWLHOOK ON TOP

import time
import os
import subprocess
import platform

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
    from dhooks import Webhook
except (ModuleNotFoundError):
    print("Dhooks module not found, installing...")
    subprocess.check_call([os.sys.executable, "-m", "pip", "install", "dhooks"])
    from dhooks import Webhook

if platform.system() == "Windows":
    os.system('mode 90,27')
    os.system('title {OwlHook - by elk}')
else:
    os.system('printf "\e[8;27;90t"')
    os.system('echo -ne "\033]0;{OwlHook - by elk}\007"') 

import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=False)

# ^^ imports

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
                  ║        1) - Spammer               2) - Deleter     ║
                  ║                                                    ║
                  ║                      COMING SOON                   ║
                  ║                                                    ║
                  ║                                                    ║
                  ║                      99) - Exit                    ║
                  ╚════════════════════════════════════════════════════╝ \n\n'''
print(f'{Fore.LIGHTYELLOW_EX}' + banner)
if platform.system() == "Windows":
    os.system('echo       ╔═════HookOwl@%username%')
else:
    os.system(f'echo       ╔═════HookOwl@{os.getlogin()}')
print('      ║')
choicehook = input('      ╚═════════════════════════>> ')

# ^^ banner + input

if choicehook not in ('1', '2', '99'):

    print('Sorry, Not a valid option, Goodbye!')
    time.sleep(3)
    os._exit(0)

# ^^ if the input is not one of the listed options

elif choicehook == '1':

# ^^ webhook-spammer option

    os.system('cls' if platform.system() == 'Windows' else 'clear')

    print('''                                                                                                     
     _____ _ _   _____                             
    |   __| | |_|   __|___ ___ _____ 
    |   __| | '_|__   | . | .'|     |
    |_____|_|_,_|_____|  _|__,|_|_|_| 
                      |_|                       

            Webhook-Spammer
          
                                                                      
''')

# ^^ webhook-spammer banner

    message0 = input("    Message to spam >> ")
    webhookurl = Webhook(input("\n    Webhook URL >> "))
    message = (message0 + ' - elk owns you :3 @here')

# ^^ input for the webhook-spammer (the message, url, etc.)

    try:
        while True:
            webhookurl.send(message)
            print("Sent MSG.")
    except KeyboardInterrupt:
        print("\nStopped spamming.")
        input("Press Enter to continue . . .")
        os._exit(0)

# ^^ messaging the webhook using dhooks + if spamming is stopped

elif choicehook == '2':

# ^^ webhook-deleter option

    os.system('cls' if platform.system() == 'Windows' else 'clear')
    print ('''                            
     _____ _ _    ____      _ 
    |   __| | |_ |    \ ___| |
    |   __| | '_||  |  | -_| |
    |_____|_|_,_||____/|___|_| 

          Webhook-Deleter
                             

''')

    del_web = input("   Enter the Webhook URL to delete >> ")

# ^^ webhook-deleter banner + webhook URL input

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

# ^^ webhook-deleters code (Checking if webhook is valid by status code + using the requests to delete the webhook)

elif choicehook == '99':

# ^^ exit option

    print ('                                Exiting OwlHook, Goodbye!')
    time.sleep(1)
    os._exit(0)

# ^^ ts pmo icl 808 r u fr rn nigbart 
