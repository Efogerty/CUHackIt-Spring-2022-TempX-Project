# TempX - CUhackit 2022
## Keaton Myers, Isaiah Griner, Jenna Hofseth, Evan Fogerty
 This project was done in 15 hours during a Hackathon Event hosted at Clemson. \
 Our team's project won the Best Twilio Implementation Award. 
# Project Description
 Our project consists of an Arduino and Raspberry Pi device connected to temperature sensor nodes that a user would attach to various points on their body in order to track skin temperature. \
 The Arduino manages the analog readings from the temperature sensors, whereas the Pi manages communication with a TimeScale database and Twilio. If the wearer of the device passes a certain threshold when their skin temperature is measured, the Pi's script will use Twilio in order to send a message to their phone notifying them of this in order to prevent medical emergencies such as skin reactions, strokes, or spiking fevers. \
 We implemented fullstack development & circuitry techniques to develop a mobile device that communicates with the user's phone and with the TempX website to passively monitor temperature readings.
# Software and Hardware
 We utilized an analog temperature sensor connected to a Arduino \
 The data collected by the arduino is then serialized to a Raspberry Pi (OS DietPi) to manage wireless communications \
 Then, the Pi runs a python script and iteratively sends data (temperature readings, in Fahrenheit) to a Timescale database \
 If the Raspberry Pi found that the temperature surpassed 96 degrees Fahrenheit (the set threshold), the user recieves a text message notifying them of that and their temperature reading that surpassed the threshold \
 The cloud server can then send the data to Grafana, which helps to visualize data readings \
 We then created a simple website on our own domain using Bootstrap, HTML, and CSS. \
 This website has embeded graphs\data from Grafana that updates every 5 seconds when the user wears the device
