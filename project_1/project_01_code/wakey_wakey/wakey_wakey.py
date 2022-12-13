"""
--------------------------------------------------------------------------
Wakey Wakey
--------------------------------------------------------------------------
License:   
Copyright 2022 Garrett French

Redistribution and use in source and binary forms, with or without 
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this 
list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, 
this list of conditions and the following disclaimer in the documentation 
and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors 
may be used to endorse or promote products derived from this software without 
specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE 
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE 
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE 
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL 
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR 
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER 
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, 
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE 
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
--------------------------------------------------------------------------

Use three buttons, a Wifi module, a Bluetooth module, and a GPS module for an
alarm clock that has spatial awareness, can tell weather data for its current
location, and can perform the regular functions of an alarm clock.

Sourced codes:
https://beagleboard.org/p/beaglefriends-octavosystems/pocketbeagle-alexa-0425b6
https://beagleboard.org/p/manoj-kurapati/ece497-project-alarm-with-remote-speaker-5eae5d

"""

# Import necessary packages
import signal
import subprocess
import Adafruit_BBIO.GPIO as GPIO
import time
import datetime
import os
import wifi
import gps

class Wakey_Wakey():
    """ People Counter """
    button1    = None
    button2    = None
    button3    = None
    button4    = None
    button5    = None
    display    = None
    gpsmod     = None
    btmod      = None
    wifimod    = None
    



# Setup
ampm = 0
alarm = 0
alarm_hour = 0 
alarm_minute = 0 
proc = None #Setup Proc for sound playing

# Initialize Buttons - refer to project proposal for the button uses
button1= "P2_01"
button2="P2_02"
button3= "P2_03"  
button4="P2_04"
button5="P2_05"

# Set correct functions for buttons and LEDs
GPIO.setup(button1, GPIO.IN)
GPIO.setup(button2, GPIO.IN)
GPIO.setup(button3, GPIO.IN)
GPIO.setup(button4, GPIO.IN)
GPIO.setup(button5, GPIO.IN)

def update(): #Main method to update display
    global ampm
    global alarm
    global alarm_hour
    global alarm_minute
    while(1):
        #Continually check for correct time
        datetime_hour = datetime.datetime.now().hour
        minute = datetime.datetime.now().minute
        hour = datetime_hour
        alarm_hour_ampm = alarm_hour

        #Correction for 24 hour time
        if datetime_hour > 12:
            hour = datetime_hour - 12
        if alarm_hour > 12:
            alarm_hour_ampm = alarm_hour - 12

        #Turning Alarm on at correct time
        if alarm == 1 and alarm_hour == datetime_hour and alarm_minute == minute:
            alarm_on()
            alarm = 0
            GPIO.output(LEDalarmOnOff, alarm)
        
        #Showing Alarm or setting time
        if GPIO.input("P9_02"):
            set_7seg(alarm_hour_ampm, alarm_minute)
            if alarm_hour < 12:
                ampm = 0
            else:
                ampm = 1
        else:
            set_7seg(hour, minute)
            if datetime_hour < 12:
                ampm = 0
            else:
                ampm = 1
        print('Display updated')
    return 0

def alarm_on():
    global proc
    #Running cvlc from console for youtube.  Enter desired youtube link here.
    proc = subprocess.Popen(['cvlc', '--no-video', 'https://www.youtube.com/watch?v=U68MJz9DrI4'])
    print('Alarm running')
    return 0

def alarm_off(channel):
    #Killing cvlc to turn off alarm
    global proc
    proc.send_signal(signal.SIGINT)
    print('Alarm off')
    return 0

#Setting Alarm Hour
def set_alarm_hour(channel):
    global alarm_hour
    if alarm_hour == 23:
        alarm_hour = 0
    else:
        alarm_hour = alarm_hour + 1
    return 0

#Setting Alarm minute        
def set_alarm_minute(channel):
    global alarm_minute
    if alarm_minute == 59:
        alarm_minute = 0
    else:
        alarm_minute = alarm_minute + 1
    return 0

#Write to display
def set_7seg(hour, minute):
    segment.clear()
    # Set hours
    segment.set_digit(0, int(hour / 10))     
    segment.set_digit(1, hour % 10)          
    # Set minutes
    segment.set_digit(2, int(minute / 10))   
    segment.set_digit(3, minute % 10)        
    # Toggle colon
    segment.set_colon(datetime.datetime.now().second % 2)              
    
    # Update the actual display LEDs.
    segment.write_display()

    # Wait a quarter second
    time.sleep(0.25)
    print('Display displaying')
    return 0

#GPIO Events for button presses
GPIO.add_event_detect(buttonSnooze, GPIO.FALLING, callback=alarm_off, bouncetime=200) 
GPIO.add_event_detect(buttonHour, GPIO.FALLING, callback=set_alarm_hour, bouncetime=200) 
GPIO.add_event_detect(buttonMinute, GPIO.FALLING, callback=set_alarm_minute, bouncetime=200)
GPIO.add_event_detect(buttonAlarmToggle, GPIO.FALLING, callback=alarm_toggle, bouncetime=200)

