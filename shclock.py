#!/usr/bin/python3

from sense_hat import SenseHat
import time

sense = SenseHat()

sense.set_rotation(180)
sense.low_light = True

number = [
0,1,1,1, # Zero
0,1,0,1,
0,1,0,1,
0,1,1,1,
0,0,1,0, # One
0,1,1,0,
0,0,1,0,
0,1,1,1,
0,1,1,1, # Two
0,0,1,1,
0,1,1,0,
0,1,1,1,
0,1,1,1, # Three
0,0,1,1,
0,0,1,1,
0,1,1,1,
0,1,0,1, # Four
0,1,1,1,
0,0,0,1,
0,0,0,1,
0,1,1,1, # Five
0,1,1,0,
0,0,1,1,
0,1,1,1,
0,1,0,0, # Six
0,1,1,1,
0,1,0,1,
0,1,1,1,
0,1,1,1, # Seven
0,0,0,1,
0,0,1,0,
0,1,0,0,
0,1,1,1, # Eight
0,1,1,1,
0,1,1,1,
0,1,1,1,
0,1,1,1, # Nine
0,1,0,1,
0,1,1,1,
0,0,0,1
]

hour_color = [0,0,255] # Blue
hour_half_bright = [0,0,128] # Blue for inside of 8
minute_color = [248,226,55] # GeekPub Yellow
minute_half_bright = [124,113,27] # GeekPub Yellow for inside of 8
empty = [0,0,0] # Black

clock_image = [
0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0
]

while True:
  hour = time.localtime().tm_hour
  minute = time.localtime().tm_min

  # Map digits to the clock_image array
  pixel_offset = 0
  index = 0
  for index_loop in range(0, 4):
    for counter_loop in range(0, 4):
      if (hour < 10):
        clock_image[index] = number[pixel_offset]
      else:
        clock_image[index] = number[int(hour/10)*16+pixel_offset]
      clock_image[index+4] = number[int(hour%10)*16+pixel_offset]
      clock_image[index+32] = number[int(minute/10)*16+pixel_offset]
      clock_image[index+36] = number[int(minute%10)*16+pixel_offset]
      pixel_offset = pixel_offset + 1
      index = index + 1
    index = index + 4

  # Color the hours and minutes
  for index in range(0, 64):
    if (clock_image[index]):
      if index < 32:
        clock_image[index] = hour_color
      else:
        clock_image[index] = minute_color
    else:
      clock_image[index] = empty
  # Set the inside two pixels in any 3 and 8 to half bright
  if str(hour)[-1] == '3' or str(hour)[-1] == '8':
    clock_image[14] = hour_half_bright
    clock_image[22] = hour_half_bright
  if str(minute)[0] == '3':
      clock_image[42] = minute_half_bright
      clock_image[50] = minute_half_bright
  if str(minute)[-1] == '3' or str(minute)[-1] == '8':
    clock_image[46] = minute_half_bright
    clock_image[54] = minute_half_bright

  # Display the time
  sense.low_light = True # Optional
  sense.set_pixels(clock_image)
  time.sleep(1)
