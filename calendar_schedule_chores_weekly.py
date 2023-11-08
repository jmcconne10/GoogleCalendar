# In this version, we iterate through the rows then call the function to connect and create the event. It may be more efficient to flip those.
# This is to schedule single all day events
# Input file must be in format yyyy-mm-dd

from datetime import datetime, timedelta

#from datetime import datetime, timedelta
from cal_setup import get_calendar_service

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
    date = '2023-11-24'


    #Inelegant way of getting 4 kids through each of the 4 chores. 
    for x in range(90):

        d = datetime.strptime(date, "%Y-%m-%d") #Converts above string to datetime object
        d = d + timedelta(days=1) #Adds a day
        d = d.date() #strips the hours from object
        dStr = str(d) #converts to string
        date = dStr
        day_of_week = d.weekday()

        print(dStr)
        print(get_day_of_week(dStr, day_of_week))

def get_day_of_week(d, day_value):
    if day_value == 0:
        event = 'Dish Bre - Trash E'
        createEvent(d,event)
        return "Monday"
    elif day_value == 1:
        event = 'Dish Bro- Trash Bre'
        createEvent(d,event)
        return "Tuesday"
    elif day_value == 2:
        event = 'Dish RC - Trash E'
        createEvent(d,event)
        return "Wednesday"
    elif day_value == 3:
        event = 'Dish Bre - Trash Bro'
        createEvent(d,event) 
        return "Thursday"
    elif day_value == 4:
        event = 'Dish Bro- Trash RC'
        createEvent(d,event)
        return "Friday"
    elif day_value == 5:
        event = 'Dish RC - Trash Bre'
        createEvent(d,event)
        return "Saturday"
    elif day_value == 6:
        event = 'Dish E- Trash Bro'
        createEvent(d,event)
        return "Sunday"
    else:
        return "Invalid day value" 

if __name__ == '__main__':
   main()