#Call the main function
update()


# ------------------------------------------------------------------------
# Main script
# ------------------------------------------------------------------------

if __name__ == '__main__':

    print("Program Start")

    wakey_wakey = Wakey_Wakey()
    
    try:
    # Run wakey_wakey
    wakey_wakey.run()

    except KeyboardInterrupt:
    
    print("Program Complete")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# OTHER PROJECT
import signal
import subprocess
import Adafruit_BBIO.GPIO as GPIO
import time
import datetime
import os
from Adafruit_LED_Backpack import SevenSegment

# Setup
ampm = 0 # AM/PM Flag
alarm = 0 # Alarm Flag
alarm_hour = 0 
alarm_minute = 0 
segment = SevenSegment.SevenSegment(address=0x70, busnum=2) #Set up Seven Segment on corrent Bus
segment.begin()
proc = None #Setup Proc for sound playing

buttonSnooze= "P2_21"  #InitializeButtons
buttonSetAlarm="P2_22"
buttonHour= "P2_23"  
buttonMinute="P2_24"
buttonAlarmToggle="P2_25"

LEDalarmOnOff="P2_26" #Initialize LEDs
LEDampm="P2_27"

GPIO.setup(buttonSnooze, GPIO.IN) #Set correct functions for buttons and LEDs
GPIO.setup(buttonSetAlarm, GPIO.IN)
GPIO.setup(buttonHour, GPIO.IN)
GPIO.setup(buttonMinute, GPIO.IN)
GPIO.setup(buttonAlarmToggle, GPIO.IN)
GPIO.setup(LEDalarmOnOff, GPIO.OUT)
GPIO.setup(LEDampm, GPIO.OUT)


GPIO.output(LEDalarmOnOff, alarm)

def update(): #Main method to update Seven Segment Display
    global ampm
    global alarm
    global alarm_hour
    global alarm_minute
    while(1):
        #Continually check for correct time
        datetime_hour = datetime.datetime.now().hour
        minute = datetime.datetime.now().minute
        hour = datetime_hour
        alarm_hour_ampm = alarm_hour

        #Correction for 24 our time
        if datetime_hour > 12:
            hour = datetime_hour - 12
        if alarm_hour > 12:
            alarm_hour_ampm = alarm_hour - 12

        #Turning Alarm on at correct time
        if alarm == 1 and alarm_hour == datetime_hour and alarm_minute == minute:
            alarm_on()
            alarm = 0
            GPIO.output(LEDalarmOnOff, alarm)
        
        #Showing Alarm or setting time
        if GPIO.input("P9_22"):
            set_7seg(alarm_hour_ampm, alarm_minute)
            if alarm_hour < 12:
                ampm = 0
            else:
                ampm = 1
        else:
            set_7seg(hour, minute)
            if datetime_hour < 12:
                ampm = 0
            else:
                ampm = 1
        GPIO.output(LEDampm, ampm) #Setting AM/PM LED

def alarm_on():
    global proc
    #Running cvlc from console for youtube.  Enter desired youtube link here.
    proc = subprocess.Popen(['cvlc', '--no-video', 'https://www.youtube.com/watch?v=nPRHumwZfk4'])
    return 0

def alarm_off(channel):
    #Killing cvlc to turn off alarm
    global proc
    proc.send_signal(signal.SIGINT) 
    return 0

#Turn Alarm on or off
def alarm_toggle(channel):
    global alarm
    if alarm == 1:
        alarm = 0
    else:
        alarm = 1
    GPIO.output(LEDalarmOnOff, alarm)

#Setting Alarm Hour
def set_alarm_hour(channel):
    global alarm_hour
    if alarm_hour == 23:
        alarm_hour = 0
    else:
        alarm_hour = alarm_hour + 1

#Setting Alarm minute        
def set_alarm_minute(channel):
    global alarm_minute
    if alarm_minute == 59:
        alarm_minute = 0
    else:
        alarm_minute = alarm_minute + 1

#Write to Seven Segment
def set_7seg(hour, minute):
    segment.clear()
    # Set hours
    segment.set_digit(0, int(hour / 10))     
    segment.set_digit(1, hour % 10)          
    # Set minutes
    segment.set_digit(2, int(minute / 10))   
    segment.set_digit(3, minute % 10)        
    # Toggle colon
    segment.set_colon(datetime.datetime.now().second % 2)              
    
    # Update the actual display LEDs.
    segment.write_display()

    # Wait a quarter second
    time.sleep(0.25)
    return 0

#GPIO Events for button presses
GPIO.add_event_detect(buttonSnooze, GPIO.FALLING, callback=alarm_off, bouncetime=200) 
GPIO.add_event_detect(buttonHour, GPIO.FALLING, callback=set_alarm_hour, bouncetime=200) 
GPIO.add_event_detect(buttonMinute, GPIO.FALLING, callback=set_alarm_minute, bouncetime=200)
GPIO.add_event_detect(buttonAlarmToggle, GPIO.FALLING, callback=alarm_toggle, bouncetime=200)

#Call the main function
update()