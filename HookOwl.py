# tool by elk!!
# this tool is still being worked on!!
# give all credit to elk!!
import time
import os

try:
    import requests
except (ModuleNotFoundError):
    os.system('pip install requests')

try:
    from dhooks import Webhook # type: ignore
except (ModuleNotFoundError):
       os.system('pip install dhooks')

os.system('chcp 65001 >nul')
os.system('title HookOwl - by elk')

## ^^ imports, code page, and window title. (THE IMPORTS MIGHT TAKE A WHILE TO LOAD)
choicehook = input('''                                                  
                   

                                             _____         _   _____       _ 
                                            |  |  |___ ___| |_|     |_ _ _| |
                                            |     | . | . | '_|  |  | | | | |
                                            |__|__|___|___|_,_|_____|_____|_|
                                                         .___,   
                                                      ___('v')___
                                                      `"-\._./-"'
                                                          ^ ^    
                                                  Discord Webhook Tool 
                                                        By: Elk
                   
                                 ======================================================
                                 ======================================================
                
                                      1) - Spammer                   2) - Deleter

                   
    >> ''')

## ^^ banner, and options
if choicehook not in [1, 2]:
       print ('Not a valid option, closing HookOwl, Goodbye!')
       os.system('timeout /t 1 /nobreak >nul')
       os._exit()
       

if choicehook == '1':
    os.system('cls; clear')

    print('''                                                                                                     
 _____ _ _   _____                             
|   __| | |_|   __|___ ___ _____ 
|   __| | '_|__   | . | .'|     |
|_____|_|_,_|_____|  _|__,|_|_|_| 
                  |_|                       

        Webhook Spammer
          
                                                                      
''')

    message0 = input("What do you want to spam? >> ")
    webhookurl = Webhook(input("Enter webhook >> "))
    message = (message0 + ' - ELK WAS HERE, HOOKOWL ON TOP :3')

    while True:
        webhookurl.send(message)
        print("Sent message.")


## ^^ webhook spammer code
elif choicehook == '2':
        os.system('cls; clear')
        print ('''                            
 _____ _ _    ____      _ 
|   __| | |_ |    \ ___| |
|   __| | '_||  |  | -_| |
|_____|_|_,_||____/|___|_|

      Webhook Deleter
                             

''')
    
webhook_del = input(" Enter the Webhook URL to delete >> ")

def delete():
            requests.delete(webhook_del)
            check = requests.get(webhook_del)
            if check.status_code == 404:
                print("\n Webhook Successfully Deleted")
                time.sleep(3.5)
            elif check.status_code == 200:
                print("\n Could not delete the Webhook.")
                time.sleep(3.5)

test = requests.get(webhook_del)
if test.status_code == 404:
            print("\n Invalid webhook.")
            time.sleep(3.5)
elif test.status_code == 200:
            print("\n Valid Hook...")
            delete()


## ^^ webhook deleter code