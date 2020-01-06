# photoBoothQ

Small project to create a Photo Booth for my older brother's wedding
This project we coded in python 2.7 on a raspberry pi, we used the following packages:
* pygame
* picamera
We needed the following material:
* A raspberry pi to run the interface
* A picamera
* A touch screen
* Some speakers for the sound
* A nice box where to put all this
Before running interface.py (which is the main program) you need to make sure that your onboard GPU has enough memory:
* check in `raspi config`
* In Advanced options -> Memory split check that you have 256 Mb

## How it works
The interface built with pygame waits for the click of the user (ie the touch on the touch screen) to trigger a countdown and the picture at the end of it, A random noise is chosen among a list along a random message to give a little surprise to the persons using the device. We built a wrapper of picamera so that the interface can use it more smoothly.

## Cautions
Sounds and pictures are not to be used for commercial purposes

Amateur work please be kind ;)

Here is our wonderful but not perfect box for holding everything

![Nice Box](https://raw.githubusercontent.com/williampiat3/photoBoothQ/master/nice_box.jpg "Niiiice")

