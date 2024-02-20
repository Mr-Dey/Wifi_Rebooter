import wmi
c=wmi.WMI()
devices=c.Win32_PnPEntity()
my_devices=["D-Link DWA-131 Wireless N Nano USB Adapter(rev.E)","Bluetooth Device (Personal Area Network)"]

device_index=int(input("".join(f"[{x}] -> {device}\n" for x,device in enumerate(my_devices))+"\nSelect a device => "))

if(device_index in range(0,len(my_devices))):
    print("Finding the device")
    for x in range(len(devices)):
        if devices[x].Caption==my_devices[device_index]:
            print("Found the device, Trying to reboot")
            devices[x].Disable()
            devices[x].Enable()
            print("Reboot sucessfull.")
            break
