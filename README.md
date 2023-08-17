# EspHome-Sinilink-Clock

EHSC is meant to be used on ESP-based Sinilink Wifi XY-Clocks using ESPHome. It can probably be adapted for use with other 7-Segment Display clocks. And, of course, it's ESPHome, so it's only limited by your imagination and skill.

![image](./images/sinilink_XY-Clock.jpg)

This is the link on Aliexpress I have personally used but I am sure there are others:
https://www.aliexpress.com/item/1005004427096126.html

A lot of inspiration is taken from the [EHMTXv2](https://github.com/lubeda/EspHoMaTriXv2) project... but with a TM1650 display.

It requires the tm1650 display to be supported by external component - at least until ESPHome has native support.  A link is provided to my own fork of buzzer13's repo (updated to work with ESPHome 2023.06 which changed the way that ESPHome handles time).

The Tasmota device profile has some useful information, especially on how to flash this with a custom firmware: https://templates.blakadder.com/XY-Clock.html


The file [`EHSClock.yaml`](EHSClock.yaml) contains the full YAML code.


## Integration with Home Assistant

![image](./images/EHSC_Home_Assistant_message.png)

This example will send a message that will display for 3 seconds before reverting to the clock for 5 seconds, and repeat until 20 seconds is finished (if it is displaying the message, it will finish that last 3 seconds).  Unfortunately you are limited to what a TM1650 can actually display so you should probably test it out before adding it to an automation.  Decimal places will only work after the 1st or second digit since the colon actually relies on the 3rd and 4th decimal, so it's perfect for displaying weather or room temperatures or even crypto prices.

![image](./images/EHSC_Home_Assistant_tune.png)

This will play a Nokia-style tune through the piezo speaker. I recommend just doing a search for "RTTTL" and the name of the song you would like.  If you really want a lot, check out: https://picaxe.com/rtttl-ringtones-for-tune-command/

## Useful Links

What started my curiousity: https://github.com/arendst/Tasmota/discussions/15788

Tasmota Template: https://templates.blakadder.com/XY-Clock.html

About the Rtttl Buzzer: https://esphome.io/components/rtttl.html

TM 1650 External component: https://github.com/buzzer13/esphome-components

About outputting to the Display: https://esphome.io/components/display/tm1637.html?highlight=tm1637

What characters can be displayed: https://esphome.io/components/display/max7219.html#display-max7219-characters

ESPHome's Display: https://esphome.io/components/display/index.html
