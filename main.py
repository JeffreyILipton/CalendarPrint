from CalendarInterface import getEvents
from CalendarHelperFunctions import *
from person import Person
from MakeCookie import *





guy = Person("jeff",25,240/2.2,(5*12+10)*2.54,'male')    

eventList = getEvents('2013-03-24T00:00:00Z','2013-03-25T00:00:00Z')
#eventList.append(("ate:2000",60))
#eventList.append(("running",30))
calsEaten = eaten(eventList)
calsBurned = burned(eventList,guy)

guy.ate(calsEaten)
guy.exercised(calsBurned)

makeCookie(guy.calRemaining()*0.05)

print eventList
guy.printSelf()

