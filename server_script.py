import subprocess
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

while "export" not in output:
    output += bluetoothctl.stdout.readline().decode()
    print(output)

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
#while "export" not in output:
    #output += bluetoothctl.stdout.readline().decode()
    #print(output)
bluetoothctl.stdin.write(b'list\n')
bluetoothctl.stdin.flush()

while "raspberrypi [default]" not in output:
	
    output += bluetoothctl.stdout.readline().decode()
    print(output)
    
#Turn on Advertising
bluetoothctl.stdin.write(b'advertise on\n')
bluetoothctl.stdin.flush()

while "Discoverable: on" not in output:
	
    output += bluetoothctl.stdout.readline().decode()
    print(output)

#Menu gatt
bluetoothctl.stdin.write(b'menu gatt\n')
bluetoothctl.stdin.flush()
time.sleep(1)

print("Success")

#Register custom service
bluetoothctl.stdin.write(b'register-service e2d36f99-8909-4136-9a49-d825508b297b\n')
bluetoothctl.stdin.flush()
time.sleep(1)

#while "yes/no" not in output:
	
    #output += bluetoothctl.stdout.readline().decode()
    #print(output)
    
bluetoothctl.stdin.write(b'yes\n')
bluetoothctl.stdin.flush()
time.sleep(1)
    
#Register custom characteristic
bluetoothctl.stdin.write(b'register-characteristic 0x1234 write\n')
bluetoothctl.stdin.flush()
time.sleep(1)

bluetoothctl.stdin.write(b'67\n')
bluetoothctl.stdin.flush()
time.sleep(1)


#while "Enter value:\n" not in output:
	
    #output += bluetoothctl.stdout.readline().decode()
    #print(output)

bluetoothctl.stdin.write(b'register-application\n')
bluetoothctl.stdin.flush()
time.sleep(1)

print("end config")
i = 0

with open("scripttest.txt", 'w') as fileObj:
    fileObj.write(f"ready : {i}" )
# with open("scripttest.txt", 'w') as fileObj:
#     fileObj.write("ready")
while True:
    # time.sleep(5)
   
    output1 = bluetoothctl.stdout.readline().decode()
    # print(output1)
    # print(output1)
    while " link LE\n" in output1:
        # subprocess.run(['echo', str(i), '>', 'test.txt'], shell=True)
        output2 = bluetoothctl.stdout.readline().decode()
        print(output1)
        print(output2)
        if len(output2) > 0:
            lastchar = output2[len(output2) - 65]
            print("The required character is: %s" % lastchar)
        else:
            print("Wrong string")
        
        # match = re.search(r'(?<=WriteValue: \b[0-9A-Fa-f]{2}\b offset 0 link LE\n\s+)\w+', output)
        #match = re.search(r'^\s*05\s*', output2)

        #if match:
         #   value = match.group(0).strip()
          #  print(value)
        #else:
         #   print("No match found")
        # if match:
        # value = match.group(0)
        with open("scripttest.txt", 'w') as fileObj:
            fileObj.write(lastchar)
        # else:
        break
