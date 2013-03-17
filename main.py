from CalendarInterface import getEvents
from CalendarHelperFunctions import *
from person import Person





guy = Person("jeff",25,240/2.2,(5*12+10)*2.54,'male')    

eventList = getEvents('2013-03-08T00:00:00Z','2013-03-10T00:00:00Z')
eventList.append(("ate:2000",60))
eventList.append(("running",30))
calsEaten = eaten(eventList)
calsBurned = burned(eventList,guy)

guy.ate(calsEaten)
guy.exercised(calsBurned)



print eventList
guy.printSelf()

