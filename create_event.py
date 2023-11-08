from datetime import datetime, timedelta
from cal_setup import get_calendar_service


def main():

    #set date & time
    strdate="24-03-2022"
    strtime="13:00:00"
    strDateTime= strdate + " " + strtime

    #convert to datetime object
    datetimeobj=datetime.strptime(strDateTime,"%d-%m-%Y %H:%M:%S")

    # creates one hour event tomorrow 10 AM IST
    service = get_calendar_service()

    start = datetimeobj.isoformat()
    end = (datetimeobj + timedelta(hours=1)).isoformat()
    
    event_result = service.events().insert(calendarId='primary',
       body={
           "summary": 'Attempt20',
           "description": 'This is a tutorial example of automating google calendar with python',
           "start": {"dateTime": start, "timeZone": 'America/Chicago'},
           "end": {"dateTime": end, "timeZone": 'America/Chicago'},
       }
   ).execute()
    

    print("created event on date ", start)
    print("id: ", event_result['id'])
    print("summary: ", event_result['summary'])
    print("starts at: ", event_result['start']['dateTime'])
    print("ends at: ", event_result['end']['dateTime'])
    

if __name__ == '__main__':
   main()