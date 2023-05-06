# Raspberry PI Documentation
### Revision 1.0 (Pending Approval)

This contains the all of the documentation for the onboard raspberry pi.


---


## SECTION 1
### STARTUP

In order to safely startup the Raspberry Pi into its functional state, you must first make sure a number of conditions are met:

Insure that the main power is turned on and supplied to the rover.
Check the current and voltage and make sure that they are within the nominal specifications.
Check all physical connections to and from the Pi.
After confirming all of these, you may now begin the startup. First, you must connect the USB power cable to some kind of external USB power supply. The power supply must supply no more than 5.1 volts, or it must be explicitly approved. Once the power supply is connected, you should see the red PWR light turn on. If this is not the case, then unplug the USB and start troubleshooting (see Section 3). If you do not have a monitor plugged into the Pi, you can safely skip these next steps. If the red PWR light has turned on, you should see a boot screen. If no boot screen shows, see Section 3. Wait until you get to a desktop environment. Please note that this can take up to a minute. If you still haven't gotten to the desktop after a minute, see Section 3. If you do have a monitor connected to the Pi, you can safely skip these next steps. If the red PWR light has turned on, wait to see if the green ACT light flickers at all. If it does not, see Section 3. On a Windows 10 or higher device, open an ip scanner (I recommend wireless network watcher) and look for a new device with the hostname raspberrypi. (Please note that this is subject to change and will be updated here.) Find its IP address, then open PuTTY. Using the ssh protocol, remote into the Raspberry Pi with the following details: USERNAME: pi PASSWORD: pi (Subject to change, this will be updated here.) If you cannot ssh into the Pi, see Section 3. The following instructions apply to both displays and no displays. In order to start the Node Red server, you must execute the command node-red in a bash terminal. In PuTTY, you will by default be in a bash terminal. In the desktop environment, you must open the terminal shortcut in the start menu (of course, in the Raspberry Pi desktop environment). With that, the Raspberry Pi has been started up with node-red running. Once more services have been added, there will be a unified script to start everything up.

This concludes Section 1.

Section 2
SHUTDOWN
In order to shutdown the Raspberry Pi safely, you must follow these instructions.

First, make sure that the rover is not currently executing an instruction. If it is either waiting for the instructions to finish or you can shutdown the Raspberry Pi, however, there is no guarantee that the rover will not be left in a non-functional or degraded state. Once you have checked the instruction status and made a decision, the actual shutdown process is quite simple. First, you must open a bash terminal. From the bash terminal, you can now execute sudo shutdown. After that, the Raspberry Pi will close all of the programmes and shut down. Once the green ACT light has turned off, you may unplug the power to the Pi.

This concludes Section 2.

Section 3
TROUBLESHOOTING
If the Pi will not boot, there are a few steps you must follow. If you have a display output, then please ignore the following section: If you have no display output, check the green ACT light. If the light is solid on, it may be a problem with the Raspberry PI board itself and may need to be removed for repairs or replacement. Before removing the board, ensure that the power to the rover and Raspberry PI is off, then unplug all USB cables from the front of the device. Ensure that the USB SD card reader is still inserted in one of the blue USB ports (symbolising a USB 3.0 port). Then attempt powering it from the onboard USB C port. If the symptoms have not changed, please unplug all external connections to the Raspberry Pi and remove it from the body of the rover.

(Continuation pending) (Presumed next revision in V2.0 software)

Section 4
Xylophener code/programming
In server.py is the part of the code that is what runs the website. We located a server port, which we will use as our IP for the website. In the website, you can choose which song you want it to play, and it will. In Gui.py
