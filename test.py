import gflags
import httplib2

from apiclient.discovery import build
from oauth2client.file import Storage
from oauth2client.client import OAuth2WebServerFlow
from oauth2client.tools import run
from CalendarHelperFunctions import duration

FLAGS = gflags.FLAGS

# Set up a Flow object to be used if we need to authenticate. This
# sample uses OAuth 2.0, and we set up the OAuth2WebServerFlow with
# the information it needs to authenticate. Note that it is called
# the Web Server Flow, but it can also handle the flow for native
# applications
# The client_id and client_secret are copied from the API Access tab on
# the Google APIs Console
FLOW = OAuth2WebServerFlow(
    client_id='65056611106.apps.googleusercontent.com',
    client_secret='qMzPW-5wrmCUn0D6E-izxq03',
    scope='https://www.googleapis.com/auth/calendar',
    user_agent='PrintCalendar/0.1')

# To disable the local server feature, uncomment the following line:
# FLAGS.auth_local_webserver = False

# If the Credentials don't exist or are invalid, run through the native client
# flow. The Storage object will ensure that if successful the good
# Credentials will get written back to a file.
storage = Storage('calendar.dat')
credentials = storage.get()
if credentials is None or credentials.invalid == True:
  credentials = run(FLOW, storage)

# Create an httplib2.Http object to handle our HTTP requests and authorize it
# with our good Credentials.
http = httplib2.Http()
http = credentials.authorize(http)

# Build a service object for interacting with the API. Visit
# the Google APIs Console
# to get a developerKey for your own application.
service = build(serviceName='calendar', version='v3', http=http,
       developerKey='AIzaSyDFNRC0qG6KBQt1t7qK3WZTHuAK2R8KQ9s')
       
       
       
calendar = service.calendars().get(calendarId='primary').execute()

page_token = None
while True:
  events = service.events().list(calendarId='primary', pageToken=page_token,timeMin='2013-03-08T00:00:00Z',timeMax='2013-03-10T00:00:00Z').execute()
  if events['items']:
    for event in events['items']:
      start=  event['start']['dateTime']
      end = event['end']['dateTime']
      delta = duration(start,end)
      print event['summary'], delta
  page_token = events.get('nextPageToken')
  if not page_token:
    break
    
    
