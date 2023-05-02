# Author: Sudarshan Jagannathan
# Name: server_script.py
# Description: This script automates the process of setting up a bluetooth server using the bluetoothctl utility of Bluez v.5.63. it sets up custom services and characteristics 
# that are exposted to the client device, and receives data from a connected client. This data is written into a file to be accessed by the I2S module script to play music. 
# Date Modified: 05/01/2023
# References: 1. https://www.guru99.com/reading-and-writing-files-in-python.html
#2.https://realpython.com/python-strings/#:~:text=String%20indexing%20in%20Python%20is,of%20the%20string%20minus%20one.&text=For%20any%20non%2Dempty%20string,both%20return%20the%20last%20character.
# 3. ChatGPT
# 4. https://ubuntu.com/core/docs/bluez/how-to

import subprocess
import fcntl
import time

import re
# Run the bluetoothctl command
bluetoothctl = subprocess.Popen(['bluetoothctl'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)

# Send the "agent on" command to register the agent
bluetoothctl.stdin.write(b'agent on\n')
bluetoothctl.stdin.flush()

# Read the output of the command until "Agent registered" is found
output = ""
while "Agent registered" not in output:
    output += bluetoothctl.stdout.readline().decode()
    print(output)
    
# Send the "power on" command
bluetoothctl.stdin.write(b'power on\n')
bluetoothctl.stdin.flush()

# Read the output of the command until "Changing power on succeeded" is found
output = ""
while "Changing power on succeeded" not in output:
    output += bluetoothctl.stdout.readline().decode()
    print(output)

# Send the "menu advertise" command
bluetoothctl.stdin.write(b'menu advertise\n')
bluetoothctl.stdin.flush()

# Set the manufacturer ID
bluetoothctl.stdin.write(b'manufacturer 0xffff 0x12 0x34\n')
time.sleep(1)
bluetoothctl.stdin.flush()
print("Success manufacturer")

#Set the name
bluetoothctl.stdin.write(b'name aesd_server\n')
time.sleep(1)
bluetoothctl.stdin.flush()
print("Success name")

#Back to main menu
bluetoothctl.stdin.write(b'back\n')
bluetoothctl.stdin.flush()
time.sleep(1)

bluetoothctl.stdin.write(b'list\n')
bluetoothctl.stdin.flush()
    
#Turn on Advertising
bluetoothctl.stdin.write(b'advertise on\n')
bluetoothctl.stdin.flush()

#Menu gatt
bluetoothctl.stdin.write(b'menu gatt\n')
bluetoothctl.stdin.flush()
time.sleep(1)

print("Success")

#Register custom service
bluetoothctl.stdin.write(b'register-service e2d36f99-8909-4136-9a49-d825508b297b\n')
bluetoothctl.stdin.flush()
time.sleep(1)
# Say yes to set as primary service    
bluetoothctl.stdin.write(b'yes\n')
bluetoothctl.stdin.flush()
time.sleep(1)
    
#Register custom characteristic
bluetoothctl.stdin.write(b'register-characteristic 0x1234 write\n')
bluetoothctl.stdin.flush()
time.sleep(1)
#Write an initial value for the characteristic
bluetoothctl.stdin.write(b'67\n')
bluetoothctl.stdin.flush()
time.sleep(1)

bluetoothctl.stdin.write(b'register-application\n')
bluetoothctl.stdin.flush()
time.sleep(1)

print("end config")

while True:
# Poll for a command sent by the client. Parse this command to decode the character of concern and write it into a file.    
    output1 = bluetoothctl.stdout.readline().decode()
   #Detecting that a command has been sent by the client. 
    while " link LE\n" in output1:
        output2 = bluetoothctl.stdout.readline().decode()
        print(output1)
        print(output2)
        if len(output2) > 0:
            lastchar = output2[len(output2) - 65]
            print("The required character is: %s" % lastchar)
        else:
            print("Wrong string")
        #File Mutex to access shared resource.     
        with open("audio_test.txt", 'w') as fileObj:
            fcntl.flock(fileObj, fcntl.LOCK_EX)
            fileObj.write(lastchar)
            fcntl.flock(fileObj, fcntl.LOCK_UN)
        break
