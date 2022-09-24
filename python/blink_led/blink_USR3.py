# -*- coding: utf-8 -*-
"""
--------------------------------------------------------------------------
USR3 Blink for PocketBeagle
--------------------------------------------------------------------------
License:   
Copyright 2022 - Charles French

Redistribution and use in source and binary forms, with or without 
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, 
this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, 
this list of conditions and the following disclaimer in the documentation 
and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors 
may be used to endorse or promote products derived from this software without 
specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE 
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE 
ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE 
LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR 
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF 
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS 
INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN 
CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) 
ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF 
THE POSSIBILITY OF SUCH DAMAGE.
--------------------------------------------------------------------------

This program will cause the USR3 LED on the PocketBeagle to blink at a
frequency of 5 Hz.

--------------------------------------------------------------------------
"""

import Adafruit_BBIO.GPIO as GPIO
import time
# Imports relevant librarires

GPIO.setup("USR3", GPIO.OUT)
# From ADAFruit

while True:
    GPIO.output("USR3", GPIO.HIGH)
    time.sleep(0.1)
    # Turns USR3 on for 0.1 second
    
    GPIO.output("USR3", GPIO.LOW)
    time.sleep(0.1)
    # Turns USR3 off for 0.1 second
    
    # NOTE: An on period of 0.1 seconds followed by an off period of 0.1 seconds
    # creates a period of 0.2 seconds, which will cycle 5 times in 1 second,
    # and thus the frequency of the blinking is 5 Hz.