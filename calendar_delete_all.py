import datetime
from cal_setup import get_calendar_service

def main():
    service = get_calendar_service()
    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    print('Lists events as it deletes')
    events_result = service.events().list(
       calendarId='primary', timeMin=now,
       maxResults=100, singleEvents=True,
       orderBy='startTime').execute()
    events = events_result.get('items', [])

    i = 0

    if not events:
       print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        info = event['summary'] + ' ' + event['id']
        print(info)
        i = i + 1
        service.events().delete(
            calendarId='primary',
            eventId=event['id'],
        ).execute()
        
    print('Deleted ' + str(i) + ' events')
if __name__ == '__main__':
   main()