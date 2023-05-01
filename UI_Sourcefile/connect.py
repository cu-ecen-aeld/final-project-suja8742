##
# Owner: Sachin Mathad
# Project: AESD Final Project
# ref: https://stackoverflow.com/questions/49800452/retrieve-list-of-bluetooth-devices-using-python-3-and-terminal#:~:text=bt%20%3D%20subprocess.Popen%20%28%5B%22sudo%22%2C,%22bluetoothctl%22%2C%20%22scan%22%2C%20%22on%22%5D%2C%20stdin%3Dsubprocess.PIPE%29
# ref: https://stackoverflow.com/questions/63355946/how-to-run-and-read-bluetoothctl-commands-outputs-from-nodejs
##

import subprocess

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

# Send the "scan on" command
bluetoothctl.stdin.write(b'scan on\n')
bluetoothctl.stdin.flush()

# Search for the target MAC address and connect to it
while True:
    output = bluetoothctl.stdout.readline().decode()
    print(output)
    
    if "Device B8:27:EB:B1:9B:68" in output:
        bluetoothctl.stdin.write(b'connect B8:27:EB:B1:9B:68\n')
        bluetoothctl.stdin.flush()
        break

# Read the output of the command until "Connection successful" is found
output = ""
while "Connection successful" not in output:
    output += bluetoothctl.stdout.readline().decode()
    print(output)

# Print success message
print("Success!")

# Launch the AESDUI_v1.py script if the connection is successful
if "Connection successful" in output:
    subprocess.Popen(['python', 'UI.py'])
