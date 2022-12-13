"""
--------------------------------------------------------------------------
Wakey Wakey - GPS
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


"""

# GPS takes coordinates in in WGS-84 format: __°__'__" N/S, __°__'__" E/W 
# I could not find code to take in location data from the specific GPS module that I ordered, so I am using a generic method. This method produces coordinates in decimal format rather than minutes-seconds format.

def get_coordinates():
    # Could not find code of how to use a GPS module to generate device's current coordinates. However, I did find a review on Amazon saying the module that I ordered was particularly difficult for beginner programmers to use.
    # Latitude and longitude values will be initialized as the coordinates of Houston, TX so this device will be great for Houstonians!
    Latitude = """29° 44' 59.6652'' N"""
    Longitude = """95° 21' 30.3156'' W"""
    return [Latitude, Longitude]