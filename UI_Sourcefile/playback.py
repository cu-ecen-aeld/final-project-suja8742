##
# Owner: Sachin Mathad
# Project: AESD Final Project
##
import sys

if len(sys.argv) < 2:
    print("Usage: playback.py <action>")
    sys.exit(1)

action = sys.argv[1]

if action == 'play':
    print('Playing...')
elif action == 'pause':
    print('Pausing...')
elif action == 'stop':
    print('Stopping...')
else:
    print('Unknown action:', action)
    sys.exit(1)
