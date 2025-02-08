import time
import os
import subprocess

# Try to import the requests module, and install it if it's missing
try:
    import requests
except ModuleNotFoundError:
    print("Requests module not found, installing...")
    subprocess.check_call([os.sys.executable, "-m", "pip", "install", "requests"])
    import requests

# Try to import the dhooks module, and install it if it's missing
try:
    from dhooks import Webhook  # type: ignore
except (ModuleNotFoundError):
    print("Dhooks module not found, installing...")
    subprocess.check_call([os.sys.executable, "-m", "pip", "install", "dhooks"])
    from dhooks import Webhook

os.system('chcp 65001 >nul')
os.system('title HookOwl - by elk')

# Banner and options
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

# Validate user input for the option
if choicehook not in ('1', '2'):
    print('Sorry, Not a valid option, Goodbye!')
    os.system('timeout /t 1 /nobreak >nul')
    input("Press Enter to exit...")
    exit()

# Webhook Spammer
elif choicehook == '1':
    os.system('cls; clear')

    print('''                                                                                                     
 _____ _ _   _____                             
|   __| | |_|   __|___ ___ _____ 
|   __| | '_|__   | . | .'|     |
|_____|_|_,_|_____|  _|__,|_|_|_| 
                  |_|                       

        Webhook raper1
          
                                                                      
''')

    message0 = input("What do you want to spam? >> ")
    webhookurl = Webhook(input("Enter webhook >> "))
    message = (message0 + ' - ELK WAS HERE, HOOKOWL ON TOP :3')

    try:
        while True:
            webhookurl.send(message)
            print("Sent message.")
            time.sleep(1)  # Add delay to avoid flooding the server
    except KeyboardInterrupt:
        print("\nSpamming stopped by user.")
        input("Press Enter to exit...")
        exit()

# Webhook Deleter
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

    # Function to delete the webhook
    def delete(del_web):
        requests.delete(del_web)
        check = requests.get(del_web)
        if check.status_code == 404:
            print("\nWebhook Successfully Deleted")
            time.sleep(3.5)
        elif check.status_code == 200:
            print("\nCould not delete the Webhook.")
            time.sleep(3.5)

    # Validate if webhook is valid
    test = requests.get(del_web)
    if test.status_code == 404:
        print("\nInvalid webhook.")
        time.sleep(3.5)
    elif test.status_code == 200:
        print("\nValid Hook...")
        delete(del_web)


