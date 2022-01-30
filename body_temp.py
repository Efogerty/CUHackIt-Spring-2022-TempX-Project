__version__ = '0.0.1'
required = ['datetime', 'pandas', 'twilio.rest', 'RPi.GPIO','serial', 're']
import datetime
import meerschaum as mrsm

setpoint = 96
user_number = "8433194801"

####Texts an alert to the phone of the user if their tempeture is above a setpoint
def text(sense, value):
    from twilio.rest import Client
    import pandas as pd
    import datetime

    #hide in a future version
    account_sid = "ACe6afa5701f07612f5acedb2a39552ea3"
    auth_token = "c7636fe1c209764b22cdac7495a82a7d"

    cur_time = datetime.datetime.utcnow()
    bucket = mrsm.Pipe("bucket", "last_call", instance="sql:local", columns={'datetime':'utcdatetime'})

    data = {"cur_time":[cur_time]}
    df = pd.DataFrame(data)
    suc, msg = bucket.sync(df)
    if not suc:
        return suc, msg

    #sets up the api
    client = Client(account_sid, auth_token)
    
    #creates the message being sent
    message = client.messages.create(
    to=user_number,
    from_="7754145760",
    body=f"your current tempeture at {sense} is {value} \nyou're in danger")
    #prints message
    print(message.sid)

#####sets up serialization of the usb connector and takes the median of 1 second of data recording#####
def get_temp_sec():
    import serial
    import pandas as pd
    import re
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.reset_input_buffer()
    #time collection to measure a second
    start = datetime.datetime.utcnow()
    end = datetime.datetime.utcnow()
    #storage for the dataframe
    data = {"readings":[]}
    while end - start < datetime.timedelta(seconds = 1):
        end = datetime.datetime.utcnow()
        #if there is data in the serial port
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            #save the float value from a string
            if line != "":
                data["readings"] += re.findall("\d+\.\d+",line)

    df = pd.DataFrame(data)
    #pulls the median out of the dataframe
    med = df.median()['readings']
    return med

    
####main of the function, returns the data tothe database####
def sync(pipe, **kw):
    import pandas as pd
    import datetime
    import RPi.GPIO as GPIO

    #grabs the value
    input_val = get_temp_sec()

    #gets the current time at time of inputs end
    cur_time = datetime.datetime.utcnow()
    #sets up the lists for the datafrome to be expanded upon with more sensors
    Sensor_List = [1]
    Input_List = [(input_val*(9.0/5.0)+32)]
    Time_List = [cur_time]

    #checks if the read value is above the setpoint
    bucket = mrsm.Pipe("bucket", "last_call", instance="sql:local", columns={'datetime':'utcdatetime'})
    bucket_last = bucket.get_sync_time(newest=True)
    last = (
        bucket_last if bucket_last is not None
        else cur_time - datetime.timedelta(minutes = 2)
    )

    print(bucket_last)
    print(last)

    if(cur_time - last >= datetime.timedelta(minutes = 1)):
        print("made it")
        if Input_List[0] > setpoint:
            print(Input_List)
            text(Sensor_List[0], Input_List[0])

    #loads dataframe
    data = {'utcdatetime':Time_List, 'sensor_id':Sensor_List, 'value': Input_List }
    df = pd.DataFrame(data)


    #returns dataframe to the database
    return pipe.sync(df)