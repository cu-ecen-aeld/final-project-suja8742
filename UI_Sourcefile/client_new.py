##
# Owner: Sachin Mathad
# Project: AESD Final Project
# https://kernel.googlesource.com/pub/scm/bluetooth/bluez/+/5.6/test/test-device
# https://ukbaz.github.io/howto/python_gio_1.html
# https://chat.openai.com/
##

import sys
import dbus

# The MAC address of your device
device_mac_address = 'B8:27:EB:B1:9B:68'

# The UUID of the GATT service and characteristic you want to access
service_uuid = 'e2d36f99-8909-4136-9a49-d825508b297b'
char_uuid = '00001234-0000-1000-8000-00805f9b34fb'

# Get the value from the command-line argument
value = int(sys.argv[1])

# Make sure the value is between 1 and 5
if value < 1 or value > 5:
    print("Value must be between 1 and 5")
    exit(1)

# Get a handle to the system bus
bus = dbus.SystemBus()

# Get a handle to the BlueZ service
bluez_service = bus.get_object('org.bluez', '/')

# Get a handle to the BlueZ manager interface
manager_iface = dbus.Interface(bluez_service, 'org.freedesktop.DBus.ObjectManager')

# Get a list of all the objects on the system bus
objects = manager_iface.GetManagedObjects()

# Find the device object with the correct MAC address
device_path = None
for path, interfaces in objects.items():
    if 'org.bluez.Device1' in interfaces and interfaces['org.bluez.Device1'].get('Address') == device_mac_address:
        device_path = path
        break

if not device_path:
    print(f"Device with MAC address {device_mac_address} not found")
    exit(1)

# Get a handle to the device object
device_obj = bus.get_object('org.bluez', device_path)

# Get a handle to the GATT service object
service_path = None
for path, interfaces in objects.items():
    if 'org.bluez.GattService1' in interfaces and interfaces['org.bluez.GattService1'].get('UUID') == service_uuid:
        service_path = path
        break

if not service_path:
    print(f"GATT service with UUID {service_uuid} not found")
    exit(1)

service_obj = bus.get_object('org.bluez', service_path)

# Get a handle to the GATT characteristic object
char_path = None
for path, interfaces in objects.items():
    if 'org.bluez.GattCharacteristic1' in interfaces and interfaces['org.bluez.GattCharacteristic1'].get('UUID') == char_uuid:
        char_path = path
        break

if not char_path:
    print(f"GATT characteristic with UUID {char_uuid} not found")
    exit(1)

char_obj = bus.get_object('org.bluez', char_path)

# Convert the value to bytes
value_bytes = value.to_bytes(1, byteorder='little')

# Write the value to the characteristic
char_iface = dbus.Interface(char_obj, 'org.bluez.GattCharacteristic1')
char_iface.WriteValue(value_bytes, {})
