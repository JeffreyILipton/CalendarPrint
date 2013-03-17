from MET import MetDict



def duration(start, end):
        [sdate, stime] = start.split('T')
        [edate,etime] = end.split('T')
        
        startList = stime.split('-')[0].split(':')
        smin = float(startList[0])*60.0+float(startList[1])
        
        
        endList = etime.split('-')[0].split(':')
        
        emin = float(endList[0])*60.0+float(endList[1])
        
        delta = emin-smin
        return delta
        
def calsBurned(summary, time, person):
    if MetDict.has_key(summary) :
        met = MetDict[summary]
        return time*met*person.weight/200.0
    else:
        return 0.0
        

def eaten(eventsList):
    cals = 0
    for pair in eventsList:
        summaryList = pair[0].split(":")
        if ( len(summaryList)==2 and(summaryList[0].lower() == "ate")):
            cals += float(summaryList[1])
    return cals
    
    
def burned(eventsList, person):
    cals = 0
    for pair in eventsList:
        cals += calsBurned(pair[0], pair[1], person)
    return cals
    
    
    
    