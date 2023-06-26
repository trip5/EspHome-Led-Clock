# EspHome-Sinilink-Clock

EHSC is meant to be used on ESP-based Sinilink Wifi XY-Clocks using ESPHome. It can probably be adapted for use with other 7-Segment Display clocks. And, of course, it's ESPHome, so it's only limited by your imagination and skill.

![image](.\images\sinilink_XY-Clock.jpg)  This is the link on Aliexpress I have personally used but I am sure there are others:
https://www.aliexpress.com/item/1005004427096126.html

A lot of inspiration is taken from the [EHMTXv2](https://github.com/lubeda/EspHoMaTriXv2) project... but with a TM1650 display.

Integration with Home Assistant is recommended.

It requires the tm1650 display to be supported by external component - at least until ESPHome has native support.  A link is provided by my own fork of buzzer13's repo.

The Tasmota device profile has some useful information, especially on how to flash this with a custom firmware: https://templates.blakadder.com/XY-Clock.html

The file [`EHSClock.yaml`](EHSClock.yaml) contains the full YAML code.