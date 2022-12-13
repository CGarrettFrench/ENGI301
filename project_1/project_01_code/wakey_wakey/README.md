# Wakey Wakey
Created by Garrett French, Rice University, ENGI 301 F22 

## Installing Necessary Packages
1. `Bone:~/wakey_wakey/$ ./install.sh`

## Set up Bluetooth Files
1. `Bone:~/wakey_wakey/$ sudo nano /usr/share/alsa/alsa.conf`
2. Change defaults.ctl.card and defaults.pcm.card variables to 1
3. `Bone:~/project_01/$ mv daemon.txt daemon.comp`
4. `Bone:~/project_01/$ sudo cp daemon.comf /etc/pulse`
5. `Bone:~/project_01/$ sudo nano /etc/pulse/daemon.conf`
6. Remove the semicolons in front of "high-priority" and "exit-idle-time," and change their values to "yes" and "86400," respectively.

## Setting up Bluetooth
1. `Bone:~/project_01/$ pulseaudio --start`
2. `Bone:~/project_01/$ bluetoothctl`
3. `[Bluetooth] scan on`
4. Search for your Bluetooth Device Address
5. `[Bluetooth] pair (insert device Address here)`
6. `[Bluetooth] tust (insert device Address here)`
7. `[Bluetooth] connect (insert device Address here)`
8. `[Device name] exit`

## Setting up WiFi capabilities
1. In wify.py, for the line: YOUR_API_KEY = "Enter your API key here", delete the apostrophed text and replace it with the key associated with your API account. If you do not have an account, go to https://www.visualcrossing.com/weather/weather-data-services and make one, then you can find your key by clicking "Account."

## Ensuring Modules are Connected
Use command lsusb to see USB devices to ensure that they are connected properly.

If the connection is giving you issues, try `pulseaudio -k` to kill it and `pulseaudio --start` to restart it.  Then open the Bluetooth menu to try and connect again.

## Changing Youtube Video
The video that is played for the alarm can be changed by opening wakey_wakey.py and changing "https://www.youtube.com/watch?v=U68MJz9DrI4" in the following line: "proc = subprocess.Popen(['cvlc', '--no-video', 'https://www.youtube.com/watch?v=U68MJz9DrI4'])" to the link to a YouTube video with the desired alarm audio. 

## More information
A complete description of this project can be found on Hackster.io (https://www.hackster.io/manoj-kurapati/ece497-project-alarm-with-remote-speaker-5eae5d).
