# In this version, we iterate through the rows then call the function to connect and create the event. It may be more efficient to flip those.
# This is to schedule single all day events
# Input file must be in format yyyy-mm-dd

from datetime import datetime, timedelta
from cal_setup import get_calendar_service
import pandas as pd

# This function takes the date, time, and event name, connects to the Google Calendar and creates the event
def createEvent(strDate,event):
    #set date & time
    strDate

    # creates one hour event tomorrow 10 AM IST
    service = get_calendar_service()
    
    event_result = service.events().insert(calendarId='primary',
       body={
           "summary": event,
           "description": 'This is a tutorial example of automating google calendar with python',
           "start": {"date": strDate, "timeZone": 'America/Chicago'},
           "end": {"date": strDate, "timeZone": 'America/Chicago'},
       }
   ).execute()
    
#
def main():
    
    #open up file
    reader = pd.read_csv("testCalendar.csv")

    for index, row in reader.iterrows():
        createEvent(row['Date'],row['Event'])     

if __name__ == '__main__':
   main()