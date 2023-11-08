# In this version, we iterate through the rows then call the function to connect and create the event. It may be more efficient to flip those.
# This is to schedule single all day events
# Input file must be in format yyyy-mm-dd

import datetime as dt

#from datetime import datetime, timedelta
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
           "description": 'Powered by automating google calendar with python',
           "start": {"date": strDate, "timeZone": 'America/Chicago'},
           "end": {"date": strDate, "timeZone": 'America/Chicago'},
       }
   ).execute()

def main():
    
    #This is the date one day prior to when events will start being scheduled
    date = '2023-11-07'


    #Inelegant way of getting 4 kids through each of the 4 chores. 
    for x in range(10):

        d = dt.datetime.strptime(date, "%Y-%m-%d") #Converts above string to datetime object
        d = d + dt.timedelta(days=1) #Adds a day
        d = d.date() #strips the hours from object
        d = str(d) #converts to string
        date = d
        print(d)

        #print(day_of_week(d))
        #event = 'Dish E - Trash Bre'
        #createEvent(d,event)

        

if __name__ == '__main__':
   main()