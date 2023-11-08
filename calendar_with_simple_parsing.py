#In this version, we iterate through the rows then call the function to connect and create the event. It may be more efficient to flip those.
#Required format for input file dd-mm-YYYY,HH:mm:ss,eventName

from datetime import datetime, timedelta
from cal_setup import get_calendar_service
import pandas as pd

# This function takes the date, time, and event name, connects to the Google Calendar and creates the event
def createEvent(strDate,strTime,event):
    #set date & time
    strDateTime= strDate + " " + strTime

    #convert to datetime object
    datetimeobj=datetime.strptime(strDateTime,"%d-%m-%Y %H:%M:%S")

    # creates one hour event tomorrow 10 AM IST
    service = get_calendar_service()

    start = datetimeobj.isoformat()
    end = (datetimeobj + timedelta(hours=1)).isoformat()
    
    event_result = service.events().insert(calendarId='primary',
       body={
           "summary": event,
           "description": 'This is a tutorial example of automating google calendar with python',
           "start": {"dateTime": start, "timeZone": 'America/Chicago'},
           "end": {"dateTime": end, "timeZone": 'America/Chicago'},
       }
   ).execute()
    
#
def main():
    
    #open up file
    reader = pd.read_csv("testCalendar.csv")

    for index, row in reader.iterrows():
        createEvent(row['Date'],row['Time'],row['Event'])     

if __name__ == '__main__':
   main()