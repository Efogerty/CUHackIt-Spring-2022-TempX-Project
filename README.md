# TempX CUhackit
 This project was done in 15 hours during a Hackathon Event hosted at Clemson. \
 This team won the Best Twilio Implementation Award. 
# Project Description
 This project was to notify the user if their skin temperature surpassed a threshold \
 We implemented fullstack developement skills and hardware skills to achieve a mobile device that would send pings to your phone
# Software and Hardware
 We used an analog temperature sensor connected to a arduino \
 The data collected by the arduino was then serialized to a raspberry pi (OS DietPi) \
 The raspberry pi would run a python script and then send data (Fahrenheit Temperature) to a cloud server \
 If the raspberry pi found that the temperature surpassed 96 degrees Fahrenheit the user would recieve a text message \
 The cloud server would then send the data to an api called Grafana which would visual the data \
 We then created a simple website on our own domain \
 This website had embeded graphs\data from Grafana that would update every 5 seconds 
